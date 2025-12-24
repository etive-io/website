---
layout: default
title: "Tutorials"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Tutorials & Examples</h1>
        <p class="lead text-muted">Learn how to use asimov and its ecosystem with step-by-step tutorials and practical examples.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Getting Started</h2>
        
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">Installing asimov</h3>
            <p class="text-muted">Learn how to install asimov and set up your analysis environment.</p>
            <div class="mt-3">
              <pre><code>pip install asimov</code></pre>
            </div>
            <p class="mt-3">For more detailed installation instructions, including development installations and dependencies, see the <a href="{{ "/documentation" | relative_url }}">documentation</a>.</p>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">Your First Analysis</h3>
            <p class="text-muted">A step-by-step guide to running your first gravitational-wave parameter estimation with asimov.</p>
            <p>Coming soon! This tutorial will walk you through:</p>
            <ul>
              <li>Setting up a basic analysis configuration</li>
              <li>Selecting a pipeline (bilby, PyCBC, etc.)</li>
              <li>Running the analysis</li>
              <li>Interpreting the results</li>
            </ul>
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
        <h2 class="h3 fw-bold mb-4">Pipeline-Specific Tutorials</h2>
        
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">Using asimov with bilby</h3>
            <p class="text-muted">Learn how to configure and run analyses using the bilby inference library.</p>
            <p>Topics covered:</p>
            <ul>
              <li>bilby configuration options</li>
              <li>Prior selection and customization</li>
              <li>Sampler settings</li>
              <li>Result visualization</li>
            </ul>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">Using asimov with PyCBC</h3>
            <p class="text-muted">Interface with PyCBC through asimov-pycbc for parameter estimation.</p>
            <p>Learn about:</p>
            <ul>
              <li>Installing and configuring asimov-pycbc</li>
              <li>PyCBC-specific settings</li>
              <li>Working with PyCBC templates</li>
              <li>Post-processing results</li>
            </ul>
            <p class="mt-3"><a href="https://github.com/etive-io/asimov-pycbc" target="_blank">View asimov-pycbc on GitHub →</a></p>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">Using asimov with cogwheel</h3>
            <p class="text-muted">Leverage cogwheel's efficient likelihood calculations through asimov.</p>
            <p>Learn about:</p>
            <ul>
              <li>Installing and configuring asimov-cogwheel</li>
              <li>cogwheel's relative binning approach</li>
              <li>Optimizing performance</li>
              <li>Interpreting results</li>
            </ul>
            <p class="mt-3"><a href="https://github.com/etive-io/asimov-cogwheel" target="_blank">View asimov-cogwheel on GitHub →</a></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Advanced Topics</h2>
        
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">Managing Data with asimov-gwdata</h3>
            <p class="text-muted">Efficiently handle gravitational-wave data in your analyses.</p>
            <p>Topics:</p>
            <ul>
              <li>Data discovery and download</li>
              <li>Data quality checks</li>
              <li>Cache management</li>
              <li>Working with strain data</li>
            </ul>
            <p class="mt-3"><a href="https://github.com/etive-io/asimov-gwdata" target="_blank">View asimov-gwdata on GitHub →</a></p>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">Reproducible Workflows</h3>
            <p class="text-muted">Best practices for creating reproducible gravitational-wave analyses.</p>
            <p>Learn about:</p>
            <ul>
              <li>Version control for analysis configurations</li>
              <li>Environment management</li>
              <li>Documentation standards</li>
              <li>Sharing results and code</li>
            </ul>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h3 class="h5 card-title">Comparing Pipeline Results</h3>
            <p class="text-muted">Use asimov to run the same analysis across multiple pipelines and compare results.</p>
            <p>Topics:</p>
            <ul>
              <li>Setting up multi-pipeline analyses</li>
              <li>Standardizing configurations</li>
              <li>Result comparison tools</li>
              <li>Understanding systematic differences</li>
            </ul>
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
        <h2 class="h3 fw-bold mb-3">Need Help?</h2>
        <p class="lead text-muted mb-4">Can't find what you're looking for? Check out the documentation or reach out to the community.</p>
        <div>
          <a href="{{ "/documentation" | relative_url }}" class="btn btn-primary me-2">Documentation</a>
          <a href="{{ "/contributing" | relative_url }}" class="btn btn-outline-primary">Contributing Guide</a>
        </div>
      </div>
    </div>
  </div>
</section>
