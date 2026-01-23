---
layout: default
title: "Home"
---

<!-- Hero Section -->
<section class="hero">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-8 mx-auto text-center">
        <h1>Scientific Workflow Orchestration</h1>
        <p class="lead">asimov is a robust, extensible framework for managing complex scientific computing workflows. Run Python, shell scripts, compiled binaries, and containerized applications—all orchestrated seamlessly at scale.</p>
        <p style="font-size: 1.1rem; color: rgba(255,255,255,0.85); margin-top: 1rem;">Built by LIGO researchers. Used in production by the gravitational-wave astronomy community. Ready for your domain.</p>
        <div class="mt-4">
          <a href="{{ "/tutorials/quickstart" | relative_url }}" class="btn btn-light btn-lg me-2">5-Minute Quickstart</a>
          <a href="{{ "/comparison" | relative_url }}" class="btn btn-outline-light btn-lg me-2">Compare to Nextflow</a>
          <a href="https://github.com/etive-io/asimov" class="btn btn-outline-light btn-lg">GitHub</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- About Section -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="section-title">What is asimov?</h2>
        <p class="lead text-muted">asimov is a workflow management system designed for scientific computing at scale. It handles job submission, monitoring, dependency resolution, and fault recovery across heterogeneous compute environments—without forcing you to learn a domain-specific language.</p>
        <p style="margin-top: 1.5rem; color: #6b7280; line-height: 1.8;">
          <strong>Write workflows in Python.</strong> Use native Python for logic, configuration, and integration. Call out to shell scripts, compiled binaries, containerized services, or other languages as needed. No DSL to learn.
        </p>
        <p style="color: #6b7280; line-height: 1.8;">
          <strong>Designed for research.</strong> Born from the LIGO collaboration's need to coordinate hundreds of parameter estimation analyses. Now proven across gravitational-wave physics, but equally applicable to genomics, climate modeling, machine learning, and beyond.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Ecosystem Section -->
<section class="section bg-light">
  <div class="container">
    <h2 class="section-title text-center">The asimov Ecosystem</h2>
    <p class="section-subtitle text-center">Integrations with leading gravitational-wave analysis pipelines</p>
    
    <div class="row g-4">
      {% for pipeline in site.data.projects.supported_pipelines %}
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 package-card">
          <div class="card-body">
            <h4>{{ pipeline.name }}</h4>
            <p class="package-description">{{ pipeline.short_description }}</p>
            <div class="package-links">
              <a href="{{ pipeline.github_url }}" target="_blank">{{ pipeline.git_label | default: 'GitHub' }} →</a>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
      
      {% for project in site.data.projects.core_projects %}
      {% if project.featured_on_homepage %}
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 package-card">
          <div class="card-body">
            <h4>{{ project.name }}</h4>
            <p class="package-description">{{ project.short_description }}</p>
            <div class="package-links">
              <a href="{{ project.github_url }}" target="_blank">GitHub →</a>
            </div>
          </div>
        </div>
      </div>
      {% endif %}
      {% endfor %}
    </div>
    
    <div class="row mt-4">
      <div class="col-lg-8 mx-auto">
        <h3 class="h4 fw-bold mt-4 mb-3">Pipeline Interfaces</h3>
        <p>asimov provides specialized interfaces to connect with different analysis pipelines:</p>
        <ul>
          {% for project in site.data.projects.pipeline_interfaces %}
          <li><strong>{{ project.name }}</strong>: {{ project.short_description }} (<a href="{{ project.github_url }}" target="_blank">GitHub</a>)</li>
          {% endfor %}
        </ul>
        <p class="mt-3">Explore more packages and tools in the <a href="https://github.com/etive-io" target="_blank">etive-io organization on GitHub</a>.</p>
      </div>
    </div>
  </div>
</section>

<!-- Features Section -->
<section class="section">
  <div class="container">
    <h2 class="section-title text-center">Why asimov?</h2>
    <p class="section-subtitle text-center">Designed to make gravitational-wave analysis accessible and reproducible</p>
    
    <div class="row g-4">
      <div class="col-md-4">
        <div class="text-center">
          <div class="mb-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
              <path d="M11 5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM8 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm.256 7a4.474 4.474 0 0 1-.848-1.454l-.853.482c.326.585.83 1.109 1.404 1.466l.414-.892ZM16 12.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm1.5-1.5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Zm-7.5 2.5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Zm2.5-8.5a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z"/>
            </svg>
          </div>
          <h3 class="h5 fw-bold">Language-Agnostic</h3>
          <p class="text-muted">Orchestrate Python, shell, C++, containers, and more. Write workflows in Python; call anything from anywhere.</p>
        </div>
      </div>
      
      <div class="col-md-4">
        <div class="text-center">
          <div class="mb-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
              <path d="M12.5 15H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h8.5a.5.5 0 0 1 .354.146l2.854 2.854a.5.5 0 0 1 .146.354V14a1 1 0 0 1-1 1zM4.5 13a.5.5 0 0 0 0 1h8a.5.5 0 0 0 0-1h-8zm0-3a.5.5 0 0 0 0 1h8a.5.5 0 0 0 0-1h-8zm0-3a.5.5 0 0 0 0 1h8a.5.5 0 0 0 0-1h-8z"/>
            </svg>
          </div>
          <h3 class="h5 fw-bold">Reproducible</h3>
          <p class="text-muted">Standardized configuration, version tracking, and audit logs ensure your science is reproducible and transparent.</p>
        </div>
      </div>
      
      <div class="col-md-4">
        <div class="text-center">
          <div class="mb-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
              <path d="M8 3.5a.5.5 0 0 0-1 0V9H3.5a.5.5 0 0 0 0 1H7v3.5a.5.5 0 0 0 1 0V10h3.5a.5.5 0 0 0 0-1H8V3.5z"/>
            </svg>
          </div>
          <h3 class="h5 fw-bold">Extensible</h3>
          <p class="text-muted">Plugin architecture lets you integrate your own analysis tools, backends, and custom logic seamlessly.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA Section -->
<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto text-center">
        <h2 class="section-title">Get Started Today</h2>
        <p class="lead text-muted mb-4">Ready to streamline your gravitational-wave analysis workflow?</p>
        <div>
          <a href="{{ "/tutorials" | relative_url }}" class="btn btn-primary btn-lg me-2">View Tutorials</a>
          <a href="{{ "/documentation" | relative_url }}" class="btn btn-outline-primary btn-lg">Read the Docs</a>
        </div>
      </div>
    </div>
  </div>
</section>
