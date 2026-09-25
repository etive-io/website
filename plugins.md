---
layout: default
title: "Plugins"
description: "Pipelines, hooks and integrations that extend asimov, built from each package's own metadata."
---
{% assign registry = site.data.registry %}
{% assign packages = registry.packages | where_exp: "p", "p.category != 'core'" %}

<section class="section pb-3">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h1 class="section-title">Plugin registry</h1>
        <p class="lead text-muted">
          asimov itself contains no analysis code. Pipelines, data sources and service
          integrations are separate Python packages that register themselves through
          <a href="https://packaging.python.org/en/latest/specifications/entry-points/">entry points</a>.
          Once a package is installed, its pipelines can be named in a blueprint.
        </p>
        <p class="text-muted small mb-0">
          {{ packages.size }} packages. Versions, entry points and descriptions are read from PyPI and from each
          repository when the site is built (last refreshed {{ registry.generated_at }}).
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section pt-0">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">

        <div class="registry-controls mb-4">
          <label for="registry-search" class="visually-hidden">Search plugins</label>
          <input id="registry-search" type="search" class="form-control form-control-lg mb-3"
                 placeholder="Search by name, description or pipeline name…" autocomplete="off">

          <div class="d-flex flex-wrap gap-2 mb-2" role="group" aria-label="Filter by category">
            <button type="button" class="btn btn-sm btn-outline-secondary active" data-filter="category" data-value="">All</button>
            {% for c in registry.categories %}
              {% assign n = packages | where: "category", c.id | size %}
              {% if n > 0 %}
              <button type="button" class="btn btn-sm btn-outline-secondary" data-filter="category" data-value="{{ c.id }}">{{ c.label }} <span class="opacity-75">{{ n }}</span></button>
              {% endif %}
            {% endfor %}
          </div>

          <div class="d-flex flex-wrap align-items-center gap-3 small text-muted">
            <label>Provides
              <select class="form-select form-select-sm d-inline-block w-auto ms-1" data-filter="provides">
                <option value="">anything</option>
                {% for g in registry.entry_point_groups %}
                <option value="{{ g[0] }}">{{ g[1] | downcase }}</option>
                {% endfor %}
              </select>
            </label>
            <label class="form-check-label"><input type="checkbox" class="form-check-input me-1" data-filter="official">Maintained by the asimov team</label>
            <label class="form-check-label"><input type="checkbox" class="form-check-input me-1" data-filter="pypi">On PyPI</label>
            <label class="form-check-label"><input type="checkbox" class="form-check-input me-1" data-filter="deprecated">Show deprecated</label>
          </div>
        </div>

        <div id="registry-list" class="row g-3">
          {% for c in registry.categories %}
          {% assign group = packages | where: "category", c.id | sort_natural: "name" %}
          {% for p in group %}
          {% capture provides %}{% for ep in p.entry_points %}{{ ep.group }} {% endfor %}{% endcapture %}
          {% capture ep_names %}{% for ep in p.entry_points %}{{ ep.names | join: " " }} {% endfor %}{% endcapture %}
          <div class="col-md-6 registry-item"
               data-category="{{ c.id }}"
               data-provides="{{ provides | strip }}"
               data-official="{% if p.maintenance == 'official' %}1{% endif %}"
               data-pypi="{% if p.pypi %}1{% endif %}"
               data-deprecated="{% if p.deprecated %}1{% endif %}"
               data-text="{{ p.name | downcase | escape }} {{ p.summary | downcase | escape }} {{ ep_names | downcase }} {{ p.source.topics | join: ' ' | escape }}">
            <a class="card h-100 registry-card text-decoration-none" href="{{ '/plugins/' | append: p.slug | append: '/' | relative_url }}">
              <div class="card-body">
                <div class="d-flex justify-content-between align-items-start gap-2 mb-1">
                  <h2 class="h5 card-title mb-0">{{ p.name }}</h2>
                  {% if p.latest_version %}<span class="small text-muted text-nowrap">v{{ p.latest_version | remove_first: "v" }}</span>{% endif %}
                </div>
                <p class="small text-uppercase text-muted fw-semibold mb-2">{{ c.label }}</p>
                <p class="text-body mb-3">{{ p.summary }}</p>
                <div class="d-flex flex-wrap gap-1 small">
                  {% if p.deprecated %}<span class="badge text-bg-warning">Deprecated</span>{% endif %}
                  {% if p.maintenance == "official" %}<span class="badge text-bg-primary">asimov team</span>{% endif %}
                  {% for ep in p.entry_points %}{% for n in ep.names %}<span class="badge text-bg-light border" title="{{ ep.label }}">{{ ep.label | downcase }}: {{ n }}</span>{% endfor %}{% endfor %}
                  {% unless p.pypi %}<span class="badge text-bg-light border text-muted">install from source</span>{% endunless %}
                </div>
              </div>
            </a>
          </div>
          {% endfor %}
          {% endfor %}
        </div>
        <p id="registry-empty" class="text-muted mt-4" hidden>No plugins match these filters.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light" id="add">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="h3 fw-bold mb-3">Add your plugin</h2>
        <p>
          Listing a package takes a pull request of about four lines. You don't write a page: the site
          reads your README, your PyPI metadata and your <code>asimov.*</code> entry points directly,
          so the listing updates when you release.
        </p>
        <ol class="mb-4">
          <li>Register your integration under an asimov entry-point group in <code>pyproject.toml</code>, e.g.
            <code>[project.entry-points."asimov.pipelines"]</code>. The
            <a href="https://asimov.docs.ligo.org/asimov/">asimov documentation</a> describes the
            <code>Pipeline</code> interface and the available hooks.</li>
          <li>Add the GitHub topic <code>asimov-plugin</code> to your repository so it can be found automatically.</li>
          <li>Add an entry to <a href="https://github.com/etive-io/website/blob/master/registry.yml"><code>registry.yml</code></a> and open a pull request:</li>
        </ol>
<pre><code>- name: asimov-mycode
  repo: my-org/asimov-mycode        # or a full https:// URL for GitLab
  category: parameter-estimation
</code></pre>
        <p class="small text-muted mb-0">
          A check on the pull request confirms that the repository can be reached and exposes asimov entry points.
          The other fields are optional; they're described in the comments at the top of <code>registry.yml</code>.
          Prefer not to open a pull request? <a href="https://github.com/etive-io/website/issues/new?template=plugin-submission.yml">Request a listing</a> instead.
        </p>
      </div>
    </div>
  </div>
</section>

<script>
(function () {
  const items = Array.from(document.querySelectorAll('.registry-item'));
  const search = document.getElementById('registry-search');
  const empty = document.getElementById('registry-empty');
  const flags = ['official', 'pypi', 'deprecated'];
  const state = { q: '', category: '', provides: '', official: false, pypi: false, deprecated: false };

  function readHash() {
    const h = new URLSearchParams(location.hash.slice(1));
    state.q = h.get('q') || '';
    state.category = h.get('category') || '';
    state.provides = h.get('provides') || '';
    flags.forEach(k => state[k] = h.get(k) === '1');
  }

  function writeHash() {
    const h = new URLSearchParams();
    if (state.q) h.set('q', state.q);
    if (state.category) h.set('category', state.category);
    if (state.provides) h.set('provides', state.provides);
    flags.forEach(k => { if (state[k]) h.set(k, '1'); });
    const s = h.toString();
    history.replaceState(null, '', s ? '#' + s : location.pathname);
  }

  function sync() {
    search.value = state.q;
    document.querySelectorAll('[data-filter="category"]').forEach(b =>
      b.classList.toggle('active', b.dataset.value === state.category));
    document.querySelector('[data-filter="provides"]').value = state.provides;
    flags.forEach(k => document.querySelector(`[data-filter="${k}"]`).checked = state[k]);
  }

  function apply() {
    const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    items.forEach(el => {
      const d = el.dataset;
      const ok =
        (!state.category || d.category === state.category) &&
        (!state.provides || d.provides.split(' ').includes(state.provides)) &&
        (!state.official || d.official) &&
        (!state.pypi || d.pypi) &&
        // Deprecated packages are hidden unless asked for, or searched for by name.
        (state.deprecated || !d.deprecated || terms.length > 0) &&
        terms.every(t => d.text.includes(t));
      el.hidden = !ok;
      if (ok) shown++;
    });
    empty.hidden = shown > 0;
  }

  function update() { writeHash(); apply(); }

  search.addEventListener('input', () => { state.q = search.value.trim(); update(); });
  document.querySelectorAll('[data-filter="category"]').forEach(b => b.addEventListener('click', () => {
    state.category = b.dataset.value; sync(); update();
  }));
  document.querySelector('[data-filter="provides"]').addEventListener('change', e => { state.provides = e.target.value; update(); });
  flags.forEach(k => document.querySelector(`[data-filter="${k}"]`)
    .addEventListener('change', e => { state[k] = e.target.checked; update(); }));
  window.addEventListener('hashchange', () => { readHash(); sync(); apply(); });

  readHash(); sync(); apply();
})();
</script>
