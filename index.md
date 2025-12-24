---
layout: default
title: "Home"
---

<!-- Hero Section -->
<section class="hero">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-8 mx-auto text-center">
        <h1>Making gravitational-wave analysis fun, easy, and reproducible</h1>
        <p class="lead">etive.io hosts asimov and its ecosystem – a collection of tools designed to streamline gravitational-wave astrophysics analysis pipelines.</p>
        <div class="mt-4">
          <a href="{{ "/tutorials" | relative_url }}" class="btn btn-light btn-lg me-2">Get Started</a>
          <a href="https://github.com/etive-io" class="btn btn-outline-light btn-lg">View on GitHub</a>
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
        <h2 class="section-title">About asimov</h2>
        <p class="lead text-muted">asimov is a framework for managing and orchestrating gravitational-wave parameter estimation analyses. It provides a unified interface to multiple analysis pipelines, making it easier to run reproducible analyses across different codes.</p>
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
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 package-card">
          <div class="card-body">
            <h4>bilby</h4>
            <p class="package-description">A Bayesian inference library for gravitational-wave astronomy</p>
            <div class="package-links">
              <a href="https://github.com/bilby-dev/bilby" target="_blank">GitHub →</a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 package-card">
          <div class="card-body">
            <h4>cogwheel</h4>
            <p class="package-description">Efficient likelihood calculations for gravitational-wave signals</p>
            <div class="package-links">
              <a href="https://github.com/jroulet/cogwheel" target="_blank">GitHub →</a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 package-card">
          <div class="card-body">
            <h4>LALInference</h4>
            <p class="package-description">LIGO Algorithm Library inference package</p>
            <div class="package-links">
              <a href="https://github.com/lscsoft/lalsuite" target="_blank">GitHub →</a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 package-card">
          <div class="card-body">
            <h4>PyCBC</h4>
            <p class="package-description">Python toolkit for analysis of gravitational-wave data</p>
            <div class="package-links">
              <a href="https://github.com/gwastro/pycbc" target="_blank">GitHub →</a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 package-card">
          <div class="card-body">
            <h4>BayesWave</h4>
            <p class="package-description">Bayesian algorithm for detecting and characterizing gravitational-wave signals</p>
            <div class="package-links">
              <a href="https://git.ligo.org/lscsoft/bayeswave" target="_blank">LIGO Git →</a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 package-card">
          <div class="card-body">
            <h4>asimov-gwdata</h4>
            <p class="package-description">Data handling utilities for gravitational-wave analysis</p>
            <div class="package-links">
              <a href="https://github.com/etive-io/asimov-gwdata" target="_blank">GitHub →</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="row mt-4">
      <div class="col-lg-8 mx-auto">
        <h3 class="h4 fw-bold mt-4 mb-3">Pipeline Interfaces</h3>
        <p>asimov provides specialized interfaces to connect with different analysis pipelines:</p>
        <ul>
          <li><strong>asimov-pycbc</strong>: Interface between asimov and PyCBC (<a href="https://github.com/etive-io/asimov-pycbc" target="_blank">GitHub</a>)</li>
          <li><strong>asimov-cogwheel</strong>: Interface between asimov and cogwheel (<a href="https://github.com/etive-io/asimov-cogwheel" target="_blank">GitHub</a>)</li>
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
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
              <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
            </svg>
          </div>
          <h3 class="h5 fw-bold">Easy to Use</h3>
          <p class="text-muted">Unified interface across multiple analysis pipelines makes it simple to get started and switch between tools.</p>
        </div>
      </div>
      
      <div class="col-md-4">
        <div class="text-center">
          <div class="mb-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
              <path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z"/>
              <path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5L9.5 0zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z"/>
            </svg>
          </div>
          <h3 class="h5 fw-bold">Reproducible</h3>
          <p class="text-muted">Standardized workflows and configuration management ensure your analyses are reproducible and well-documented.</p>
        </div>
      </div>
      
      <div class="col-md-4">
        <div class="text-center">
          <div class="mb-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
              <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
            </svg>
          </div>
          <h3 class="h5 fw-bold">Community-Driven</h3>
          <p class="text-muted">Open-source and built by researchers, for researchers. Contributions are welcome and encouraged.</p>
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
