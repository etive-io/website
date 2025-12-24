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
        
        <div class="card mb-4 package-card">
          <div class="card-body">
            <h4>asimov</h4>
            <p class="package-description">The main framework for managing gravitational-wave parameter estimation analyses across multiple pipelines.</p>
            <div class="package-links">
              <a href="https://github.com/etive-io/asimov" target="_blank">GitHub →</a>
              <a href="https://asimov.docs.ligo.org/asimov/" target="_blank">Documentation →</a>
            </div>
          </div>
        </div>
        
        <div class="card mb-4 package-card">
          <div class="card-body">
            <h4>asimov-gwdata</h4>
            <p class="package-description">Data handling utilities for gravitational-wave analysis, including data discovery, download, and quality checks.</p>
            <div class="package-links">
              <a href="https://github.com/etive-io/asimov-gwdata" target="_blank">GitHub →</a>
              <a href="https://github.com/etive-io/asimov-gwdata#readme" target="_blank">Documentation →</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="h3 fw-bold mb-4">Pipeline Interfaces</h2>
        
        <div class="card mb-4 package-card">
          <div class="card-body">
            <h4>asimov-pycbc</h4>
            <p class="package-description">Interface between asimov and PyCBC for running parameter estimation with PyCBC inference.</p>
            <div class="package-links">
              <a href="https://github.com/etive-io/asimov-pycbc" target="_blank">GitHub →</a>
              <a href="https://github.com/etive-io/asimov-pycbc#readme" target="_blank">Documentation →</a>
            </div>
          </div>
        </div>
        
        <div class="card mb-4 package-card">
          <div class="card-body">
            <h4>asimov-cogwheel</h4>
            <p class="package-description">Interface between asimov and cogwheel for efficient likelihood calculations using relative binning.</p>
            <div class="package-links">
              <a href="https://github.com/etive-io/asimov-cogwheel" target="_blank">GitHub →</a>
              <a href="https://github.com/etive-io/asimov-cogwheel#readme" target="_blank">Documentation →</a>
            </div>
          </div>
        </div>
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
          <div class="col-md-6">
            <div class="card h-100 package-card">
              <div class="card-body">
                <h4>bilby</h4>
                <p class="package-description">A Bayesian inference library for gravitational-wave astronomy and beyond.</p>
                <div class="package-links">
                  <a href="https://github.com/bilby-dev/bilby" target="_blank">GitHub →</a>
                  <a href="https://lscsoft.docs.ligo.org/bilby/" target="_blank">Documentation →</a>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100 package-card">
              <div class="card-body">
                <h4>PyCBC</h4>
                <p class="package-description">Python toolkit for analysis of data from gravitational-wave laser interferometer detectors.</p>
                <div class="package-links">
                  <a href="https://github.com/gwastro/pycbc" target="_blank">GitHub →</a>
                  <a href="https://pycbc.org/" target="_blank">Documentation →</a>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100 package-card">
              <div class="card-body">
                <h4>cogwheel</h4>
                <p class="package-description">Efficient likelihood calculations using relative binning for gravitational-wave parameter estimation.</p>
                <div class="package-links">
                  <a href="https://github.com/jroulet/cogwheel" target="_blank">GitHub →</a>
                  <a href="https://cogwheel.readthedocs.io/" target="_blank">Documentation →</a>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100 package-card">
              <div class="card-body">
                <h4>LALInference</h4>
                <p class="package-description">LIGO Algorithm Library inference package for Bayesian parameter estimation.</p>
                <div class="package-links">
                  <a href="https://github.com/lscsoft/lalsuite" target="_blank">GitHub →</a>
                  <a href="https://lscsoft.docs.ligo.org/lalsuite/" target="_blank">Documentation →</a>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100 package-card">
              <div class="card-body">
                <h4>BayesWave</h4>
                <p class="package-description">Bayesian algorithm for detecting and characterizing gravitational-wave signals in noisy data.</p>
                <div class="package-links">
                  <a href="https://git.ligo.org/lscsoft/bayeswave" target="_blank">LIGO Git →</a>
                  <a href="https://git.ligo.org/lscsoft/bayeswave/-/blob/master/README.md" target="_blank">Documentation →</a>
                </div>
              </div>
            </div>
          </div>
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
