---
layout: default
title: "Blog"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Blog</h1>
        <p class="lead text-muted">Updates, insights, and news from the asimov ecosystem.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        {% if site.posts.size > 0 %}
          {% for post in site.posts %}
            <article class="card mb-4">
              <div class="card-body">
                <h2 class="post-title">
                  <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                </h2>
                <div class="post-meta">
                  <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
                  {% if post.author %} • {{ post.author }}{% endif %}
                  {% if post.categories.size > 0 %} • {{ post.categories | join: ', ' }}{% endif %}
                </div>
                {% if post.excerpt %}
                  <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
                {% endif %}
                <a href="{{ post.url | relative_url }}" class="btn btn-outline-primary btn-sm">Read more →</a>
              </div>
            </article>
          {% endfor %}
        {% else %}
          <div class="card">
            <div class="card-body text-center py-5">
              <h3 class="h5 fw-bold mb-3">No posts yet</h3>
              <p class="text-muted">Check back soon for updates, tutorials, and insights about asimov and gravitational-wave analysis.</p>
              <p class="mt-4">In the meantime, you can:</p>
              <div class="mt-3">
                <a href="{{ "/tutorials" | relative_url }}" class="btn btn-primary me-2">Explore Tutorials</a>
                <a href="{{ "/documentation" | relative_url }}" class="btn btn-outline-primary">Read Documentation</a>
              </div>
            </div>
          </div>
        {% endif %}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h4 fw-bold mb-4">Stay Updated</h2>
        <p class="text-muted">Follow the etive.io organization on GitHub to stay up-to-date with the latest developments in the asimov ecosystem.</p>
        <div class="mt-3">
          <a href="https://github.com/etive-io" target="_blank" class="btn btn-outline-primary">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="me-2" viewBox="0 0 16 16" style="vertical-align: text-bottom;">
              <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
            </svg>
            Follow on GitHub
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
