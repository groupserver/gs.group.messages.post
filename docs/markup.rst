.. _microformats:

Microformats used in the post
=============================

A post uses the following microformats, which can be used to
analyse a post.

* Each post given the ``article`` role [#article]_.
* The topic-title is marked with the ``entry-title`` class, and
  given a ``heading`` role [#heading]_. Note that it may be
  hidden by the CSS for the page.
* The author metadata is given the ``h-card`` and ``author``
  classes, with the name marked with the ``p-name`` class [#h-card]_.
* The post-date in in a ``<time>`` element, with the ``datetime``
  attribute [#time]_ set to the date the post was made in
  UTC. The surrounding element is given the classes ``date``,
  ``updated``, and ``published`` classes.


.. [#article] For more on the ``article`` role see
              <http://www.w3.org/TR/wai-aria/roles#article>

.. [#heading] For more on the ``heading`` role see
              <http://www.w3.org/TR/wai-aria/roles#heading>

.. [#h-card] See the Microformats wiki for more on ``h-card``
             <http://microformats.org/wiki/h-card>

.. [#time] For more on the HTML5 Time element see
           <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time>
