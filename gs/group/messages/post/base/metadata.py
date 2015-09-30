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
from zope.component import createObject
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.app.pagetemplate import ViewPageTemplateFile
from gs.group.base.contentprovider import GroupContentProvider


class PostMetadataContentProvider(GroupContentProvider):
    post = None

    def __init__(self, context, request, view):
        super(PostMetadataContentProvider, self).__init__(context, request, view)
        self.updated = False
        # allow baseclass override

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
        assert self.post
        # See the interface for what is passed in.
        self.updated = True

        self.showPhoto = self.showPhoto

        self.authored = self.user_authored()
        self.authorInfo = createObject('groupserver.UserFromId',
                                       self.context,
                                       self.post['author_id'])
        self.pageTemplate = ViewPageTemplateFile(self.pageTemplateFileName)

    def render(self):
        if not self.updated:
            raise UpdateNotCalled()
        return self.pageTemplate(self)

    #########################################
    # Non-standard methods below this point #
    #########################################

    def user_authored(self):
        retval = False
        if not(self.loggedInUser.anonymous):
            retval = self.loggedInUser.id == self.post['author_id']
        assert type(retval) == bool
        return retval
