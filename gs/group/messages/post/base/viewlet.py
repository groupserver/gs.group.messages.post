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
from gs.group.base import GroupViewlet


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
