.. _post:

The post content provider
=========================

.. currentmodule:: gs.group.messages.post.base.interfaces

The post `content provider`_ provides an interface_, which is
used by the XML_ that generates the page.

Interface
---------

The post `content provider`_ implements the interface
:class:`IPost`.

.. class:: IPost

   .. attribute:: post

      The email message instance that is being displayed.

   .. attribute:: position

      The position of the post in the list of posts, as an
      integer (``int``) above ``0`` (a cardinal value). The
      position may be the position in the topic, or in the list
      of posts. Defaults to ``1``.

   .. attribute:: topicName

      The name of the topic that the post appears in, as a
      Unicode sequence (``str`` in Python 3, ``unicode`` in
      Python 2). While the post could figure this out, it is
      faster to have this information provided (see
      :ref:`requirements`).

   .. attribute:: showPhoto

      Whether the photo of the author should be shown, as a
      Boolean (``bool``, defaulting to ``True``). On both the
      *Topic* and *Post* page sequential posts by the same author
      have the profile photo dropped.

   .. attribute:: isPublic

      Whether the post is public, as a Boolean (``bool``). While
      the post could figure this out, it is faster to have this
      information provided (see :ref:`requirements`).

   .. attribute:: showRemainder

      Whether to show the snipped bottom-quoting and signature on
      the post, as a Boolean (``bool``, defaulting to ``False``).

XML
---

The XML that uses the content provider is in two parts. First,
the parameters are set up by the TAL of the calling code, using
the ``tal:define`` attribute. Second the content provider is
called using the ``provider`` call. For example, the code used by
the *Topic* page looks similar to the following.

.. code-block:: xml
   :linenos:
   :emphasize-lines: 2,3,6,10,11

   <tal:block
     define="topicName view/topicName;
             isPublic view/isPublic;">
     <tal:block repeat="post view/topic">
       <tal:block 
         define="position repeat/post/number;
                 currAuth python:view.topic[position-1]['author_id'];
                 prevAuth python:view.topic[position-2]['author_id'];
                 rptAuth python: currAuth == prevAuth;
                 showPhoto python:(position==1) or not(rptAuth);"
         replace="structure provider:groupserver.Post">
         This is replaced by the body of the post
       </tal:block>
     </tal:block>
   </tal:block>

Initially, the :attr:`IPost.topicName` and :attr:`IPost.isPublic`
attributes are set up (lines 2–3). The the topic iterates across
all the posts in the topic, setting the :attr:`IPost.position`
accordingly (line 6). The :attr:`IPost.showPhoto` is calculated
(line 10), while the :attr:`IPost.showRemainder` is left as its
default (``False``). Finally, the content provider is called
using ``structure provider:groupserver.Post``, replacing the
content of the ``<tal:block>`` element (line 11).

.. _content provider:
   https://pypi.python.org/pypi/zope.contentprovider
