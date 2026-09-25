---
layout: default
title: "Home"
---
{% assign registry = site.data.registry %}
{% assign plugins = registry.packages | where_exp: "p", "p.category != 'core'" %}
{% assign featured = plugins | where: "featured", true %}
{% assign core = registry.packages | where: "name", "asimov" | first %}

<section class="hero">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-7">
        <p class="hero-eyebrow">asimov{% if core.latest_version %} · v{{ core.latest_version }}{% endif %} · open source (MIT)</p>
        <h1>Workflow infrastructure for large-scale scientific analysis</h1>
        <p class="lead">
          asimov automates, records and reproduces the analyses behind the gravitational-wave
          transient catalogues. It turns declarative blueprints into jobs on HTCondor and Slurm,
          keeps every analysis in a version-controlled ledger, and works with any analysis code
          through a documented plugin interface.
        </p>
        <div class="mt-4 d-flex flex-wrap gap-2">
          <a href="{{ '/tutorials/09-gw150914-quickstart/' | relative_url }}" class="btn btn-light btn-lg">Get started</a>
          <a href="{{ '/plugins/' | relative_url }}" class="btn btn-outline-light btn-lg">Browse plugins</a>
          <a href="https://github.com/etive-io/asimov" class="btn btn-outline-light btn-lg">Source code</a>
        </div>
      </div>
      <div class="col-lg-5">
        <div class="hero-install">
          <div class="hero-install-label">Install</div>
          <pre><code>pip install asimov</code></pre>
          <div class="hero-install-label">or</div>
          <pre><code>conda install -c conda-forge asimov</code></pre>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="evidence border-bottom">
  <div class="container">
    <div class="row text-center g-4 py-4">
      <div class="col-6 col-md-3">
        <div class="evidence-figure">GWTC-2 → 4.0</div>
        <div class="evidence-label">catalogues produced with asimov by the LIGO, Virgo and KAGRA collaborations</div>
      </div>
      <div class="col-6 col-md-3">
        <div class="evidence-figure">{{ plugins.size }}</div>
        <div class="evidence-label"><a href="{{ '/plugins/' | relative_url }}">plugins</a> for parameter estimation, data, searches and more</div>
      </div>
      <div class="col-6 col-md-3">
        <div class="evidence-figure">{{ site.data.citing-papers.total_citations | default: "—" }}</div>
        <div class="evidence-label"><a href="{{ '/impact' | relative_url }}">papers</a> citing asimov</div>
      </div>
      <div class="col-6 col-md-3">
        <div class="evidence-figure">HTCondor · Slurm</div>
        <div class="evidence-label">schedulers supported out of the box</div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">What asimov does</h2>
        <p class="lead text-muted mb-5">
          A catalogue of gravitational-wave events means thousands of analyses, run with several
          codes, over months, by many people. asimov exists so that each of those analyses is
          specified once, run automatically, and can be traced and re-run later.
        </p>
        <div class="row g-4 pillars">
          <div class="col-md-6">
            <h3>Declare</h3>
            <p>
              Analyses are described in YAML <a href="https://asimov.docs.ligo.org/asimov/blueprints.html">blueprints</a>:
              which pipeline, which settings, and which other analyses they depend on. Settings cascade from
              project to subject to analysis, so shared choices are made in one place and can be reviewed.
            </p>
          </div>
          <div class="col-md-6">
            <h3>Automate</h3>
            <p>
              asimov writes each pipeline's configuration, submits the jobs to HTCondor or Slurm,
              monitors them, resubmits them when they fail, and starts dependent analyses and
              post-processing when their inputs are ready.
            </p>
          </div>
          <div class="col-md-6">
            <h3>Record</h3>
            <p>
              A ledger holds the configuration and state of every analysis, and generated configurations are
              committed to git. Review sign-off is stored alongside each result, and HTML reports summarise
              the state of a whole project.
            </p>
          </div>
          <div class="col-md-6">
            <h3>Extend</h3>
            <p>
              Pipelines are Python packages that register through entry points, so asimov doesn't depend
              on any particular analysis code. Adding a pipeline means implementing one
              class; the <a href="{{ '/plugins/' | relative_url }}">registry</a> lists the existing ones.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-5">
        <h2 class="section-title">From blueprint to result</h2>
        <p class="text-muted">
          This blueprint asks for a noise-spectrum estimate followed by parameter estimation that
          uses it. asimov works out the order, builds both configurations, runs each job when its
          inputs are ready, and records the outcome in the ledger.
        </p>
<pre><code>kind: analysis
name: generate-psds
pipeline: bayeswave
---
kind: analysis
name: parameter-estimation
pipeline: bilby
needs:
  - generate-psds</code></pre>
<pre class="mt-3"><code>asimov apply -f analyses.yaml -e GW150914_095045
asimov manage build submit
asimov monitor</code></pre>
      </div>
      <div class="col-lg-7">
        <figure class="flow-figure">
          <svg viewBox="0 0 640 290" role="img" aria-labelledby="flow-title">
            <title id="flow-title">Blueprints are applied to the ledger; asimov builds pipeline configurations through plugins, submits them to a scheduler, monitors the jobs and records results and reviews back in the ledger.</title>
            <defs>
              <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
              </marker>
            </defs>
            <g class="flow-node"><rect x="10" y="30" width="130" height="64" rx="8"/><text x="75" y="58">Blueprints</text><text x="75" y="78" class="sub">YAML, reviewed</text></g>
            <g class="flow-node core"><rect x="250" y="20" width="140" height="84" rx="8"/><text x="320" y="52">Ledger</text><text x="320" y="72" class="sub">config · state</text><text x="320" y="90" class="sub">reviews · git</text></g>
            <g class="flow-node"><rect x="500" y="30" width="130" height="64" rx="8"/><text x="565" y="58">Plugins</text><text x="565" y="78" class="sub">bilby, pycbc, …</text></g>
            <g class="flow-node"><rect x="500" y="200" width="130" height="64" rx="8"/><text x="565" y="228">Scheduler</text><text x="565" y="248" class="sub">HTCondor · Slurm</text></g>
            <g class="flow-node"><rect x="250" y="200" width="140" height="64" rx="8"/><text x="320" y="228">Monitor</text><text x="320" y="248" class="sub">detect · resubmit</text></g>
            <g class="flow-node"><rect x="10" y="200" width="130" height="64" rx="8"/><text x="75" y="228">Results</text><text x="75" y="248" class="sub">reports · review</text></g>
            <g class="flow-edge">
              <path d="M140,62 L246,62" marker-end="url(#arr)"/><text x="193" y="52">apply</text>
              <path d="M390,62 L496,62" marker-end="url(#arr)"/><text x="443" y="52">build</text>
              <path d="M565,94 L565,196" marker-end="url(#arr)"/><text x="575" y="150" class="left">submit</text>
              <path d="M500,232 L394,232" marker-end="url(#arr)"/><text x="447" y="222">status</text>
              <path d="M250,232 L144,232" marker-end="url(#arr)"/><text x="197" y="222">finish</text>
              <path d="M320,200 L320,108" marker-end="url(#arr)"/><text x="330" y="160" class="left">record</text>
            </g>
          </svg>
        </figure>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="d-flex flex-wrap justify-content-between align-items-end mb-4 gap-2">
      <div>
        <h2 class="section-title mb-1">Ecosystem</h2>
        <p class="text-muted mb-0">Maintained integrations with widely used gravitational-wave codes, and community plugins beyond them.</p>
      </div>
      <a href="{{ '/plugins/' | relative_url }}" class="btn btn-outline-primary">All {{ plugins.size }} plugins →</a>
    </div>
    <div class="row g-3">
      {% for p in featured %}
      <div class="col-md-6 col-lg-4">
        <a class="card h-100 registry-card text-decoration-none" href="{{ '/plugins/' | append: p.slug | append: '/' | relative_url }}">
          <div class="card-body">
            <h3 class="h5 card-title mb-1">{{ p.name }}</h3>
            <p class="small text-uppercase text-muted fw-semibold mb-2">{{ p.category_label }}</p>
            <p class="mb-0 text-body">{{ p.summary }}</p>
          </div>
        </a>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-6">
        <h2 class="h3 fw-bold mb-3">Learn</h2>
        <ul class="list-unstyled learn-list">
          <li><a href="{{ '/tutorials/09-gw150914-quickstart/' | relative_url }}">Analyse GW150914</a><span>set up a project and run a complete analysis</span></li>
          <li><a href="https://asimov.docs.ligo.org/asimov/">Documentation</a><span>user guide, blueprint reference and API</span></li>
          <li><a href="{{ '/features' | relative_url }}">Features</a><span>what asimov does, in more detail</span></li>
        </ul>
      </div>
      <div class="col-lg-6">
        <h2 class="h3 fw-bold mb-3">Cite</h2>
        <p class="text-muted">If asimov contributes to your research, please cite:</p>
        <blockquote class="cite-block">
          Williams, D., Veitch, J., Chiofalo, M., Schmidt, P., Udall, R., Vajpeyi, A., &amp; Hoy, C. (2023).
          Asimov: A framework for coordinating parameter estimation workflows.
          <em>The Journal of Open Source Software</em>, 8(84), 4170.
          <a href="https://doi.org/10.21105/joss.04170">doi:10.21105/joss.04170</a>
        </blockquote>
        <a href="{{ '/citing' | relative_url }}">BibTeX and software DOIs →</a>
      </div>
    </div>
  </div>
</section>
