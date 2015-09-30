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
from gs.group.base.contentprovider import GroupContentProvider


class GSPostContentProvider(GroupContentProvider):
    post = None
    __thread_lock = RLock()
    cookedTemplates = {}

    def __init__(self, context, request, view):
        super(GSPostContentProvider, self).__init__(context, request, view)
        self.__updated = False

    def update(self):
        """Update the internal state of the post content-provider.

        This method can be considered the main "setter" for the
        content provider; for the most part, information about the post's
        author is set.

        SIDE EFFECTS
          The following attributes are set.
            * "self.__updated"     Set to "True".
            * "self.authorId"      Set to the user-id of the post author.
            * "self.authorName"    Set to the name of the post author.
            * "self.authorExists"  Set to "True" if the author exists.
            * "self.authored"      Set to "True" if the current user
                                   authored the post.
            * "self.authorImage"   Set to the URL of the author's image.
            * "self.siteInfo"     Set to an instance of GSSiteInfo.
            * "self.groupInfo"    Set to an instance of GSGroupInfo.
            * "self.post"         Set to the content of the post.
        """
        if not(self.post):
            raise ValueError('The self.post is missing')
        # See the interface for what is passed in.
        self.__updated = True

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

    def render(self):
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
            raise ValueError('The self.position is unset')
        retval = 'even' if ((self.position % 2) == 0) else 'odd'
        retval += ' post-hidden' if self.post['hidden'] else ' post-visible'
        return retval
