---
layout: default
title: "asimov: The Workflow Platform for Complex Scientific Research"
---

<!-- Hero Section -->
<section class="hero">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-8 mx-auto text-center">
        <h1>asimov: Built for Complex Scientific Workflows</h1>
        <p class="lead">Purpose-built for computational research with multiple interdependent codes, long-running analyses, and publication-grade reproducibility requirements.</p>
      </div>
    </div>
  </div>
</section>

<!-- Overview Section -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">Quick Feature Comparison</h2>
        <p class="section-subtitle">How asimov stacks up against general-purpose workflow tools</p>
        
        <div class="table-responsive mt-5">
          <table class="table table-bordered">
            <thead class="table-light">
              <tr>
                <th style="width: 20%;">Feature</th>
                <th style="width: 16%;">asimov</th>
                <th style="width: 16%;">Nextflow</th>
                <th style="width: 16%;">Snakemake</th>
                <th style="width: 16%;">Galaxy</th>
                <th style="width: 16%;">Cromwell</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Primary Language</strong></td>
                <td>Python</td>
                <td>Groovy/Java</td>
                <td>Python</td>
                <td>Web UI / YAML</td>
                <td>WDL</td>
              </tr>
              <tr>
                <td><strong>Workflow Definition</strong></td>
                <td>Python API + YAML</td>
                <td>Nextflow DSL</td>
                <td>Snakefile (Python)</td>
                <td>Graphical or YAML</td>
                <td>WDL</td>
              </tr>
              <tr>
                <td><strong>Target Users</strong></td>
                <td>Researchers / Developers</td>
                <td>Bioinformaticians / DevOps</td>
                <td>Bioinformaticians / Data Scientists</td>
                <td>Bench Scientists</td>
                <td>WDL Community / Genomics</td>
              </tr>
              <tr>
                <td><strong>Execution Backends</strong></td>
                <td>HTCondor, Local, Docker</td>
                <td>Nextflow Tower, Cloud native</td>
                <td>SLURM, PBS, Local, Cloud</td>
                <td>Local, Galaxy Server</td>
                <td>Google Cloud, AWS, Azure</td>
              </tr>
              <tr>
                <td><strong>Job Submission</strong></td>
                <td>Direct + Managed</td>
                <td>Native Cloud</td>
                <td>Cluster-aware</td>
                <td>Web UI</td>
                <td>Cloud-focused</td>
              </tr>
              <tr>
                <td><strong>Multi-language Support</strong></td>
                <td>✓ (Python-first)</td>
                <td>✓ (Groovy-first)</td>
                <td>✓ (Python-first)</td>
                <td>✓ (Tools)</td>
                <td>✓ (WDL tasks)</td>
              </tr>
              <tr>
                <td><strong>Containerization</strong></td>
                <td>Docker, Singularity</td>
                <td>Docker, Singularity, Podman</td>
                <td>Docker, Conda</td>
                <td>Tool containers</td>
                <td>Docker</td>
              </tr>
              <tr>
                <td><strong>Dependency Resolution</strong></td>
                <td>Manual + Automatic</td>
                <td>Automatic</td>
                <td>Automatic</td>
                <td>Manual</td>
                <td>Manual</td>
              </tr>
              <tr>
                <td><strong>Monitoring UI</strong></td>
                <td>Web dashboard (in development)</td>
                <td>Nextflow Tower (managed)</td>
                <td>Limited</td>
                <td>Web UI</td>
                <td>Cromwell Server</td>
              </tr>
              <tr>
                <td><strong>Extensibility</strong></td>
                <td>Plugin system</td>
                <td>Custom modules</td>
                <td>Custom rules</td>
                <td>Tool integration</td>
                <td>Custom tasks</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Physical Sciences Focus -->
<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">Built for Complex Scientific Research</h2>
        <p class="section-subtitle mb-5">Whether in physics, chemistry, biology, climate science, or computational engineering—asimov addresses the needs of research that demands multi-code orchestration and reproducibility</p>
        
        <div class="row g-4 mt-4">
          <div class="col-lg-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title fw-bold">🔬 Multi-Code Orchestration</h5>
                <p class="card-text">Seamlessly integrate Python, C++, Fortran, and shell pipelines in a single workflow. Define complex dependencies between heterogeneous codes without preprocessing or manual orchestration.</p>
              </div>
            </div>
          </div>
          
          <div class="col-lg-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title fw-bold">🖥️ Academic HPC Integration</h5>
                <p class="card-text">Native support for HTCondor, SLURM, and PBS—the infrastructure that powers university research. Works with your existing HPC cluster, not cloud-only platforms.</p>
              </div>
            </div>
          </div>
          
          <div class="col-lg-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title fw-bold">📊 Computational Scale</h5>
                <p class="card-text">Orchestrate thousands of jobs across heterogeneous resources. Built for parameter sweeps, ensemble methods, statistical inference at scale, and any workflow with massive computational demands.</p>
              </div>
            </div>
          </div>
          
          <div class="col-lg-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title fw-bold">🔐 Research Governance</h5>
                <p class="card-text">Audit trails, role-based access, and reproducibility built-in. Essential for collaborative research, multi-institution projects, and grant-mandated archival requirements.</p>
              </div>
            </div>
          </div>
          
          <div class="col-lg-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title fw-bold">🐍 Python-Native for Science</h5>
                <p class="card-text">Built entirely in Python, asimov integrates directly with NumPy, SciPy, Astropy, and domain-specific packages. No context-switching between DSLs—your analysis logic and orchestration logic are one.</p>
              </div>
            </div>
          </div>
          
          <div class="col-lg-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title fw-bold">📈 Reproducible Science</h5>
                <p class="card-text">Every workflow execution produces a complete audit trail. Version-tracked configurations, reproducible event data, and containerized codes ensure your research meets modern reproducibility standards.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Design Philosophy -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">The Research Orchestration Problem</h2>
        
        <p class="lead mb-4">Generic workflow tools weren't designed for the realities of computational research:</p>
        
        <div class="row g-4 mt-4">
          <div class="col-lg-6">
            <h5 class="fw-bold mb-3">The Research Challenge</h5>
            <ul>
              <li><strong>Multi-code workflows:</strong> Analyses flow through multiple interdependent analysis codes and simulations</li>
              <li><strong>Long-running computations:</strong> Individual jobs can take days or weeks; need robust management and recovery</li>
              <li><strong>Complex dependencies:</strong> Results from one code feed into the next; intricate orchestration needed</li>
              <li><strong>Heterogeneous compute:</strong> Mix of Python packages, compiled binaries, shell scripts, remote resources</li>
              <li><strong>Reproducibility at scale:</strong> Publication requirements demand complete audit trails across thousands of jobs</li>
            </ul>
          </div>
          
          <div class="col-lg-6">
            <h5 class="fw-bold mb-3">asimov's Solution</h5>
            <ul>
              <li><strong>Orchestration framework</strong> built for multi-code scientific pipelines</li>
              <li><strong>Stateful job management</strong> with recovery from partial failures</li>
              <li><strong>Monitoring dashboards</strong> for tracking hundreds or thousands of jobs</li>
              <li><strong>Plugin architecture</strong> for adding analysis codes without forking</li>
              <li><strong>Research infrastructure</strong> designed for publication-grade reproducibility</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Real-World Use Cases in Physics -->
<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">Current Focus & Future Directions</h2>
        <p class="section-subtitle mb-5">asimov currently powers gravitational wave astronomy research, with infrastructure designed to extend to any domain requiring multi-code orchestration</p>
        
        <div class="row g-4 mt-4">
          <div class="col-lg-6">
            <h5 class="fw-bold mb-3">🌊 Current: Gravitational Wave Astronomy</h5>
            <p class="mb-3">asimov is actively used for:</p>
            <ul class="small">
              <li>Multi-code parameter estimation pipelines (signal processing → Bayesian inference → population inference)</li>
              <li>Thousands of nested sampling jobs coordinated across LIGO and research institutions</li>
              <li>Ensemble simulations for synthetic data generation and detector characterization</li>
            </ul>
          </div>
          
          <div class="col-lg-6">
            <h5 class="fw-bold mb-3">🔮 Expanding To: Computational Science</h5>
            <p class="mb-3">The architecture applies directly to:</p>
            <ul class="small">
              <li><strong>Computational Biology:</strong> Molecular dynamics ensembles, free energy calculations, structure prediction</li>
              <li><strong>Climate Science:</strong> Model ensemble runs, coupled simulations, large-scale data analysis</li>
              <li><strong>Materials Science:</strong> Parameter sweeps, simulation pipelines, cross-code validation</li>
              <li><strong>ML in Science:</strong> Training dataset generation, hyperparameter optimization, model inference</li>
            </ul>
          </div>
        </div>
        
        <div class="alert alert-info mt-5" role="alert">
          <p class="mb-0"><strong>Building the next domain:</strong> If you work in computational science and see your workflow reflected in asimov's architecture, we'd like to hear from you. asimov is designed to expand beyond its current focus—get in touch if you're interested in piloting multi-code orchestration for your research.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Why Physics Needs a Different Tool -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">Why Specialized Tools Fall Short</h2>
        
        <div class="row g-4 mt-4">
          <div class="col-lg-6">
            <h5 class="fw-bold mb-3">Bioinformatics-First Tools</h5>
            <p><strong>Nextflow, Snakemake, Galaxy</strong> assume cloud infrastructure and pre-built tool ecosystems:</p>
            <ul class="small">
              <li>✗ Built for "docker pull biotools"; your Fortran solver isn't in Bioconda</li>
              <li>✗ Cloud-native designs miss HTCondor/SLURM resources universities depend on</li>
              <li>✗ Assume quick-running tasks; not designed for week-long parameter estimation</li>
              <li>✗ Limited state management for complex inter-code dependencies</li>
            </ul>
          </div>
          
          <div class="col-lg-6">
            <h5 class="fw-bold mb-3">Generic Job Schedulers</h5>
            <p><strong>Slurm, PBS, HTCondor</strong> can run individual jobs, but lack research-grade orchestration:</p>
            <ul class="small">
              <li>✗ No monitoring dashboards for tracking thousand-job surveys</li>
              <li>✗ Manual dependency management across codes</li>
              <li>✗ No audit trails for reproducibility</li>
              <li>✗ No integration with analysis packages (Bilby, LALInference, etc.)</li>
            </ul>
          </div>
          
          <div class="col-lg-6">
            <h5 class="fw-bold mb-3">Python Task Frameworks</h5>
            <p><strong>Celery, Dask, Ray</strong> are built for distributed computing, not research orchestration:</p>
            <ul class="small">
              <li>✗ No stateful workflow management</li>
              <li>✗ Poor support for HPC cluster integration</li>
              <li>✗ No built-in reproducibility or audit features</li>
              <li>✗ No monitoring UI or research-grade monitoring</li>
            </ul>
          </div>
          
          <div class="col-lg-6">
            <h5 class="fw-bold mb-3">asimov Fills the Gap</h5>
            <p><strong>Purpose-built for physics research:</strong></p>
            <ul class="small">
              <li>✓ Orchestrates multi-code scientific pipelines</li>
              <li>✓ Native HPC + Python package integration</li>
              <li>✓ Monitoring and state management for long-running analyses</li>
              <li>✓ Built-in reproducibility and audit trails</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Call to Action -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto text-center">
        <h2 class="section-title">Ready to Get Started?</h2>
        <p class="lead text-muted mb-4">Explore asimov with our tutorials and documentation.</p>
        <div>
          <a href="{{ "/tutorials" | relative_url }}" class="btn btn-primary btn-lg me-2">View Tutorials</a>
          <a href="https://github.com/etive-io/asimov" class="btn btn-outline-primary btn-lg">GitHub Repository</a>
        </div>
        
        <div class="alert alert-info mt-5" role="alert">
          <strong>Note:</strong> This comparison reflects asimov's current capabilities and design philosophy. The field of workflow orchestration is rapidly evolving. For the latest features and updates, check our <a href="https://github.com/etive-io/asimov">GitHub repository</a> and <a href="{{ "/documentation" | relative_url }}">documentation</a>.
        </div>
      </div>
    </div>
  </div>
</section>
