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
from __future__ import absolute_import, unicode_literals
from mock import MagicMock
from unittest import TestCase
from gs.group.messages.post.base.viewlet import (PostViewlet)


class TestPostViewlet(TestCase):

    def setUp(self):
        self.viewlet = PostViewlet(MagicMock(), MagicMock(), MagicMock(), MagicMock())
        self.groupInfo = MagicMock()
        self.groupInfo.relativeURL = '/groups/test'

    @staticmethod
    def create_file(mime, size, fileId, name):
        retval = {
            'mime_type': mime,
            'file_size': size,
            'file_id': fileId,
            'file_name': name, }
        return retval

    def test_get_files_none(self):
        'Test when there are no files'
        post = {'files_metadata': []}
        r = self.viewlet.get_files(post, self.groupInfo)

        self.assertEqual(2, len(r))
        self.assertEqual([], r[0])
        self.assertEqual([], r[1])

    def test_get_files_img(self):
        'Test when there is an image'
        post = {'files_metadata': [self.create_file('image/jpeg', 1234, 'anId', 'photo.jpg')]}
        r = self.viewlet.get_files(post, self.groupInfo)

        self.assertEqual(1, len(r[0]))
        self.assertEqual(1, len(r.media))
        i = r[0][0]
        self.assertIn('icon', i)
        self.assertIn('src', i)
        self.assertIn('url', i)
        self.assertIn('size', i)
        self.assertEqual([], r[1])

    def test_get_files_images(self):
        'Test when there are images'
        i1 = self.create_file('image/jpeg', 1234, 'anId0', 'photo-0.jpg')
        i2 = self.create_file('image/png', 4321, 'anId1', 'photo-1.png')
        post = {'files_metadata': [i1, i2]}
        r = self.viewlet.get_files(post, self.groupInfo)

        self.assertEqual(2, len(r[0]))
        self.assertEqual(2, len(r.media))
        self.assertEqual([], r[1])

    def test_get_files_non_img(self):
        'Test when there is a non-image file'
        post = {'files_metadata': [self.create_file('application/octet-stream', 1234, 'anId',
                                                    'a.file')]}
        r = self.viewlet.get_files(post, self.groupInfo)

        self.assertEqual([], r[0])
        self.assertEqual(1, len(r[1]))
        self.assertEqual(1, len(r.normal))
        i = r[1][0]
        self.assertIn('icon', i)
        self.assertNotIn('src', i)
        self.assertIn('url', i)
        self.assertIn('size', i)

    def test_get_files_both(self):
        'Test when there are both types of file'
        img = self.create_file('image/jpeg', 1234, 'anId', 'photo.jpg')
        other = self.create_file('application/octet-stream', 1234, 'anId', 'a.file')
        post = {'files_metadata': [img, other]}
        r = self.viewlet.get_files(post, self.groupInfo)

        self.assertEqual(1, len(r[0]))
        self.assertEqual(1, len(r[1]))
        self.assertNotEqual(r[0][0], r[1][0])
        self.assertEqual('image', r[0][0]['mime_type'][:5])
