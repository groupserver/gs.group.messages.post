# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, division, unicode_literals, print_function
from threading import RLock
from zope.cachedescriptors.property import Lazy
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.app.pagetemplate import ViewPageTemplateFile
from gs.viewlet.manager import WeightOrderedViewletManager


class PostViewletManager(WeightOrderedViewletManager):
    __thread_lock = RLock()
    cookedTemplates = {}

    def cook_template(self, fname):
        if fname in self.cookedTemplates:
            return self.cookedTemplates[fname]

        cooked = ViewPageTemplateFile(fname)
        try:
            # don't block, we'll just cache it later
            if self.__thread_lock.acquire(False):
                self.cookedTemplates[fname] = cooked
        finally:
            self.__thread_lock.release()

        return cooked

    def notRender(self):
        if not self.__updated:
            raise UpdateNotCalled
        pageTemplate = self.cook_template(self.pageTemplateFileName)
        self.request.debug = False
        r = pageTemplate(self)
        return r

    #########################################
    # Non-standard methods below this point #
    #########################################

    @Lazy
    def cssClass(self):
        if not hasattr(self, 'position'):
            raise AttributeError('The self.position is unset')
        retval = 'even' if ((self.position % 2) == 0) else 'odd'
        retval += ' post-hidden' if self.post['hidden'] else ' post-visible'
        return retval
