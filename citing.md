---
layout: default
title: "Citing"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Citing asimov</h1>
        <p class="lead text-muted">How to properly cite asimov and related packages in your research.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Citing asimov</h2>
        
        <p class="text-muted mb-4">If you use asimov in your research, please cite the original paper which describes asimov:</p>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title mb-3">Journal Article</h5>
            <p class="text-muted mb-3">
              Williams, D., Veitch, J., Chiofalo, M., Schmidt, P., Udall, R., Vajpeyi, A., & Hoy, C. (2023). 
              "Asimov: A framework for coordinating parameter estimation workflows". 
              <em>The Journal of Open Source Software</em>, 8(84), 4170. 
              <a href="https://doi.org/10.21105/joss.04170" target="_blank">https://doi.org/10.21105/joss.04170</a>
            </p>
            
            <h6 class="fw-bold mt-4 mb-2">BibTeX Citation</h6>
            <pre><code>@article{asimov-paper,
  author = {Williams, Daniel and Veitch, John and Chiofalo, Maria and Schmidt, Patricia and Udall, Rhiannon and Vajpeyi, Avi and Hoy, Charlie},
  title = {Asimov: A framework for coordinating parameter estimation workflows},
  journal = {The Journal of Open Source Software},
  year = {2023},
  month = {apr},
  volume = {8},
  number = {84},
  eid = {4170},
  pages = {4170},
  doi = {10.21105/joss.04170},
  archiveprefix = {arXiv},
  eprint = {2207.01468},
  primaryclass = {gr-qc}
}</code></pre>
          </div>
        </div>
        
        <h2 class="h3 fw-bold mb-4 mt-5">Citing Specific Software Versions</h2>
        
        <p class="text-muted mb-4">Each release of asimov is archived on Zenodo and receives a unique DOI. When you use a specific version of asimov, you should cite both the paper above and the corresponding Zenodo release.</p>
        
        <div class="card mb-4">
          <div class="card-body">
            <h6 class="fw-bold mb-2">Latest Releases</h6>
            <div id="zenodo-releases" style="margin-top: 1rem;">
              <p class="text-muted"><em>Loading latest releases from Zenodo...</em></p>
            </div>
            <p class="text-muted mt-3 mb-0"><small><a href="https://doi.org/10.5281/zenodo.4024432" target="_blank">View all releases on Zenodo →</a></small></p>
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
        <h2 class="h3 fw-bold mb-4">Citing Analysis Pipelines</h2>
        
        <p class="text-muted mb-4">When using asimov with specific analysis pipelines, you should also cite those pipelines. Below are citation guidelines for the main supported pipelines:</p>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">bilby</h5>
            <p class="text-muted">If you use bilby through asimov, please cite:</p>
            <pre><code>@article{bilby,
  title={BILBY: A user-friendly Bayesian inference library for gravitational-wave astronomy},
  author={Ashton, Gregory and others},
  journal={The Astrophysical Journal Supplement Series},
  volume={241},
  number={2},
  pages={27},
  year={2019},
  publisher={IOP Publishing}
}</code></pre>
            <a href="https://lscsoft.docs.ligo.org/bilby/" target="_blank" class="btn btn-outline-primary btn-sm mt-2">Visit bilby documentation</a>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">PyCBC</h5>
            <p class="text-muted">If you use PyCBC through asimov-pycbc, please cite:</p>
            <pre><code>@article{pycbc,
  title={PyCBC Inference: A Python-based parameter estimation toolkit for compact binary coalescence signals},
  author={Biwer, C. M. and others},
  journal={Publications of the Astronomical Society of the Pacific},
  volume={131},
  number={996},
  pages={024503},
  year={2019}
}</code></pre>
            <a href="https://pycbc.org/" target="_blank" class="btn btn-outline-primary btn-sm mt-2">Visit PyCBC documentation</a>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">cogwheel</h5>
            <p class="text-muted">If you use cogwheel through asimov-cogwheel, please cite:</p>
            <pre><code>@article{cogwheel,
  title={Rapid localization of gravitational wave sources with likelihood reweighting},
  author={Roulet, Javier and others},
  journal={Physical Review D},
  volume={104},
  pages={083010},
  year={2021}
}</code></pre>
            <a href="https://github.com/jroulet/cogwheel" target="_blank" class="btn btn-outline-primary btn-sm mt-2">Visit cogwheel repository</a>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">LALInference</h5>
            <p class="text-muted">If you use LALInference, please cite:</p>
            <pre><code>@article{lalinference,
  title={Parameter estimation for compact binaries with ground-based gravitational-wave observations using the LALInference software library},
  author={Veitch, J. and others},
  journal={Physical Review D},
  volume={91},
  pages={042003},
  year={2015}
}</code></pre>
            <a href="https://lscsoft.docs.ligo.org/lalsuite/" target="_blank" class="btn btn-outline-primary btn-sm mt-2">Visit LALSuite documentation</a>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">BayesWave</h5>
            <p class="text-muted">If you use BayesWave, please cite:</p>
            <pre><code>@article{bayeswave,
  title={BayesWave: Bayesian Inference for Gravitational Wave Bursts and Instrument Glitches},
  author={Cornish, Neil J. and Littenberg, Tyson B.},
  journal={Classical and Quantum Gravity},
  volume={32},
  pages={135012},
  year={2015}
}</code></pre>
            <a href="https://git.ligo.org/lscsoft/bayeswave" target="_blank" class="btn btn-outline-primary btn-sm mt-2">Visit BayesWave repository</a>
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
        <h2 class="h3 fw-bold mb-4">Acknowledgments</h2>
        
        <p class="text-muted mb-3">In addition to citations, consider including an acknowledgment in your paper. Here's a suggested template:</p>
        
        <div class="card">
          <div class="card-body">
            <p class="mb-0"><em>"This research has made use of asimov [cite], a framework for managing gravitational-wave parameter estimation analyses. The analysis was performed using [pipeline name] [cite]."</em></p>
          </div>
        </div>
        
        <p class="text-muted mt-4">If asimov was particularly important to your research, you may also want to acknowledge specific contributors or features that were crucial to your work.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Software Metadata</h2>
        
        <p class="text-muted mb-4">For enhanced reproducibility and proper attribution, consider including the following information in your methodology section:</p>
        
        <ul>
          <li>Specific version numbers of asimov and all pipeline packages used</li>
          <li>DOI references for archived versions (when available through Zenodo)</li>
          <li>Links to configuration files or analysis scripts (e.g., via GitHub repository)</li>
          <li>System requirements and computational resources used</li>
        </ul>
        
        <p class="text-muted mt-4">This information helps other researchers reproduce your analysis and understand the computational context of your results.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto text-center">
        <h2 class="h3 fw-bold mb-3">Questions about Citations?</h2>
        <p class="lead text-muted mb-4">If you have questions about how to cite asimov or related software, please reach out to the community or check the documentation.</p>
        <div>
          <a href="{{ "/documentation" | relative_url }}" class="btn btn-primary me-2">Documentation</a>
          <a href="https://github.com/etive-io" target="_blank" class="btn btn-outline-primary">GitHub</a>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
// Load Zenodo releases for asimov
fetch('{{ site.baseurl }}/data/zenodo-releases.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('zenodo-releases');
    if (data.releases && data.releases.length > 0) {
      let html = '<ul style="list-style: none; padding: 0;">';
      data.releases.slice(0, 5).forEach(release => {
        html += `
          <li style="margin-bottom: 1rem;">
            <strong><a href="${release.links.html}" target="_blank">${release.title}</a></strong><br>
            <small class="text-muted">DOI: <a href="https://doi.org/${release.doi}" target="_blank">${release.doi}</a></small><br>
            <small class="text-muted">Published: ${new Date(release.created).toLocaleDateString()}</small>
          </li>
        `;
      });
      html += '</ul>';
      container.innerHTML = html;
    } else {
      container.innerHTML = '<p class="text-muted">Check <a href="https://doi.org/10.5281/zenodo.4024432" target="_blank">Zenodo for all releases →</a></p>';
    }
  })
  .catch(error => {
    console.log('Could not load Zenodo data:', error);
    document.getElementById('zenodo-releases').innerHTML = '<p class="text-muted">Check <a href="https://doi.org/10.5281/zenodo.4024432" target="_blank">Zenodo for all releases →</a></p>';
  });
</script>
