---
layout: default
title: "Statistics"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h1 class="section-title">Package Statistics</h1>
        <p class="lead text-muted">Download and usage statistics for asimov and the asimov ecosystem. Stats are updated weekly from <a href="https://pypi.org/">PyPI</a> and <a href="https://conda-forge.org/">conda-forge</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <div class="table-responsive">
          <table class="table table-hover">
            <thead class="table-light">
              <tr>
                <th>Package</th>
                <th class="text-center">⭐ Stars</th>
                <th class="text-center">Latest Release</th>
                <th class="text-center">PyPI (Weekly)</th>
                <th class="text-center">PyPI (Monthly)</th>
                <th class="text-center">conda-forge</th>
              </tr>
            </thead>
            <tbody>
              {% for package in site.data.package-stats %}
              <tr>
                <td>
                  <a href="https://github.com/{{ package.github_repo }}" target="_blank" rel="noopener noreferrer">
                    <strong>{{ package.name }}</strong>
                  </a>
                </td>
                <td class="text-center">
                  <span class="badge bg-warning text-dark">{{ package.github_stars }}</span>
                </td>
                <td class="text-center small">
                  {% if package.latest_release %}
                    <a href="https://github.com/{{ package.github_repo }}/releases/tag/{{ package.latest_release }}" target="_blank" rel="noopener noreferrer">
                      {{ package.latest_release }}
                    </a>
                    <br>
                    <span class="text-muted">{% assign release_date = package.release_date | date: "%Y-%m-%d" %}{{ release_date }}</span>
                  {% else %}
                    <span class="text-muted">—</span>
                  {% endif %}
                </td>
                <td class="text-center">
                  <span class="badge bg-info">{{ package.pypi_downloads_week | default: 0 }}</span>
                </td>
                <td class="text-center">
                  <span class="badge bg-primary">{{ package.pypi_downloads_month | default: 0 }}</span>
                </td>
                <td class="text-center">
                  <span class="badge bg-secondary">{{ package.conda_forge_downloads_month | default: 0 }}</span>
                </td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
        
        <div class="alert alert-info mt-4" role="alert">
          <strong>Note:</strong> PyPI statistics are powered by <a href="https://pepy.tech/">pepy.tech</a>. conda-forge statistics reflect total downloads from the conda-forge repository. Data is updated weekly via <a href="https://github.com/etive-io/website/blob/master/.github/workflows/update-stats.yml">GitHub Actions</a>.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="h3 fw-bold mb-4">What Do These Numbers Mean?</h2>
        
        <div class="row">
          <div class="col-md-4">
            <h4 class="fw-bold mb-2">⭐ GitHub Stars</h4>
            <p>Number of GitHub stars for each repository. A good indicator of community interest and project visibility.</p>
          </div>
          
          <div class="col-md-4">
            <h4 class="fw-bold mb-2">📦 PyPI Downloads</h4>
            <p>Number of times packages were downloaded from the Python Package Index (PyPI) using pip. This reflects direct installation activity and is a good indicator of adoption.</p>
            <ul class="small">
              <li><strong>Weekly:</strong> Last 7 days</li>
              <li><strong>Monthly:</strong> Last 30 days</li>
            </ul>
          </div>
          
          <div class="col-md-4">
            <h4 class="fw-bold mb-2">🌾 conda-forge</h4>
            <p>Number of times packages were downloaded from conda-forge, an alternative package distribution channel commonly used in scientific computing.</p>
          </div>
        </div>
        
        <div class="row mt-4">
          <div class="col-12">
            <h4 class="fw-bold mb-2">🚀 Latest Release</h4>
            <p>The most recent release tag and publication date for each pipeline package. For the core asimov package, check GitHub releases for the latest updates.</p>
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
        <h2 class="h3 fw-bold mb-4">How to Install</h2>
        
        <div class="row">
          <div class="col-md-6">
            <h5 class="fw-bold mb-3">Using pip (PyPI)</h5>
            <pre><code>pip install asimov</code></pre>
          </div>
          
          <div class="col-md-6">
            <h5 class="fw-bold mb-3">Using conda (conda-forge)</h5>
            <pre><code>conda install -c conda-forge asimov</code></pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
