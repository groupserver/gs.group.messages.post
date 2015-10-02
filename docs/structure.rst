.. _structure:

The structure of a post
=======================

.. currentmodule:: gs.group.messages.post.base

The structure of a post in GroupServer may seem simple, but that
is just good user-interface design. It is actually quite
complex. In this document I will discuss the structure of the
viewlets that are used to create the post.

The post itself provides two interfaces. 

* To *external* code it looks like a `content provider`_ that
  provides the interface
  :class:`.interfaces.IPostContentProvider` interface.
* To the *internal* code that provide the content of the post it
  is a *viewlet manager* that provides the
  :class:`.interfaces.IPost` interface.

Three viewlets provided by this product use the post viewlet
manager, two of which contain viewlet managers themselves.

.. code-block:: none

    ┌─Post viewlet manager─────────────────────────────────────┐
    │ gs.group.messages.post.base.interfaces.IPost             │
    │                                                          │
    │ ┌─Metadata viewlet─────────────────────────────────────┐ │
    │ │ gs-group-messages-post-base-metadata                 │ │
    │ └──────────────────────────────────────────────────────┘ │
    │                                                          │
    │ ┌─Actions viewlet──────────────────────────────────────┐ │
    │ │ gs-group-messages-post-base-actions                  │ │
    │ │                                                      │ │
    │ │ ┌─Actions viewlet manager──────────────────────────┐ │ │
    │ │ │ gs.group.messages.post.base.interfaces.IActions  │ │ │
    │ │ └──────────────────────────────────────────────────┘ │ │
    │ │                                                      │ │
    │ └──────────────────────────────────────────────────────┘ │
    │                                                          │
    │ ┌─Body viewlet─────────────────────────────────────────┐ │
    │ │ gs-group-messages-post-base-body                     │ │
    │ │                                                      │ │
    │ │ ┌─Post body viewlet manager────────────────────────┐ │ │
    │ │ │ gs.group.messages.post.base.interfaces.IBody     │ │ │
    │ │ └──────────────────────────────────────────────────┘ │ │
    │ │                                                      │ │
    │ └──────────────────────────────────────────────────────┘ │
    │                                                          │
    └──────────────────────────────────────────────────────────┘

Post:
  The overall container that holds the post is a *viewlet
  manager*, which provides the :class:`.interfaces.IPost`
  interface.

Metadata:
  The metadata for the post is provided by a *viewlet* defined by
  this product The metadata includes the profile photo of the
  author, their name, and the date the post was made. (This
  metadata conforms to some :ref:`microformats. <microformats>`)

Actions:
  The controls the viewer can see (and thereby use) are shown by
  the Actions. It is split in two: a *viewlet* for the post,
  which then contains a *viewlet manger* for the content, which
  provides the class :class:`.interfaces.IActions`.

Post body:
  The body is provided by a viewlet that slots into the post
  viewlet manager. Views of the post provide state that they are
  managed by the :class:`.interfaces.IBody` viewlet manager.

As a consequence of this design, the actual body of the post is
provided by other products. Hidden posts are handled by the
`gs.group.messages.post.hide`_ product, which also controls if
the *Hide* button appears in the actions; plain-text posts
(:mimetype:`text/plain`) are rendered by the
`gs.group.messages.post.text`_ product.

Interfaces
----------

Three interfaces are used within the post:
:class:`.interfaces.IPost` for the overall layout,
:class:`.interfaces.IActions` for the actions, and
:class:`.interfaces.IBody` for the actual body.

.. autoclass:: gs.group.messages.post.base.interfaces.IPost
   :members:

.. autoclass:: gs.group.messages.post.base.interfaces.IActions
   :members:

.. autoclass:: gs.group.messages.post.base.interfaces.IBody
   :members:

.. _content provider:
   https://pypi.python.org/pypi/zope.contentprovider
.. _gs.group.messages.post.hide:
   https://github.com/groupserver/gs.group.messages.post.hide/
.. _gs.group.messages.post.text:
   https://github.com/groupserver/gs.group.messages.post.text/

..  LocalWords:  Viewlets
