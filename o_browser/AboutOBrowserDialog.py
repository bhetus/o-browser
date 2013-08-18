# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('o-browser')

import logging
logger = logging.getLogger('o_browser')

from o_browser_lib.AboutDialog import AboutDialog

# See o_browser_lib.AboutDialog.py for more details about how this class works.
class AboutOBrowserDialog(AboutDialog):
    __gtype_name__ = "AboutOBrowserDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutOBrowserDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

