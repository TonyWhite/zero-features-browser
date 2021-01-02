#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import WebKit2

class Application:
  def __init__(self):
    # Build Window
    self.window_main = Gtk.ApplicationWindow()
    self.window_main.set_icon_name(app_icon_name)
    self.window_main.set_title(app_title)
    self.window_main.resize(1066, 600)
    self.window_main.set_position(Gtk.WindowPosition.CENTER)
    self.window_main.connect("delete-event", Gtk.main_quit)
    
    # Build Header Bar
    self.header_bar = Gtk.HeaderBar()
    self.window_main.set_titlebar(self.header_bar)
    self.header_bar.set_title(app_title)
    self.header_bar.set_subtitle("Zero Features Browser")
    self.header_bar.set_show_close_button(True)
    self.header_bar.set_decoration_layout("menu:minimize,maximize,close")
    
    # Build Header Button
    self.header_button = Gtk.MenuButton()
    self.header_bar.pack_end(self.header_button)
    self.image_menu = Gtk.Image(icon_name="open-menu-symbolic")
    self.header_button.set_image(self.image_menu)
    self.header_button.set_tooltip_text("Menu")
    
    # Build Main Menu
    self.popover = Gtk.Popover()
    self.header_button.set_popover(self.popover)
    self.popover.set_position(Gtk.PositionType.BOTTOM)
    self.popover_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, margin=3, visible=True)
    self.popover.add(self.popover_vbox)
    # Menu Item Features
    self.features_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, visible=True)
    self.features_image = Gtk.Image(icon_name="dialog-information", visible=True)
    self.features_button = Gtk.ModelButton(label="Features", expand=True, xalign=0, visible=True)
    self.features_button.connect("clicked", self.button_features_clicked)
    self.features_hbox.pack_start(self.features_image, False, True, 0)
    self.features_hbox.pack_start(self.features_button, False, True, 0)
    self.popover_vbox.pack_start(self.features_hbox, False, True, 0)
    # Menu Item About
    self.about_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, visible=True)
    self.about_image = Gtk.Image(icon_name="help-about", visible=True)
    self.about_button = Gtk.ModelButton(label="About", expand=True, xalign=0, visible=True)
    self.about_button.connect("clicked", self.button_about_clicked)
    self.about_hbox.pack_start(self.about_image, False, True, 0)
    self.about_hbox.pack_start(self.about_button, False, True, 0)
    self.popover_vbox.pack_start(self.about_hbox, False, True, 0)
    
    # Build Web View
    self.webview = WebKit2.WebView()
    self.window_main.add(self.webview)
    self.webview.load_uri("https://www.duckduckgo.com") # Hardcoded home page. Is it a feature?
    
    # Show window
    self.window_main.show_all()

  # Connected to button_about event
  def button_about_clicked(self, args):
    self.about_window = About()

  # Connected to button_features event
  def button_features_clicked(self, args):
    self.features_window = Features()

# About Dialog
class About:
  def __init__(self):
    self.about_dialog = Gtk.AboutDialog(type_hint="dialog")
    self.about_dialog.set_version("educational version")
    self.about_dialog.set_logo_icon_name(app_icon_name)
    self.about_dialog.set_comments("Zero Features Browser")
    self.about_dialog.set_copyright("© 2021 - Antonio Bianco")
    self.about_dialog.set_website("https://github.com/TonyWhite/zero-features-browser")
    self.about_dialog.set_authors( ("Antonio Bianco",) )
    self.about_dialog.set_artists( ("Antonio Bianco",) )
    self.about_dialog.set_documenters( ("Antonio Bianco",) )
    self.about_dialog.set_translator_credits("Antonio Bianco")
    self.about_dialog.set_license("""DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
Version 2, December 2004

Copyright © 2004 Sam Hocevar
22 rue de Plaisance, 75014 Paris, France
Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING,
DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.""")
    self.about_dialog.connect("response", self.about_dialog_response)
    self.about_dialog.set_modal(True)
    self.about_dialog.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)
    self.about_dialog.show_all()

  def about_dialog_response(self, args, r):
    if r==Gtk.ResponseType.CANCEL or r==Gtk.ResponseType.DELETE_EVENT:
      self.about_dialog.destroy()

# Features Window
class Features:
  def __init__(self):
    self.features_window = Gtk.Window(resizable=False, type_hint="dialog")
    self.features_window.set_modal(True)
    self.features_window.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)
    
    # Build Header Bar
    self.features_header_bar = Gtk.HeaderBar()
    self.features_window.set_titlebar(self.features_header_bar)
    self.features_header_bar.set_title("Zero Features Browser")
    self.features_header_bar.set_show_close_button(True)
    self.features_header_bar.set_decoration_layout("menu:close")
    
    # Window content
    self.features_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, visible=True)
    self.features_window.add(self.features_vbox)
    self.features_label = Gtk.Label(margin=10, visible=True)
    self.features_label.set_markup("""<span weight='bold'>PROS:</span>
- No Chronology
- No Cache
- No Cookie
- No Wayland incompatibility
- No Xorg incompatibility
- Very few dependencies

<span weight='bold'>CONS:</span>
- No address bar
- No tabs
- No optimization

<span weight='bold'>BUGS:</span>
- There is still a feature: it has home page!""")
    self.features_ok_button = Gtk.Button(label="Ok", halign="center", margin=10, expand=False, visible=True)
    self.features_ok_button.connect("clicked", self.features_ok_button_clicked)
    self.features_vbox.pack_start(self.features_label, False, True, 0)
    self.features_vbox.pack_start(Gtk.Separator(), False, True, 0)
    self.features_vbox.pack_start(self.features_ok_button, False, True, 0)
    self.features_window.show_all()

  # Connected to features_ok_button event
  def features_ok_button_clicked(self, args):
    self.features_window.destroy()

if __name__ == "__main__":
  app_title = "br0wser"
  app_icon_name = "applications-internet"
  app = Application()
  Gtk.main()
  exit()
