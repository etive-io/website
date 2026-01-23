---
layout: default
title: "Features"
---

<!-- Hero Section -->
<section class="hero">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-8 mx-auto text-center">
        <h1>Workflow automation for scientific research</h1>
        <p class="lead">Run, monitor, and orchestrate complex analyses across heterogeneous compute environments—from laptops to HPC clusters.</p>
        <div class="mt-4">
          <a href="{{ "/tutorials" | relative_url }}" class="btn btn-light btn-lg me-2">Get Started</a>
          <a href="{{ "/comparison" | relative_url }}" class="btn btn-outline-light btn-lg me-2">Compare to Nextflow</a>
          <a href="{{ "/documentation" | relative_url }}" class="btn btn-outline-light btn-lg">Docs</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- What is Asimov -->
<section class="section">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-10">
        <h2 class="section-title">What is asimov?</h2>
        <p class="section-subtitle">
          A workflow management framework that orchestrates complex scientific computing at scale.
        </p>
        <p style="font-size: 1.1rem; color: #6b7280; line-height: 1.8;">
          <strong>asimov was created by the LIGO, Virgo, and KAGRA gravitational-wave physics collaborations</strong> to orchestrate hundreds of parameter estimation analyses. It managed the complete O3 and O4 observing run catalogues. But asimov isn't limited to gravitational waves—its extensible architecture makes it powerful for any large-scale scientific workflow.
        </p>
        <p style="font-size: 1.1rem; color: #6b7280; line-height: 1.8;">
          Write your analysis logic in <strong>Python</strong>. Call <strong>shell scripts, compiled code, containers, or other languages</strong> from anywhere. asimov handles the orchestration, monitoring, dependency resolution, and fault recovery. It integrates with your existing compute infrastructure—whether that's HTCondor, SLURM, Kubernetes, or the cloud.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Key Features -->
<section class="section bg-light">
  <div class="container">
    <div class="row justify-content-center mb-5">
      <div class="col-lg-8 text-center">
        <h2 class="section-title">Built for research workflows</h2>
        <p class="section-subtitle mx-auto">
          Asimov solves the practical problems researchers face when running computational analyses.
        </p>
      </div>
    </div>

    <div class="row g-4">
      <div class="col-md-6 col-lg-4">
        <div class="card h-100">
          <div class="card-body">
            <div class="mb-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
                <path d="M8 4.754a3.246 3.246 0 1 0 0 6.492 3.246 3.246 0 0 0 0-6.492zM5.754 8a2.246 2.246 0 1 1 4.492 0 2.246 2.246 0 0 1-4.492 0z"/>
                <path d="M9.796 1.343c-.527-1.79-3.065-1.79-3.592 0l-.094.319a.873.873 0 0 1-1.255.52l-.292-.16c-1.64-.892-3.433.902-2.54 2.541l.159.292a.873.873 0 0 1-.52 1.255l-.319.094c-1.79.527-1.79 3.065 0 3.592l.319.094a.873.873 0 0 1 .52 1.255l-.16.292c-.892 1.64.901 3.434 2.541 2.54l.292-.159a.873.873 0 0 1 1.255.52l.094.319c.527 1.79 3.065 1.79 3.592 0l.094-.319a.873.873 0 0 1 1.255-.52l.292.16c1.64.893 3.434-.902 2.54-2.541l-.159-.292a.873.873 0 0 1 .52-1.255l.319-.094c1.79-.527 1.79-3.065 0-3.592l-.319-.094a.873.873 0 0 1-.52-1.255l.16-.292c.893-1.64-.902-3.433-2.541-2.54l-.292.159a.873.873 0 0 1-1.255-.52l-.094-.319z"/>
              </svg>
            </div>
            <h3 class="h5 fw-bold">Unified pipeline interface</h3>
            <p class="text-muted">
              Write your analysis configuration once and deploy it across multiple pipelines. Switch between
              Bilby, LALInference, RIFT, Bayeswave, or custom codes without reconfiguring your analyses.
              Perfect for comparing methodologies or testing new approaches.
            </p>
          </div>
        </div>
      </div>

      <div class="col-md-6 col-lg-4">
        <div class="card h-100">
          <div class="card-body">
            <div class="mb-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                <path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533L8.93 6.588zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/>
              </svg>
            </div>
            <h3 class="h5 fw-bold">Automated job management</h3>
            <p class="text-muted">
              Asimov monitors your analyses, detects failures, and handles recovery automatically.
              It manages dependencies between jobs using DAG orchestration and submits work to HTCondor clusters.
              Focus on your research, not job babysitting.
            </p>
          </div>
        </div>
      </div>

      <div class="col-md-6 col-lg-4">
        <div class="card h-100">
          <div class="card-body">
            <div class="mb-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
                <path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z"/>
                <path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5L9.5 0zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z"/>
              </svg>
            </div>
            <h3 class="h5 fw-bold">Centralized configuration</h3>
            <p class="text-muted">
              All project metadata, configurations, and status tracked in a single YAML ledger.
              Hierarchical configuration with intelligent precedence (global → pipeline → event → analysis)
              means you define defaults once and override only what's needed.
            </p>
          </div>
        </div>
      </div>

      <div class="col-md-6 col-lg-4">
        <div class="card h-100">
          <div class="card-body">
            <div class="mb-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
                <path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM5 8h6a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/>
              </svg>
            </div>
            <h3 class="h5 fw-bold">Reproducible by design</h3>
            <p class="text-muted">
              Every configuration is version-controlled. Results are stored in read-only locations.
              Complete log archival and exact configuration replay ensure your analyses can be
              independently verified and reproduced.
            </p>
          </div>
        </div>
      </div>

      <div class="col-md-6 col-lg-4">
        <div class="card h-100">
          <div class="card-body">
            <div class="mb-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
                <path d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h13zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-13z"/>
                <path d="M3 5.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 8a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 8zm0 2.5a.5.5 0 0 1 .5-.5h6a.5.5 0 0 1 0 1h-6a.5.5 0 0 1-.5-.5z"/>
              </svg>
            </div>
            <h3 class="h5 fw-bold">Genuinely extensible</h3>
            <p class="text-muted">
              Add new pipelines via Python plugins without modifying core code. Hook system allows
              custom behavior at every stage. Template-based configuration generation supports any
              pipeline format. Built for customization, not just configuration.
            </p>
          </div>
        </div>
      </div>

      <div class="col-md-6 col-lg-4">
        <div class="card h-100">
          <div class="card-body">
            <div class="mb-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="text-primary" viewBox="0 0 16 16">
                <path d="M1 2.5A1.5 1.5 0 0 1 2.5 1h3A1.5 1.5 0 0 1 7 2.5v3A1.5 1.5 0 0 1 5.5 7h-3A1.5 1.5 0 0 1 1 5.5v-3zM2.5 2a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3zm6.5.5A1.5 1.5 0 0 1 10.5 1h3A1.5 1.5 0 0 1 15 2.5v3A1.5 1.5 0 0 1 13.5 7h-3A1.5 1.5 0 0 1 9 5.5v-3zm1.5-.5a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3zM1 10.5A1.5 1.5 0 0 1 2.5 9h3A1.5 1.5 0 0 1 7 10.5v3A1.5 1.5 0 0 1 5.5 15h-3A1.5 1.5 0 0 1 1 13.5v-3zm1.5-.5a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3zm6.5.5A1.5 1.5 0 0 1 10.5 9h3a1.5 1.5 0 0 1 1.5 1.5v3a1.5 1.5 0 0 1-1.5 1.5h-3A1.5 1.5 0 0 1 9 13.5v-3zm1.5-.5a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3z"/>
              </svg>
            </div>
            <h3 class="h5 fw-bold">Scale effortlessly</h3>
            <p class="text-muted">
              From single-event exploratory analysis on your laptop to hundreds of coordinated
              production runs on a cluster. The same configuration works at any scale. Proven
              in production for major gravitational wave catalogue analyses.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Why Asimov -->
<section class="section">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-6 mb-4">
        <h2 class="section-title">Why asimov?</h2>
        <p style="font-size: 1.1rem; color: #6b7280; line-height: 1.8; margin-bottom: 2rem;">
          Most workflow tools are either too generic (requiring substantial custom code) or too rigid
          (locking you into specific analysis approaches). Asimov strikes a balance: it understands
          scientific workflows while remaining flexible enough to adapt to your needs.
        </p>

        <ul style="list-style: none; padding-left: 0;">
          <li style="padding: 0.5rem 0; padding-left: 2rem; position: relative;">
            <span style="position: absolute; left: 0; color: #2563eb; font-weight: 700; font-size: 1.2rem;">✓</span>
            <strong>No vendor lock-in:</strong> Plugin architecture means you can add any analysis pipeline
          </li>
          <li style="padding: 0.5rem 0; padding-left: 2rem; position: relative;">
            <span style="position: absolute; left: 0; color: #2563eb; font-weight: 700; font-size: 1.2rem;">✓</span>
            <strong>Battle-tested:</strong> Used for major LIGO/Virgo/KAGRA catalogue production
          </li>
          <li style="padding: 0.5rem 0; padding-left: 2rem; position: relative;">
            <span style="position: absolute; left: 0; color: #2563eb; font-weight: 700; font-size: 1.2rem;">✓</span>
            <strong>Multi-pipeline by design:</strong> Compare different codes on the same data seamlessly
          </li>
          <li style="padding: 0.5rem 0; padding-left: 2rem; position: relative;">
            <span style="position: absolute; left: 0; color: #2563eb; font-weight: 700; font-size: 1.2rem;">✓</span>
            <strong>Collaborative:</strong> Built-in authentication, role-based access, and audit logging
          </li>
          <li style="padding: 0.5rem 0; padding-left: 2rem; position: relative;">
            <span style="position: absolute; left: 0; color: #2563eb; font-weight: 700; font-size: 1.2rem;">✓</span>
            <strong>Python-native:</strong> Simple API for programmatic project management
          </li>
          <li style="padding: 0.5rem 0; padding-left: 2rem; position: relative;">
            <span style="position: absolute; left: 0; color: #2563eb; font-weight: 700; font-size: 1.2rem;">✓</span>
            <strong>Self-healing:</strong> Automatic failure detection and recovery reduces manual intervention
          </li>
        </ul>
      </div>
      <div class="col-lg-6">
        <div style="background: linear-gradient(135deg, #e0e7ff 0%, #f0e7ff 100%); border-radius: 0.75rem; min-height: 350px; display: flex; align-items: center; justify-content: center; color: #6b7280; font-size: 1.2rem; font-style: italic; border: 2px dashed #e5e7eb;">
          Workflow visualization or architecture diagram
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Use Cases -->
<section class="section bg-light">
  <div class="container">
    <div class="row justify-content-center mb-5">
      <div class="col-lg-8 text-center">
        <h2 class="section-title">Who uses asimov?</h2>
        <p class="section-subtitle mx-auto">
          From single-event analyses to large-scale catalogue production.
        </p>
      </div>
    </div>

    <div class="row g-4">
      <div class="col-lg-6">
        <div class="card h-100" style="border-left: 4px solid #2563eb;">
          <div class="card-body">
            <h4 class="h5 fw-bold">Gravitational wave researchers</h4>
            <p class="text-muted mb-0">
              Coordinate parameter estimation across multiple pipelines and events.
              Automatically manage PSD generation, waveform selection, and post-processing workflows.
            </p>
          </div>
        </div>
      </div>

      <div class="col-lg-6">
        <div class="card h-100" style="border-left: 4px solid #2563eb;">
          <div class="card-body">
            <h4 class="h5 fw-bold">Catalogue production teams</h4>
            <p class="text-muted mb-0">
              Systematically process hundreds of events with consistent configurations.
              Track progress across the entire catalogue and identify problematic analyses at a glance.
            </p>
          </div>
        </div>
      </div>

      <div class="col-lg-6">
        <div class="card h-100" style="border-left: 4px solid #2563eb;">
          <div class="card-body">
            <h4 class="h5 fw-bold">Methodology comparison studies</h4>
            <p class="text-muted mb-0">
              Run the same analysis with different pipelines, approximants, or priors.
              Unified configuration means you change only what matters for your comparison.
            </p>
          </div>
        </div>
      </div>

      <div class="col-lg-6">
        <div class="card h-100" style="border-left: 4px solid #2563eb;">
          <div class="card-body">
            <h4 class="h5 fw-bold">Cross-institutional collaborations</h4>
            <p class="text-muted mb-0">
              Role-based access control and audit logging support team workflows.
              SciTokens integration provides institutional authentication.
            </p>
          </div>
        </div>
      </div>

      <div class="col-lg-6">
        <div class="card h-100" style="border-left: 4px solid #2563eb;">
          <div class="card-body">
            <h4 class="h5 fw-bold">Multi-stage data processing</h4>
            <p class="text-muted mb-0">
              Automatic dependency resolution ensures analyses run in the correct order.
              Share data between stages (e.g., PSDs from Bayeswave to Bilby) seamlessly.
            </p>
          </div>
        </div>
      </div>

      <div class="col-lg-6">
        <div class="card h-100" style="border-left: 4px solid #2563eb;">
          <div class="card-body">
            <h4 class="h5 fw-bold">Custom analysis pipelines</h4>
            <p class="text-muted mb-0">
              Plugin architecture allows you to integrate your own codes.
              Benefit from asimov's monitoring, configuration, and results management for any analysis tool.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- How It Works -->
<section class="section">
  <div class="container">
    <div class="row justify-content-center mb-5">
      <div class="col-lg-8 text-center">
        <h2 class="section-title">How it works</h2>
        <p class="section-subtitle mx-auto">
          Asimov manages the entire lifecycle of your analyses.
        </p>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-10 mx-auto">
        <div style="background: linear-gradient(135deg, #e0e7ff 0%, #f0e7ff 100%); border-radius: 0.75rem; min-height: 300px; display: flex; align-items: center; justify-content: center; color: #6b7280; font-size: 1.2rem; font-style: italic; border: 2px dashed #e5e7eb; margin-bottom: 3rem;">
          Workflow lifecycle diagram
        </div>

        <div class="row g-4 text-center">
          <div class="col-md-3">
            <div style="width: 60px; height: 60px; background: #2563eb; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin: 0 auto 1rem;">1</div>
            <h5 class="fw-bold">Configure</h5>
            <p class="text-muted">Define analyses in YAML blueprints</p>
          </div>
          <div class="col-md-3">
            <div style="width: 60px; height: 60px; background: #2563eb; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin: 0 auto 1rem;">2</div>
            <h5 class="fw-bold">Submit</h5>
            <p class="text-muted">Asimov builds DAGs and submits jobs</p>
          </div>
          <div class="col-md-3">
            <div style="width: 60px; height: 60px; background: #2563eb; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin: 0 auto 1rem;">3</div>
            <h5 class="fw-bold">Monitor</h5>
            <p class="text-muted">Automatic failure detection and recovery</p>
          </div>
          <div class="col-md-3">
            <div style="width: 60px; height: 60px; background: #2563eb; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin: 0 auto 1rem;">4</div>
            <h5 class="fw-bold">Collect</h5>
            <p class="text-muted">Results organized and archived</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Extensibility -->
<section class="section bg-light">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-6 mb-4 order-lg-2">
        <div style="background: linear-gradient(135deg, #e0e7ff 0%, #f0e7ff 100%); border-radius: 0.75rem; min-height: 350px; display: flex; align-items: center; justify-content: center; color: #6b7280; font-size: 1.2rem; font-style: italic; border: 2px dashed #e5e7eb;">
          Plugin architecture diagram
        </div>
      </div>
      <div class="col-lg-6 order-lg-1">
        <h2 class="section-title">Designed for extension</h2>
        <p style="font-size: 1.1rem; color: #6b7280; line-height: 1.8;">
          Asimov's plugin architecture means you're never locked in. Add new analysis pipelines by
          subclassing a simple Python interface. Use hooks to inject custom behavior at any stage.
          Template-based configuration generation adapts to any pipeline's input format.
        </p>
        <p style="font-size: 1.1rem; color: #6b7280; line-height: 1.8;">
          The same extensibility that allows asimov to support multiple gravitational wave pipelines
          makes it straightforward to integrate with your own analysis codes. You get the benefit of
          robust workflow orchestration without rebuilding it yourself.
        </p>

        <div class="card mt-4" style="background: white; padding: 2rem; border: 1px solid #e5e7eb; border-radius: 0.75rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
          <blockquote style="font-size: 1.2rem; line-height: 1.7; color: #1f2937; font-style: italic; margin-bottom: 1rem; border-left: 4px solid #2563eb; padding-left: 1.5rem;">
            "We developed asimov because we needed to coordinate hundreds of analyses
            across different pipelines. It's designed to handle real research complexity."
          </blockquote>
          <div style="font-size: 1rem; color: #6b7280;">— The asimov development team</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Getting Started -->
<section class="section">
  <div class="container">
    <div class="row justify-content-center mb-5">
      <div class="col-lg-8 text-center">
        <h2 class="section-title">Get started</h2>
        <p class="section-subtitle mx-auto">
          Install asimov and create your first project in minutes.
        </p>
      </div>
    </div>

    <div class="row justify-content-center">
      <div class="col-lg-8">
        <h4 class="mb-3">Installation</h4>
        <pre style="background-color: #2d3748; color: #e2e8f0; padding: 1.5rem; border-radius: 0.5rem; overflow-x: auto;"><code><span style="color: #a0aec0;"># Install via pip</span>
<span style="color: #81e6d9;">$ pip install asimov</span>

<span style="color: #a0aec0;"># Or via conda</span>
<span style="color: #81e6d9;">$ conda install -c conda-forge asimov</span></code></pre>

        <h4 class="mb-3 mt-5">Create your first project</h4>
        <pre style="background-color: #2d3748; color: #e2e8f0; padding: 1.5rem; border-radius: 0.5rem; overflow-x: auto;"><code><span style="color: #a0aec0;"># Create a project directory</span>
<span style="color: #81e6d9;">$ mkdir my-analysis && cd my-analysis</span>

<span style="color: #a0aec0;"># Initialize asimov project</span>
<span style="color: #81e6d9;">$ asimov init "My Analysis Project"</span>

<span style="color: #a0aec0;"># Load default configurations</span>
<span style="color: #81e6d9;">$ asimov apply -f https://git.ligo.org/asimov/data/-/raw/main/defaults/production-pe.yaml</span>

<span style="color: #a0aec0;"># Add an event (e.g., GW150914)</span>
<span style="color: #81e6d9;">$ asimov apply -f https://git.ligo.org/asimov/data/-/raw/main/events/gwtc-1/GW150914_095045.yaml</span>

<span style="color: #a0aec0;"># Add an analysis</span>
<span style="color: #81e6d9;">$ asimov manage analysis add bilby</span>

<span style="color: #a0aec0;"># Check project status</span>
<span style="color: #81e6d9;">$ olivaw monitor</span></code></pre>

        <p class="text-center mt-4">
          <a href="{{ "/tutorials" | relative_url }}" class="btn btn-primary btn-lg">View Full Tutorials</a>
          <a href="{{ "/documentation" | relative_url }}" class="btn btn-outline-primary btn-lg ms-2">Read Documentation</a>
        </p>
      </div>
    </div>
  </div>
</section>

<!-- CTA Section -->
<section class="hero">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto text-center">
        <h2 style="font-size: 2.5rem; font-weight: 700; margin-bottom: 1.5rem;">Start orchestrating your analyses</h2>
        <p style="font-size: 1.2rem; opacity: 0.95; margin-bottom: 2rem;">
          Join the researchers using asimov for reproducible, scalable workflow automation.
        </p>
        <a href="{{ "/tutorials" | relative_url }}" class="btn btn-light btn-lg">Get Started</a>
      </div>
    </div>
  </div>
</section>
