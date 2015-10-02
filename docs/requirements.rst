.. _requirements:

Design requirements
===================

#. The rendering of a post needs to be **fast.** Posts are the
   core GroupServer, and are used very heavily.

#. The system to display posts needs to be **flexible.** People
   can add posts containing any old thing, such as HTML, and
   plain text.

#. A post may be shown in a number of different **contexts:**

   * On the *Topic* page
   * On the *Post* page
   * On the (rarely visited) *Posts* page

#. The system needs to handle **actions**. While the normal thing
   to do with a post is to read it, people also hide and share
   posts.

   * **Hiding** posts needs to be restricted to just the
     administrator and the author.

   * **Sharing** should be restricted so people are discouraged
     from sharing links from private groups with the wider
     public.

