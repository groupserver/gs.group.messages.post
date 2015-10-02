# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2013, 2014, 2015 OnlineGroups.net and Contributors.
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
from zope.interface import Interface
from zope.schema import TextLine, Field, Int, Bool
from zope.viewlet.interfaces import IViewletManager


class IGSPostContentProvider(Interface):
    """The Groupserver Post Content Provider Interface

      This interface defines the fields that must be set up, normally using
      TAL, before creating a "GSPostContentProvider" instance. See the
      latter for an example."""
    post = Field(
        title="Email Message Instance",
        description="The email instance to display",
        required=True,
        readonly=False)

    position = Int(
        title="Position of the Post",
        description="""The position of the post in the topic.
        This is mostly used for determining the background
        colour of the post.""",
        required=False,
        min=1, default=1)

    topicName = TextLine(
        title="Title of the Topic",
        description="""The title of the topic.""",
        required=True,
        default='')

    # Should really be called "same author" or similar.
    showPhoto = Bool(
        title='Whether to show the photo',
        description="""Determines if the author's photo
        should be shown.""",
        required=False,
        default=True)

    isPublic = Bool(
        title="Is the group public?",
        description="""Whether or not the group in which this post is
          displayed is public""",
        required=True)

    showRemainder = Bool(
        title='Show the remainder',
        description='True if the bottom-quoting should be shown',
        required=False,
        default=False)


class IPostMetadataContentProvider(IGSPostContentProvider):
    '''The content provider for the post metadata'''


class IPost(IViewletManager):
    '''The viewlet manager for the post.

Viewlets that wish to provide content for the post should state that their
**manager** is this interface:

.. code-block:: xml
   :linenos:
   :emphasize-lines: 3

   <browser:viewlet
     name="gs-group-messages-post-base-metadata"
     manager="gs.group.messages.post.base.interfaces.IPost"
     class=".metadata.PostMetadataViewlet"
     template="browser/templates/metadata.pt"
     permission="zope2.View"
     weight="10"
     title="Metadata" />'''


class IActions(IViewletManager):
    '''The viewlet manager for the post actions.

Viewlets that wish to provide actions for the post should state that their
**manager** is this interface:

.. code-block:: xml
   :linenos:
   :emphasize-lines: 3

   <browser:viewlet
     name="gs-group-messages-post-hide-button"
     manager="gs.group.messages.post.base.interfaces.IActions"
     class=".button.HideButton"
     template="browser/templates/button.pt"
     permission="zope2.View"
     weight="90"
     title="Hide" />'''

class IBody(IViewletManager):
    '''The viewlet manager for the post body.

Viewlets that wish to provide views for the post body should state that
their **manager** is this interface:

.. code-block:: xml
   :linenos:
   :emphasize-lines: 3

   <browser:viewlet
     name="gs-group-messages-post-text"
     manager="gs.group.messages.post.base.interfaces.IBody"
     class=".body.PlainTextBody"
     template="browser/templates/body.pt"
     permission="zope2.View"
     weight="10"
     title="Text" />'''
