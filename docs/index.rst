==================================
:mod:`gs.group.messages.post.base`
==================================

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-09-30
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

  ..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Contents:

.. toctree::
   :maxdepth: 1

   requirements
   post
   markup
   structure
   HISTORY

The :mod:`gs.group.messages.post.base` product provides the code
for displaying posts that have been made to a group, which as
some strict :ref:`requirements <requirements>`. It provides the
``groupserver.Post`` *content provider* that creates :ref:`the
post <post>` with some :ref:`microformats <microformats>`. This
product does not, however, provide the body of the post. This is
provided by other products that work with the :ref:`structure
<structure>` provided by this product.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.messages.post.base/
- Translations:
  https://www.transifex.com/groupserver/gs-group-messages-post/
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
