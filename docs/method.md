---
layout: page
title: Method
---


# revAMp Fabrication Method
## The fabrication method for revamping building sites or architectural elements will include an experimental workflow of object scanning, sensory positioning, mobile robot navigation and in situ 3D printing. In this context, a fabrication method will be set up and explored in which damaged parts of an architectural building component are revAMped through an informed in-situ 3D printing process.

<figure>
  <img src="{{site.baseurl}}images/WorkFlow-01.jpg" alt="3D Object to be revAMped." style="width:75%" class="center">
  <figcaption>Image: 3D Object to be revAMped.</figcaption>
</figure>

## In this step, the broken building element is selected and stationed.

<div class="posts">
  {% for post in site.posts %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{site.baseurl}}{{ post.url }}">
        {{ post.title }}
      </a>
    </h1>

    <span class="post-date">{{ post.date | date_to_string }}</span>

    {{ post.content }}
  </div>
  {% endfor %}
</div>

<div class="pagination">
  {% if site.next_page %}
    <a class="pagination-item older" href="{{ site.baseurl }}page{{paginator.next_page}}">Older</a>
  {% else %}
    <span class="pagination-item older">Older</span>
  {% endif %}
  {% if site.previous_page %}
    {% if site.page == 2 %}
      <a class="pagination-item newer" href="{{ site.baseurl }}">Newer</a>
    {% else %}
      <a class="pagination-item newer" href="{{ site.baseurl }}page{{paginator.previous_page}}">Newer</a>
    {% endif %}
  {% else %}
    <span class="pagination-item newer">Newer</span>
  {% endif %}
</div>