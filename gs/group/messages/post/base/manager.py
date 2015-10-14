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
from __future__ import absolute_import, unicode_literals, print_function
from gs.viewlet.manager import WeightOrderedViewletManager


class PostBodyViewletManager(WeightOrderedViewletManager):
    '''The viewlet manager for the body of a post'''
    def __init__(self, context, request, view):
        super(PostBodyViewletManager, self).__init__(context, request, view)


class PostActionsViewletManager(WeightOrderedViewletManager):
    '''The viewlet manager for the actions that can be carried out on a post'''
    def __init__(self, context, request, view):
        super(PostActionsViewletManager, self).__init__(context, request, view)
