---
layout: default
title: "Releases"
description: "Latest versions of asimov and its plugins, read from PyPI and each repository."
---
{% assign registry = site.data.registry %}
{% assign released = registry.packages | where_exp: "p", "p.latest_version" | sort: "latest_released", "first" | reverse %}
{% assign unreleased = registry.packages | where_exp: "p", "p.latest_version == nil" | sort_natural: "name" %}

<section class="section pb-3">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h1 class="section-title">Releases</h1>
        <p class="lead text-muted">
          Current versions of asimov and every package in the <a href="{{ '/plugins/' | relative_url }}">plugin registry</a>,
          most recent first. Versions come from PyPI, falling back to the repository's releases.
        </p>
        <p class="small text-muted mb-0">Last refreshed {{ registry.generated_at }}.</p>
      </div>
    </div>
  </div>
</section>

<section class="section pt-0">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <div class="table-responsive">
          <table class="table align-middle releases-table">
            <thead>
              <tr><th>Package</th><th>Latest</th><th>Released</th><th>Recent releases</th><th>Get it</th></tr>
            </thead>
            <tbody>
              {% for p in released %}
              <tr{% if p.category == "core" %} class="table-primary"{% endif %}>
                <td>
                  {% if p.category == "core" %}<a href="{{ p.repo_url }}" class="fw-semibold">{{ p.name }}</a>
                  {% else %}<a href="{{ '/plugins/' | append: p.slug | append: '/' | relative_url }}" class="fw-semibold">{{ p.name }}</a>{% endif %}
                  <div class="small text-muted">{{ p.category_label }}</div>
                </td>
                <td><code>{{ p.latest_version }}</code></td>
                <td class="text-nowrap small">{{ p.latest_released | default: "—" }}</td>
                <td class="small">
                  {% for r in p.source.releases limit: 3 %}
                  <a href="{{ r.url }}">{{ r.version }}</a>{% if r.prerelease %} <span class="badge text-bg-light border">pre-release</span>{% endif %}{% unless forloop.last %}, {% endunless %}
                  {% else %}<span class="text-muted">—</span>
                  {% endfor %}
                </td>
                <td class="small text-nowrap">
                  {% if p.pypi %}<a href="{{ p.pypi.url }}">PyPI</a>{% endif %}
                  {% if p.conda %} · <a href="{{ p.conda.url }}">conda-forge</a>{% endif %}
                </td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>

        {% if unreleased.size > 0 %}
        <h2 class="h5 fw-bold mt-5">Installed from source</h2>
        <p class="small text-muted">These packages have no published release yet; install them from their repositories.</p>
        <ul class="small">
          {% for p in unreleased %}
          <li><a href="{{ '/plugins/' | append: p.slug | append: '/' | relative_url }}">{{ p.name }}</a> <code>{{ p.install }}</code></li>
          {% endfor %}
        </ul>
        {% endif %}

        <h2 class="h5 fw-bold mt-5">Following releases</h2>
        <p class="small text-muted mb-1">
          Each repository publishes release notes on its releases page, and GitHub's <em>Watch → Custom → Releases</em>
          option will notify you of new ones. asimov's own changes are described in its
          <a href="https://github.com/etive-io/asimov/blob/main/CHANGELOG.rst">changelog</a>, and every asimov release is
          archived on <a href="https://doi.org/10.5281/zenodo.4024432">Zenodo</a> with its own DOI.
        </p>
      </div>
    </div>
  </div>
</section>
