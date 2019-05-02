---
layout: default
class: page
title: Blog Index
description: This page is the complete list of all of the blog posts on Euler's Good Eye in chronological order.
---

Below is the list of posts for my blog entitled Euler's Good Eye.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.date | date: "%m/%d/%Y" }} | {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>