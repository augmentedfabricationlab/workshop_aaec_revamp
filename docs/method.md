---
layout: page
title: Method
---


# revAMp Fabrication Method
The fabrication method for revamping building sites or architectural elements will include an experimental workflow of object scanning, sensory positioning, mobile robot navigation and in situ 3D printing. In this context, a fabrication method will be set up and explored in which damaged parts of an architectural building component are revAMped through an informed in-situ 3D printing process.

### Step 1: 3D Object to be revAMped
In this step, the broken building element is selected and stationed.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-01.jpg" alt="3D Object to be revAMped." style="width:75%" class="center">
  <figcaption>Image: 3D Object to be revAMped.</figcaption>
</figure>

### Step 2: Driving the mobile-robot to the building element
Here, a manual intervention is utilized to drive the mobile-robot near the selected object. The mobile robot will be equipped with an onboard camera-based sensing system to roughly recognize the geometric shape.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-02.jpg" alt="Driving the mobile-robot to the building element." style="width:75%" class="center">
  <figcaption>Image: Driving the mobile-robot to the building element.</figcaption>
</figure>


### Step 3: Real Sense Positioning
This step includes (manually) positioning and rotating the camera sensor in relation to the object to capture a proper field view for data collection.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-03.jpg" alt="Real Sense Positioning." style="width:75%" class="center">
  <figcaption>Image: Real Sense Positioning.</figcaption>
</figure>

### Step 4: Scanning Trajectory
Here, identifying the exact area for refined laser-scanning from the camera image is conducted and overlayed with a zig-zag scanning path.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-04.jpg" alt="Scanning Trajectory." style="width:75%" class="center">
  <figcaption>Image: Scanning Trajectory.</figcaption>
</figure>

### Step 5: Point Cloud Collection and Evaluation
In this step, the point-clouds are collected by moving the scanner along the predefined scanning path. Single scans are registered through transforming each line scan along the robot joints.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-05.jpg" alt="Point Cloud Collection and Evaluation." style="width:75%" class="center">
  <figcaption>Image: Point Cloud Collection and Evaluation.</figcaption>
</figure>

### Step 6: Surface Re-construction
For further path-planning a closed surface is reconstructed based on the registered point-cloud. Compensation of scanning errors is performed by ~80% subsampling of the initial data sets.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-06.jpg" alt="Surface Re-construction." style="width:75%" class="center">
  <figcaption>Image: Surface Re-construction.</figcaption>
</figure>

### Step 7: Printing Region Identifying
The reconstructed surface is utilized to trim the to-be-printed geometry.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-07.jpg" alt="Printing Region Identifying." style="width:75%" class="center">
  <figcaption>Image: Printing Region Identifying.</figcaption>
</figure>

### Step 8: Printing Path Design Generation
Here, the identified printing regieon is designed.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-08.jpg" alt="Printing Path Design Generation." style="width:75%" class="center">
  <figcaption>Image: Printing Path Design Generation.</figcaption>
</figure>

### Step 9: Path Print Simulation
The printing path is simulated visually and it’s executed from the generated revAMp design.
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-09.jpg" alt="Path Print Simulation." style="width:75%" class="center">
  <figcaption>Image: Path Print Simulation.</figcaption>
</figure>

### Step 10: Extrusion 3D Printing
In this step, the mobile-robot will be equipped with an extrusion end-effector for the 3D Printing Process. The extrusion 3D Printing Process with clay has been developed in previous research projects and its controlled parameter such as (speed, distance from the surface, start and stop function,…) will be implemented. 
<figure>
  <img src="{{site.baseurl}}images/WorkFlow-10.jpg" alt="Extrusion 3D Printing." style="width:75%" class="center">
  <figcaption>Image: Extrusion 3D Printing.</figcaption>
</figure>


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