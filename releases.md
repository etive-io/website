---
layout: default
title: "Releases"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Release Announcements</h1>
        <p class="lead text-muted">Latest releases and updates from the asimov ecosystem.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Recent Releases</h2>
        
        <div class="alert alert-info">
          <strong>Note:</strong> Release information is automatically tracked through GitHub. Visit each package's repository to view the latest releases and changelogs.
        </div>
        
        {% for project in site.data.projects.core_projects %}
        <div class="card mb-4 release-card">
          <div class="card-body">
            <h3 class="h5 fw-bold">{{ project.name }}</h3>
            <p class="text-muted mb-3">{{ project.short_description }}</p>
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <a href="{{ project.github_url }}/releases" target="_blank" class="btn btn-primary btn-sm">View Releases</a>
                <a href="{{ project.github_url }}/blob/master/CHANGELOG.md" target="_blank" class="btn btn-outline-secondary btn-sm">Changelog</a>
              </div>
            </div>
          </div>
        </div>
        {% endfor %}
        
        {% for project in site.data.projects.pipeline_interfaces %}
        <div class="card mb-4 release-card">
          <div class="card-body">
            <h3 class="h5 fw-bold">{{ project.name }}</h3>
            <p class="text-muted mb-3">{{ project.short_description }}</p>
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <a href="{{ project.github_url }}/releases" target="_blank" class="btn btn-primary btn-sm">View Releases</a>
                <a href="{{ project.github_url }}/blob/master/CHANGELOG.md" target="_blank" class="btn btn-outline-secondary btn-sm">Changelog</a>
              </div>
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
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Release Policy</h2>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Versioning</h5>
            <p class="text-muted mb-0">All packages in the asimov ecosystem follow <a href="https://semver.org/" target="_blank">Semantic Versioning</a> (SemVer). Version numbers follow the format MAJOR.MINOR.PATCH:</p>
            <ul class="mt-2 mb-0">
              <li><strong>MAJOR</strong>: Incompatible API changes</li>
              <li><strong>MINOR</strong>: Backwards-compatible new features</li>
              <li><strong>PATCH</strong>: Backwards-compatible bug fixes</li>
            </ul>
          </div>
        </div>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Changelogs</h5>
            <p class="text-muted mb-0">Each package maintains a detailed changelog documenting all notable changes between versions. Changelogs follow the <a href="https://keepachangelog.com/" target="_blank">Keep a Changelog</a> format.</p>
          </div>
        </div>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Release Notes</h5>
            <p class="text-muted mb-0">Detailed release notes are published on GitHub for each release, including highlights of new features, bug fixes, and breaking changes.</p>
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
        <h2 class="h3 fw-bold mb-4">Stay Informed</h2>
        <p class="text-muted mb-4">There are several ways to stay up-to-date with new releases:</p>
        
        <div class="row g-3">
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">Watch on GitHub</h5>
                <p class="text-muted">Click "Watch" on any repository to receive notifications about new releases.</p>
                <a href="https://github.com/etive-io" target="_blank" class="btn btn-outline-primary btn-sm">Visit GitHub</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">RSS Feeds</h5>
                <p class="text-muted">Subscribe to GitHub's release feeds for each package to get updates in your feed reader.</p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">Blog</h5>
                <p class="text-muted">Major releases are announced on our blog with detailed information about new features.</p>
                <a href="{{ "/blog" | relative_url }}" class="btn btn-outline-primary btn-sm">Visit Blog</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">PyPI</h5>
                <p class="text-muted">All packages are published on PyPI. You can track new versions through PyPI notifications.</p>
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
      <div class="col-lg-8 mx-auto text-center">
        <h2 class="h3 fw-bold mb-3">Questions about a Release?</h2>
        <p class="lead text-muted mb-4">If you have questions or issues with a specific release, please open an issue on the respective GitHub repository.</p>
        <a href="https://github.com/etive-io" target="_blank" class="btn btn-primary">View Repositories</a>
      </div>
    </div>
  </div>
</section>
