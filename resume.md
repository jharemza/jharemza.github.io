---
layout: default
title: Resume
css_style: "assets/css/resume.css"
class: page
description: This page contains the latest copy of my resume. Feel free to download a copy by clicking the menu button at the bottom.
---
<body>
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
            <div class="citi-header">
              <img class="logo" src="/images/citi-logo-no-r.png" alt="Citi Logo">
              {% for job in site.jobs %}
              {% capture date %}{{ job.start_date | date: '%F' }}{% endcapture %}
              {% if date == "2019-12-01" %}
              {{ job.company }} | {{ job.start_date }} |
              {% endif %}
              {% endfor %}
            </div>
        </div>
      </div>
</body>
