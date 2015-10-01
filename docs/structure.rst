.. _structure: 

The structure of a post
=======================

.. currentmodule:: gs.group.messages.post.base

The structure of a post in GroupServer may seem simple, but that
is just good user-interface design. It is actually quite
complex. In this document I will discuss the structure of the
viewlets that are used to create the post.

The post itself is a `content provider`_, which provides the
interface :class:`.interfaces.IPost`. It is a provider so it can
be called from many different contexts.

The content provider generates the **metadata** for the post,
including the profile photo of the author, their name, and the
date the post was made. (This metadata conforms to some
:ref:`microformats <microformats>`) The rest of the post is
displayed using two *viewlet managers*.

.. code-block:: none

    ┌─Post─────────────────────────────────────────────────┐
    │                                                      │
    │ ┌─Metadata─────────────────────────────────────────┐ │
    │ │ Information about the person who made the post   │ │
    │ └──────────────────────────────────────────────────┘ │
    │                                                      │
    │ ┌─Actions viewlet manager──────────────────────────┐ │
    │ │ gs.group.messages.post.base.interfaces.IActions  │ │
    │ └──────────────────────────────────────────────────┘ │
    │                                                      │
    │ ┌─Post body viewlet manager────────────────────────┐ │
    │ │ gs.group.messages.post.base.interfaces.IPostBody │ │
    │ └──────────────────────────────────────────────────┘ │
    │                                                      │
    └──────────────────────────────────────────────────────┘

Metadata:
  The metadata for the post is provided by the content provider.

Actions:
  The actions viewlet manager shows the actions the viewer can
  carry out.

Post body:
  The post itself is provided by a viewlet that slots into the
  post viewlet manager. Views of the post provide state that they
  are ``for`` the :class:`.interfaces.IPostBody` viewlet manager.

As a consequence of this design, the actual body of the post is
provided by other products. Hidden posts are handled by the
`gs.group.messages.post.hide`_ product, which also controls if
the *Hide* button appears in the actions; plain-text posts
(:mimetype:`text/plain`) are rendered by the
`gs.group.messages.post.text`_ product.

.. _content provider:
   https://pypi.python.org/pypi/zope.contentprovider
.. _gs.group.messages.post.hide:
   https://github.com/groupserver/gs.group.messages.post.hide/
.. _gs.group.messages.post.text:
   https://github.com/groupserver/gs.group.messages.post.text/

..  LocalWords:  Viewlets
