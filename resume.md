---
layout: default
title: Resume
css_style: "assets/css/resume.css"
class: page
description: This page contains the latest copy of my resume. Feel free to download a copy by clicking the menu button at the bottom.
---


<div class="grid-container">
  <div class="resume-baseinfo">
    <h2 style="color:#8064A7">{{ site.data.resume.name }}</h2>
    <hr style="border-bottom:solid 1px;color:#8064A7">
    {{ site.data.resume.copy }}
  </div>
  <div class="resume-contact">
    {% include nav.html %}
  </div>
  <div class="resume-exp">
    <h2 style="color:#8064A7;text-align:center">Work Experience</h2>
    <hr style="border-bottom:solid 1px;color:#8064A7">
    <div class="job-card">
      {% assign we = site.jobs | sort:"start_date" | reverse %}
      {% for job in we %}
          <div class="citi-header clearfix">
            <img class="logo" src="/images/citi-logo-no-r.png" alt="Citi Logo">
            {{ job.company }} | {{ job.location }} <br>
            {{ job.title }}, {{ job.start_date | date: "%m/%Y" }} to {{ job.end_date | date: "%m/%Y" }}
          </div>
          <p>
            {{ job.content }}
          </p>
    </div>
      {% endfor %}
  </div>
</div>
<script>
    var coll = document.getElementsByClassName("citi-header");
    var i;
    
    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var job-card = this.nextElementSibling;
        if (job-card.style.maxHeight){
          job-card.style.maxHeight = null;
        } else {
          job-card.style.maxHeight = job-card.scrollHeight + "px";
        } 
      });
    }
    </script>