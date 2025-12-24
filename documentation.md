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
        <h2 class="h3 fw-bold mb-4">Core Projects</h2>
        
        {% for project in site.data.projects.core_projects %}
        <div class="card mb-4 package-card">
          <div class="card-body">
            <h4>{{ project.name }}</h4>
            <p class="package-description">{{ project.description }}</p>
            <div class="package-links">
              <a href="{{ project.github_url }}" target="_blank">GitHub →</a>
              <a href="{{ project.docs_url }}" target="_blank">Documentation →</a>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="h3 fw-bold mb-4">Pipeline Interfaces</h2>
        
        {% for project in site.data.projects.pipeline_interfaces %}
        <div class="card mb-4 package-card">
          <div class="card-body">
            <h4>{{ project.name }}</h4>
            <p class="package-description">{{ project.description }}</p>
            <div class="package-links">
              <a href="{{ project.github_url }}" target="_blank">GitHub →</a>
              <a href="{{ project.docs_url }}" target="_blank">Documentation →</a>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="h3 fw-bold mb-4">Supported Analysis Pipelines</h2>
        <p class="text-muted mb-4">asimov integrates with several leading gravitational-wave analysis pipelines. Each pipeline has its own comprehensive documentation:</p>
        
        <div class="row g-4">
          {% for pipeline in site.data.projects.supported_pipelines %}
          <div class="col-md-6">
            <div class="card h-100 package-card">
              <div class="card-body">
                <h4>{{ pipeline.name }}</h4>
                <p class="package-description">{{ pipeline.description }}</p>
                <div class="package-links">
                  <a href="{{ pipeline.github_url }}" target="_blank">{% if pipeline.git_label %}{{ pipeline.git_label }}{% else %}GitHub{% endif %} →</a>
                  <a href="{{ pipeline.docs_url }}" target="_blank">Documentation →</a>
                </div>
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">API Documentation</h2>
        <p class="text-muted mb-4">Detailed API documentation is automatically generated from the source code for each package. This includes:</p>
        
        <ul>
          <li>Class and function references</li>
          <li>Parameter descriptions and types</li>
          <li>Return value specifications</li>
          <li>Usage examples</li>
          <li>Cross-references to related components</li>
        </ul>
        
        <p class="mt-4">API documentation is built and hosted through GitHub Actions for each package. Visit the individual package repositories linked above to access their latest API documentation.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Documentation Resources</h2>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">User Guides</h5>
            <p class="text-muted mb-0">Step-by-step guides for common tasks and workflows. See the <a href="{{ "/tutorials" | relative_url }}">Tutorials</a> section.</p>
          </div>
        </div>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Examples</h5>
            <p class="text-muted mb-0">Example configurations and analysis scripts demonstrating best practices.</p>
          </div>
        </div>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Contributing Guide</h5>
            <p class="text-muted mb-0">Learn how to contribute to asimov and its ecosystem. See the <a href="{{ "/contributing" | relative_url }}">Contributing</a> section.</p>
          </div>
        </div>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">FAQ</h5>
            <p class="text-muted mb-0">Frequently asked questions and troubleshooting tips (coming soon).</p>
          </div>
        </div>
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
