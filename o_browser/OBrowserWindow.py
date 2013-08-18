# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
import os
from gettext import gettext as _
gettext.textdomain('o-browser')

from gi.repository import Gtk,WebKit # pylint: disable=E0611
import logging
logger = logging.getLogger('o_browser')

from o_browser_lib import Window
from o_browser.AboutOBrowserDialog import AboutOBrowserDialog
from o_browser.PreferencesOBrowserDialog import PreferencesOBrowserDialog

# See o_browser_lib.Window.py for more details about how this class works
class OBrowserWindow(Window):
    __gtype_name__ = "OBrowserWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(OBrowserWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutOBrowserDialog
        self.PreferencesDialog = PreferencesOBrowserDialog

        # Code for other initialization actions should be added here.

        self.refreshbutton = self.builder.get_object('refreshbutton')
        self.backbutton = self.builder.get_object('backbutton')
        self.forwardbutton = self.builder.get_object('forwardbutton')
        self.urlentry = self.builder.get_object('urlentry')
        self.scrolledwindow = self.builder.get_object('scrolledwindow')
        self.toolbar = self.builder.get_object('toolbar')
        self.firefox = self.builder.get_object('firefox')

        context = self.toolbar.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)


        self.webview = WebKit.WebView()

        self.scrolledwindow.add(self.webview)
        self.webview.show()
        
    def on_refreshbutton_clicked(self,widget):
        self.webview.reload()

    def on_backbutton_clicked(self,widget):
        print "back"
    
    def on_forwardbutton_clicked(self,widget):
        print "forward"

    def on_urlentry_activate(self,widget):
        url = widget.get_text()              
        self.webview.open(url)

    def on_firefox_clicked(self,widget):
        os.system("firefox")
        
    
    def on_scrolledwindow_clicked(self,widget):
        print  "scrolled"


