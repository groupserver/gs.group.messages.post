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
from collections import namedtuple
from math import pow, floor, log
from zope.component import createObject
from gs.group.base import GroupViewlet
from gs.group.messages.base import get_icon


FilesRetval = namedtuple('FilesRetval', ['media', 'normal'])


class PostViewlet(GroupViewlet):
    IMAGE_URI = '{0}/messages/image/{1}'
    SOURCE_URI = '{0}/files/f/{1}/{2}'

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
    def file_size_format(bytes):
        """Returns a humanized string for a given amount of bytes"""
        # http://python.todaysummary.com/q_python_11123.html
        bytes = int(bytes)
        if bytes is 0:
            retval = 'empty'
        else:
            l = floor(log(bytes, 1024))
            size = bytes / pow(1024, l)
            unit = [' bytes', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'][int(l)]
            sf = 2 if l > 0 else 0
            retval = '{size:.{sf}f}{unit}'.format(size=size, sf=sf, unit=unit)
        return retval

    def get_files(self, post, groupInfo):
        mediaFiles = []
        normalFiles = []
        for fm in post['files_metadata']:
            fm['icon'] = get_icon(fm['mime_type'])
            fm['size'] = self.file_size_format(fm['file_size'] / 1024.0)
            # TODO: Extend to audio <https://redmine.iopen.net/issues/416>
            # TODO: Extend to video <https://redmine.iopen.net/issues/333>
            if fm['mime_type'][:5] == 'image':
                fm['url'] = self.IMAGE_URI.format(groupInfo.relativeURL, fm['file_id'])
                fm['src'] = self.SOURCE_URI.format(groupInfo.relativeURL, fm['file_id'],
                                                   fm['file_name'])
                mediaFiles.append(fm)
            else:
                fm['url'] = self.SOURCE_URI.format(groupInfo.relativeURL, fm['file_id'],
                                                   fm['file_name'])
                normalFiles.append(fm)
        assert type(mediaFiles) == list
        assert type(normalFiles) == list
        retval = FilesRetval(mediaFiles, normalFiles)
        return retval

    def user_authored(self):
        retval = False
        if not(self.loggedInUser.anonymous):
            retval = self.loggedInUser.id == self.post['author_id']
        assert type(retval) == bool
        return retval
