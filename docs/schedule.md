---
layout: default
title: Schedule
permalink: /schedule/
---

In the first part of the class, we will cover postulates and analytical models. Next, we will cover approximation schemes and the principles behind computational chemistry. The last part of the class will emphasize practical molecular modeling exercises and require a capstone project.

There will be 26 class sessions over 15 weeks. Our tentative schedule is below. This class is being significantly revised since I last taught it in 2015, so the schedule is likely to be adjusted. There will be no class during the first week. On 11/25, we will have two class sessions, one during lunch. It will be recorded for those unable to attend.

Lecture slides and exercise notebooks should be available below after the class period. If they are not, please let me know.

| ---- | | |
{% for module in site.data.modules -%} |
{%- if module.day %}{{ module.day }}{% endif %} |
{%- if module.date %}{{ module.date }}{% endif %} | <b>{{ module.title }}</b>
{%- if module.description %} {{ module.description }} {% endif -%}
{%- if module.teacher %} ({{ module.teacher }}){% endif -%}
{%- if module.basename %} [[key](https://github.com/daveminh/Chem550-2024F/raw/main/slides/{{ module.basename }}.key)/[ppt](https://github.com/daveminh/Chem550-2024F/raw/main/slides/{{ module.basename }}.pptx)/[pdf](https://github.com/daveminh/Chem550-2024F/raw/main/slides/{{ module.basename }}.pdf)]. {% endif %}
{%- if module.exercise %} Exercise {{ module.exercise }}{% endif -%}
{%- if module.notebook %} [[colab](https://colab.research.google.com/github/daveminh/Chem550-2024F/blob/main/exercises/{{ module.notebook }}.ipynb)]. {% endif -%}
{%- if module.panopto %} [[Recording](https://iit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id={{module.panopto}})]{% endif -%}
{%- if module.due %} <u>Due:</u> {{ module.due }}. {% endif %}
{%- if module.quiz %} <u>Quiz:</u> {{ module.quiz }}. {% endif %} |
{% endfor %}

During the final exam period (TBD), students will give a final presentation. Exercise 8 is due on December 2 at noon. The final report and individual contribution report is due on December 9 at noon.