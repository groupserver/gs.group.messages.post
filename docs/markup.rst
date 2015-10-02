.. _microformats:

Microformats used in the post
=============================

A post uses the following microformats, which can be used to
analyse a post.

* Each post is an ``<article>`` element [#article]_, and it
  conforms to the ``h-entry`` microformat [#h-entry]_

* The topic-title is marked with the ``p-name`` class, and given
  a ``heading`` role [#heading]_. Note that the heading may be
  hidden by the CSS for the page.

  + The ``<article>`` and heading are linked by the
    ``aria-labelledby`` attribute on the ``<article>`` [#label]_.

  + The ``u-url`` (also on the heading) marks the URL of the
    *permalink* for the post.

* The author metadata is given in an ``<address>`` element
  [#address]_, with the ``h-card`` and ``p-author`` classes; the
  name marked with the ``p-name`` class [#h-card]_.

* The post-date in in a ``<time>`` element, with the ``datetime``
  attribute [#time]_ set to the date the post was made in
  UTC. The ``<time>`` element is also given the class
  ``dt-published``.

.. [#article] For more on the ``<article>`` element see
   <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article>

.. [#h-entry] See the Microformats wiki for more on ``h-entry``
              <http://microformats.org/wiki/h-entry>

.. [#heading] For more on the ``heading`` role see
              <http://www.w3.org/TR/wai-aria/roles#heading>

.. [#label] For more on the WAI-ARIA ``aria-labelledby``
            attribute see
            <https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques/Using_the_aria-labelledby_attribute>

.. [#address] For more on the ``<address>`` element see
           <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address>

.. [#h-card] See the Microformats wiki for more on ``h-card``
             <http://microformats.org/wiki/h-card>

.. [#time] For more on the HTML5 Time element see
           <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time>
