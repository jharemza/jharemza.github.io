---
layout: default
class: page
title: Blog Index
---

Below is the list of posts for my blog entitled Euler's Good Eye.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.date | date: "%m/%d/%Y" }} | {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>