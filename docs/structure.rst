The structure of a post
=======================

.. currentmodule:: gs.group.messages.post.base

The structure of a post in GroupServer may seem simple, but that
is just good user-interface design. It is actually quite
complex. In this document I will discuss the `design
requirements`_ of a post, and the structure of the viewlets_ that
are used to create the post.

.. _requirements:

Design requirements
-------------------

#. The rendering of a post needs to be **fast.** The *Topic* page
   is the workhorse page of GroupServer, and it uses posts very
   heavily.

#. The system to display posts needs to be **flexible.** People
   can add posts containing any old thing, and the system needs
   to be able to handle that. In addition a post may be shown in
   a number of different contexts:

   * On the *Topic* page
   * On the *Post* page
   * One the (rarely visited) *Posts* page

#. The system needs to handle **actions**. While the normal thing
   to do with a post is to read it, people also hide and share
   posts.

   * **Hiding** posts needs to be restricted to just the
     administrator and the author.

   * **Sharing** should be restricted so people are discouraged
     from sharing links from private groups with the wider
     public.

Viewlets
--------

The post itself is a `content provider`_, which provides the
interface :class:`.interfaces.IPost`. It is a provider so it can
be called from many different contexts (see *Flexible* above).

The content provider shows the **metadata** for the post,
including the profile photo of the author, their name, and the
date the post was made. The rest of the post is displayed using
two *viewlet managers*.

.. code-block:: none

    ┌─Post────────────────────────────────────────────────┐
    │                                                     │
    │ ┌─Metadata────────────────────────────────────────┐ │
    │ │ Information about the person who made           │ │
    │ │ the post                                        │ │
    │ └─────────────────────────────────────────────────┘ │
    │                                                     │
    │ ┌─Actions viewlet manager─────────────────────────┐ │
    │ │ gs.group.messages.post.base.interfaces.IActions │ │
    │ └─────────────────────────────────────────────────┘ │
    │                                                     │
    │ ┌─Post viewlet manager────────────────────────────┐ │
    │ │ gs.group.messages.post.base.interfaces.IPost    │ │
    │ └─────────────────────────────────────────────────┘ │
    │                                                     │
    └─────────────────────────────────────────────────────┘


Actions:
  The actions viewlet manager shows the actions the viewer can
  carry out.

Post:
  The post itself is provided by a viewlet that slots into the
  post viewlet manager.

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
