---
layout: default
title: "Pipelines"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Asimov Pipelines</h1>
        <p class="lead text-muted">Browse supported analysis pipelines and core integrations. These are the execution backends that asimov orchestrates for inference and data conditioning.</p>
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
          <button type="button" class="btn btn-outline-primary" onclick="filterPlugins('psd-estimation')">PSD &amp; Data Conditioning</button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        {% assign pipeline_plugins = site.plugins | where_exp: "pipeline", "pipeline.type == 'parameter-estimation' or pipeline.type == 'psd-estimation'" %}
        {% assign pipelines_by_type = pipeline_plugins | group_by: "type" | sort: "name" %}
        
        {% for group in pipelines_by_type %}
          <div class="plugin-category mb-5">
            <h3 class="h5 fw-bold text-uppercase text-muted mb-4">
              {% if group.name == "parameter-estimation" %}
                Parameter Estimation
              {% elsif group.name == "psd-estimation" %}
                PSD & Data Conditioning
              {% else %}
                {{ group.name | capitalize }} Pipelines
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
        <h2 class="h3 fw-bold mb-4">Add a Pipeline Integration</h2>
        <p>Have a pipeline integration to share? Submit it to the registry and help others adopt it quickly.</p>
        <p>
          <a href="https://github.com/etive-io/website/issues/new?template=plugin-submission.md" class="btn btn-primary">Submit Pipeline Integration</a>
          <a href="/documentation/plugins/" class="btn btn-outline-primary">Integration Guide</a>
        </p>
      </div>
    </div>
  </div>
</section>

<script>
function filterPlugins(type) {
  // Placeholder for JavaScript filtering
  console.log('Filter by: ' + type);
}
</script>
