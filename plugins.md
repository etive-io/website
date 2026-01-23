---
layout: default
title: "Plugins"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Asimov Plugins</h1>
        <p class="lead text-muted">Extend asimov with additional pipelines, tools, and integrations. Browse our collection of official and community plugins.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Filter by Type</h2>
        <div class="btn-group mb-4" role="group">
          <button type="button" class="btn btn-outline-primary" onclick="filterPlugins('all')">All</button>
          <button type="button" class="btn btn-outline-primary" onclick="filterPlugins('parameter-estimation')">Parameter Estimation</button>
          <button type="button" class="btn btn-outline-primary" onclick="filterPlugins('utility')">Utility</button>
          <button type="button" class="btn btn-outline-primary" onclick="filterPlugins('inference')">Inference</button>
          <button type="button" class="btn btn-outline-primary" onclick="filterPlugins('simulation')">Simulation</button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        {% assign plugins_by_type = site.plugins | group_by: "type" | sort: "name" %}
        
        {% for group in plugins_by_type %}
          <div class="plugin-category mb-5">
            <h3 class="h5 fw-bold text-uppercase text-muted mb-4">
              {% if group.name == "parameter-estimation" %}
                Parameter Estimation Pipelines
              {% elsif group.name == "psd-estimation" %}
                PSD & Data Analysis
              {% elsif group.name == "utility" %}
                Utility Tools
              {% elsif group.name == "inference" %}
                Inference & Population Analysis
              {% elsif group.name == "simulation" %}
                Simulation & Testing
              {% else %}
                {{ group.name | capitalize }} Tools
              {% endif %}
            </h3>
            
            {% for plugin in group.items | sort: "title" %}
            <div class="card mb-3">
              <div class="card-body">
                <div class="row align-items-start">
                  <div class="col-md-8">
                    <h4 class="card-title mb-2">
                      <a href="{{ plugin.url | relative_url }}">{{ plugin.title }}</a>
                    </h4>
                    <p class="text-muted mb-2">{{ plugin.description }}</p>
                    <p class="small mb-2">
                      <strong>Maintainer:</strong> {{ plugin.maintainer | default: "Community" }}
                    </p>
                  </div>
                  <div class="col-md-4 text-md-end">
                    <div class="mb-2">
                      {% if plugin.verified %}
                        <span class="badge bg-primary">✓ Verified</span>
                      {% endif %}
                      {% if plugin.status == "stable" %}
                        <span class="badge bg-success">Stable</span>
                      {% elsif plugin.status == "development" %}
                        <span class="badge bg-warning text-dark">Development</span>
                      {% elsif plugin.status == "experimental" %}
                        <span class="badge bg-info">Experimental</span>
                      {% endif %}
                    </div>
                    <div>
                      {% if plugin.github %}
                        <a href="{{ plugin.github }}" target="_blank" class="btn btn-sm btn-outline-secondary">GitHub</a>
                      {% endif %}
                    </div>
                  </div>
                </div>
              </div>
            </div>
            {% endfor %}
          </div>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Developing Your Own Plugin?</h2>
        <p>We provide a plugin template to help you get started:</p>
        <p>
          <a href="https://github.com/etive-io/asimov-plugin-template" class="btn btn-primary">View Plugin Template</a>
          <a href="/documentation/plugins/" class="btn btn-outline-primary">Plugin Development Guide</a>
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto text-center">
        <h2 class="h3 fw-bold mb-3">Have a Plugin to Share?</h2>
        <p class="lead text-muted mb-4">If you've developed an asimov plugin, we'd love to hear about it! Submit it for inclusion in our registry.</p>
        <div>
          <a href="https://github.com/etive-io/website/issues/new?template=plugin-submission.md" class="btn btn-primary me-2">Submit Your Plugin</a>
          <a href="/contributing/" class="btn btn-outline-primary">Contributing Guidelines</a>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
function filterPlugins(type) {
  // Placeholder for JavaScript filtering
  // In a static Jekyll site, this would typically require JavaScript or a rebuild
  console.log('Filter by: ' + type);
}
</script>
