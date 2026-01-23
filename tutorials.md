---
layout: default
title: "Tutorials"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Tutorials & Examples</h1>
        <p class="lead text-muted">Learn how to use asimov and its ecosystem with step-by-step tutorials and practical examples.</p>
      </div>
    </div>
  </div>
</section>

{% assign pinned_tutorials = site.tutorials | where: "pin", true | sort: "order" %}
{% assign other_tutorials = site.tutorials | where: "pin", nil %}

{% if pinned_tutorials.size > 0 %}
<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">✨ Quickstart Tutorials</h2>
        
        {% for tutorial in pinned_tutorials %}
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">{{ tutorial.title }}</h3>
            {% if tutorial.excerpt %}
              <p class="text-muted">{{ tutorial.excerpt | strip_html }}</p>
            {% endif %}
            <div class="mt-3">
              <a href="{{ tutorial.url | relative_url }}" class="btn btn-sm btn-primary">Read Tutorial</a>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</section>
{% endif %}

{% assign categories = site.tutorials | map: "category" | uniq | sort %}

{% for category in categories %}
  {% assign filtered_tutorials = site.tutorials | where: "category", category | where: "pin", nil | sort: "order" %}
  {% if filtered_tutorials.size > 0 %}
    {% if category == "getting-started" %}
      {% assign category_title = "Getting Started" %}
      {% assign section_class = "section bg-light" %}
    {% elsif category == "pipelines" %}
      {% assign category_title = "Pipeline-Specific Tutorials" %}
      {% assign section_class = "section" %}
    {% elsif category == "advanced" %}
      {% assign category_title = "Advanced Topics" %}
      {% assign section_class = "section bg-light" %}
    {% else %}
      {% assign category_title = category | capitalize %}
      {% if forloop.index0 | modulo: 2 == 1 %}
        {% assign section_class = "section bg-light" %}
      {% else %}
        {% assign section_class = "section" %}
      {% endif %}
    {% endif %}

<section class="{{ section_class }}">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">{{ category_title }}</h2>
        
        {% for tutorial in filtered_tutorials %}
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">{{ tutorial.title }}</h3>
            {% if tutorial.excerpt %}
              <p class="text-muted">{{ tutorial.excerpt | strip_html }}</p>
            {% endif %}
            <div class="mt-3">
              <a href="{{ tutorial.url | relative_url }}" class="btn btn-sm btn-primary">Read Tutorial</a>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</section>
  {% endif %}
{% endfor %}

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto text-center">
        <h2 class="h3 fw-bold mb-3">Need Help?</h2>
        <p class="lead text-muted mb-4">Can't find what you're looking for? Check out the documentation or reach out to the community.</p>
        <div>
          <a href="{{ "/documentation" | relative_url }}" class="btn btn-primary me-2">Documentation</a>
          <a href="{{ "/contributing" | relative_url }}" class="btn btn-outline-primary">Contributing Guide</a>
        </div>
      </div>
    </div>
  </div>
</section>
