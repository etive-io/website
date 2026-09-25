---
layout: default
title: "Documentation"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Documentation</h1>
        <p class="lead text-muted">Comprehensive documentation for asimov and its ecosystem packages.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="h3 fw-bold mb-4">Core Framework</h2>
        
        {% assign core = site.data.registry.packages | where: "category", "core" | first %}
        {% if core %}
        <div class="card mb-4 package-card">
          <div class="card-body">
            <h4>{{ core.name }}</h4>
            <p class="package-description">{{ core.summary }}</p>
            <div class="package-links">
              <a href="{{ core.docs }}" target="_blank">Documentation →</a>
              <a href="{{ core.repo_url }}" target="_blank">GitHub →</a>
            </div>
          </div>
        </div>
        {% endif %}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="h3 fw-bold mb-4">Plugins</h2>
        <p class="text-muted mb-4">Extend asimov with plugins for analysis pipelines, data handling, and more:</p>
        
        {% for category in site.data.registry.categories %}
          {% if category.id != "core" %}
            {% assign plugins = site.data.registry.packages | where: "category", category.id %}
            {% if plugins.size > 0 %}
              <h3 class="h5 fw-bold mt-5 mb-3">{{ category.label }}</h3>
              <table class="table table-sm">
                <thead>
                  <tr>
                    <th>Plugin</th>
                    <th>Description</th>
                    <th>Documentation</th>
                  </tr>
                </thead>
                <tbody>
                  {% assign sorted_plugins = plugins | sort: "name" %}
                  {% for plugin in sorted_plugins %}
                  <tr>
                    <td><a href="{{ "/plugins/" | append: plugin.slug | append: "/" | relative_url }}">{{ plugin.name }}</a></td>
                    <td>{{ plugin.summary }}</td>
                    <td>
                      {% if plugin.docs %}
                        <a href="{{ plugin.docs }}" target="_blank">Docs</a>
                      {% else %}
                        <a href="{{ "/plugins/" | append: plugin.slug | append: "/" | relative_url }}">README</a>
                      {% endif %}
                    </td>
                  </tr>
                  {% endfor %}
                </tbody>
              </table>
            {% endif %}
          {% endif %}
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-3">Guides in the asimov documentation</h2>
        <p class="text-muted">The <a href="https://asimov.docs.ligo.org/asimov/">asimov documentation</a> is the reference for the core package. Good starting points:</p>
        <ul class="list-unstyled learn-list">
          <li><a href="https://asimov.docs.ligo.org/asimov/getting-started.html">Getting started</a><span>install asimov and set up a project</span></li>
          <li><a href="https://asimov.docs.ligo.org/asimov/blueprints.html">Blueprints</a><span>the YAML format for projects, subjects and analyses, and how settings cascade</span></li>
          <li><a href="https://asimov.docs.ligo.org/asimov/ledger.html">The ledger</a><span>where asimov records every analysis and its state</span></li>
          <li><a href="https://asimov.docs.ligo.org/asimov/clusters.html">Clusters and schedulers</a><span>running on HTCondor and Slurm</span></li>
          <li><a href="https://asimov.docs.ligo.org/asimov/monitor-state-machine.html">Monitoring</a><span>how asimov tracks jobs and recovers from failures</span></li>
          <li><a href="https://asimov.docs.ligo.org/asimov/hooks.html">Hooks</a><span>extending asimov with post-monitor, applicator and file-source hooks</span></li>
          <li><a href="https://asimov.docs.ligo.org/asimov/api/asimov.html">API reference</a><span>the Python API, generated from the source</span></li>
        </ul>
        <p class="mt-4 text-muted">For worked examples, see the <a href="{{ "/tutorials" | relative_url }}">tutorials</a>. To contribute to asimov or list a plugin, see <a href="{{ "/contributing" | relative_url }}">contributing</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto text-center">
        <h2 class="h3 fw-bold mb-3">Questions?</h2>
        <p class="lead text-muted mb-4">If you can't find what you're looking for in the documentation, reach out to the community or open an issue on GitHub.</p>
        <div>
          <a href="https://github.com/etive-io" target="_blank" class="btn btn-primary me-2">View on GitHub</a>
          <a href="{{ "/contributing" | relative_url }}" class="btn btn-outline-primary">Get Involved</a>
        </div>
      </div>
    </div>
  </div>
</section>
