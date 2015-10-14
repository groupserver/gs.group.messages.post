# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
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
from gs.group.base import GroupViewlet
from gs.group.messages.base import get_icon


class PostViewlet(GroupViewlet):
    def __init__(self, context, request, view, manager):
        super(PostViewlet, self).__init__(context, request, view, manager)

    def update(self):
        super(PostViewlet, self).update()
        self.post = self.manager.post
        self.position = self.manager.position
        self.topicName = self.manager.topicName
        self.showPhoto = self.manager.showPhoto
        self.isPublic = self.manager.isPublic
        self.showRemainder = self.manager.showRemainder
        self.mediaFiles, self.normalFiles = self.get_files(self.post, self.groupInfo)
        self.authored = self.user_authored()
        self.authorInfo = createObject('groupserver.UserFromId',
                                       self.context,
                                       self.post['author_id'])

    #########################################
    # Non-standard methods below this point #
    #########################################

    @staticmethod
    def get_files(post, groupInfo):
        mediaFiles = []
        normalFiles = []
        for fm in post['files_metadata']:
            fm['icon'] = get_icon(fm['mime_type'])
            size = '{0:.1f}kb'.format(fm['file_size'] / 1024.0)  # FIXME: Better version somewhere?
            fm['size'] = size
            # TODO: Extend to audio <https://redmine.iopen.net/issues/416>
            # TODO: Extend to video <https://redmine.iopen.net/issues/333>
            if fm['mime_type'][:5] == 'image':
                url = '{0}/messages/image/{1}'
                fm['url'] = url.format(groupInfo.relativeURL, fm['file_id'])
                s = '{0}/files/f/{1}/{2}'
                fm['src'] = s.format(groupInfo.relativeURL, fm['file_id'], fm['file_name'])
                mediaFiles.append(fm)
            else:
                url = '{0}/files/f/{1}/{2}'
                fm['url'] = url.format(groupInfo.relativeURL, fm['file_id'], fm['file_name'])
                normalFiles.append(fm)
        assert type(mediaFiles) == list
        assert type(normalFiles) == list
        return (mediaFiles, normalFiles)

    def user_authored(self):
        retval = False
        if not(self.loggedInUser.anonymous):
            retval = self.loggedInUser.id == self.post['author_id']
        assert type(retval) == bool
        return retval
