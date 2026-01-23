---
layout: default
title: "Research Impact"
---

<!-- Hero Section -->
<section class="hero">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-8 mx-auto text-center">
        <h1>Research Impact</h1>
        <p class="lead">Discover the scientific research powered by asimov</p>
      </div>
    </div>
  </div>
</section>

<!-- Impact Stats -->
<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title text-center mb-5">Citations & Reach</h2>
        
        <div class="row g-4 text-center">
          <div class="col-md-3">
            <div class="card h-100 border-0 shadow-sm">
              <div class="card-body">
                <h3 class="display-5 fw-bold text-primary" id="citation-count">—</h3>
                <p class="text-muted">Papers Citing asimov</p>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card h-100 border-0 shadow-sm">
              <div class="card-body">
                <h3 class="display-5 fw-bold text-primary" id="paper-count">—</h3>
                <p class="text-muted">Research Articles</p>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card h-100 border-0 shadow-sm">
              <div class="card-body">
                <h3 class="display-5 fw-bold text-primary" id="year-count">—</h3>
                <p class="text-muted">Years of Citations</p>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card h-100 border-0 shadow-sm">
              <div class="card-body">
                <h3 class="display-5 fw-bold text-primary" id="domain-count">—</h3>
                <p class="text-muted">Research Domains</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Citing Papers -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title mb-4">Papers Citing asimov</h2>
        
        <div class="row mb-4">
          <div class="col-md-8">
            <div class="input-group">
              <input type="text" class="form-control" id="search-papers" placeholder="Search papers, authors, keywords...">
              <button class="btn btn-outline-secondary" type="button">Search</button>
            </div>
          </div>
          <div class="col-md-4">
            <select class="form-select" id="sort-papers">
              <option value="recent">Most Recent</option>
              <option value="title">Title (A-Z)</option>
              <option value="citations">Most Cited</option>
            </select>
          </div>
        </div>
        
        <div id="papers-list" style="min-height: 200px;">
          <p class="text-muted text-center"><em>Loading papers from NASA ADS...</em></p>
        </div>
        
        <div class="row mt-5">
          <div class="col-12 text-center">
            <p class="text-muted mb-3">View all citations on NASA ADS:</p>
            <a href="https://ui.adsabs.harvard.edu/abs/2023JOSS....8.4170W/citations" target="_blank" class="btn btn-outline-primary">
              NASA ADS Citations Page →
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Research Domains -->
<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title text-center mb-5">Research Domains Using asimov</h2>
        
        <div class="row g-4" id="domains-list">
          <p class="text-muted text-center">Loading domain information...</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Latest Papers -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title mb-4">Latest Publications</h2>
        
        <div id="latest-papers" style="min-height: 300px;">
          <p class="text-muted text-center"><em>Loading latest papers...</em></p>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
// Load citing papers from data file
let allPapers = [];

fetch('{{ site.baseurl }}/data/citing-papers.json')
  .then(response => response.json())
  .then(data => {
    allPapers = data.papers || [];
    
    // Update stats
    document.getElementById('citation-count').textContent = data.total_citations || allPapers.length;
    document.getElementById('paper-count').textContent = allPapers.length;
    
    if (allPapers.length > 0) {
      // Calculate year range
      const years = allPapers
        .map(p => parseInt(p.year || 0))
        .filter(y => y > 0)
        .sort((a, b) => a - b);
      const yearRange = years.length > 0 ? years[years.length - 1] - years[0] : 0;
      document.getElementById('year-count').textContent = yearRange;
      
      // Count domains
      const domains = new Set(allPapers.map(p => p.domain).filter(d => d));
      document.getElementById('domain-count').textContent = domains.size;
    }
    
    displayPapers(allPapers.slice(0, 10));
    displayLatestPapers(allPapers.slice(0, 5));
    displayDomains(allPapers);
  })
  .catch(error => {
    console.log('Could not load papers:', error);
    document.getElementById('papers-list').innerHTML = '<p class="text-muted text-center">Check <a href="https://ui.adsabs.harvard.edu/abs/2023JOSS....8.4170W/citations" target="_blank">NASA ADS →</a></p>';
  });

function displayPapers(papers) {
  const container = document.getElementById('papers-list');
  
  if (papers.length === 0) {
    container.innerHTML = '<p class="text-muted text-center">No papers found</p>';
    return;
  }
  
  let html = '<div class="list-group">';
  papers.forEach(paper => {
    const year = paper.year || 'n/a';
    const authors = paper.authors ? paper.authors.split(';')[0] + ' et al.' : 'Unknown';
    
    html += `
      <a href="${paper.url}" target="_blank" class="list-group-item list-group-item-action">
        <div class="d-flex w-100 justify-content-between">
          <h6 class="mb-1">${paper.title || 'Untitled'}</h6>
          <small class="text-muted">${year}</small>
        </div>
        <p class="mb-1 text-muted small">${authors}</p>
        <small class="text-muted">${paper.journal || 'Unknown Journal'}</small>
      </a>
    `;
  });
  html += '</div>';
  container.innerHTML = html;
}

function displayLatestPapers(papers) {
  const container = document.getElementById('latest-papers');
  
  if (papers.length === 0) {
    container.innerHTML = '<p class="text-muted text-center">No papers available</p>';
    return;
  }
  
  let html = '<div class="row g-4">';
  papers.forEach(paper => {
    const year = paper.year || 'n/a';
    const abstract = paper.abstract ? paper.abstract.substring(0, 150) + '...' : 'No abstract available';
    
    html += `
      <div class="col-md-6 col-lg-4">
        <div class="card h-100">
          <div class="card-body">
            <h6 class="card-title"><a href="${paper.url}" target="_blank" class="text-decoration-none">${paper.title || 'Untitled'}</a></h6>
            <p class="card-text text-muted small">${abstract}</p>
            <small class="text-muted">
              <strong>${year}</strong> • ${paper.journal || 'Journal'}
            </small>
          </div>
        </div>
      </div>
    `;
  });
  html += '</div>';
  container.innerHTML = html;
}

function displayDomains(papers) {
  const container = document.getElementById('domains-list');
  
  const domainCounts = {};
  papers.forEach(p => {
    if (p.domain) {
      domainCounts[p.domain] = (domainCounts[p.domain] || 0) + 1;
    }
  });
  
  if (Object.keys(domainCounts).length === 0) {
    container.innerHTML = '<p class="text-muted text-center">Domain information not available</p>';
    return;
  }
  
  let html = '';
  Object.entries(domainCounts).forEach(([domain, count]) => {
    const percentage = Math.round((count / papers.length) * 100);
    html += `
      <div class="col-md-6 col-lg-4">
        <div class="card">
          <div class="card-body">
            <h6 class="card-title">${domain}</h6>
            <div class="progress">
              <div class="progress-bar" style="width: ${percentage}%"></div>
            </div>
            <small class="text-muted">${count} papers (${percentage}%)</small>
          </div>
        </div>
      </div>
    `;
  });
  container.innerHTML = html;
}

// Search functionality
document.getElementById('search-papers')?.addEventListener('keyup', (e) => {
  const query = e.target.value.toLowerCase();
  const filtered = allPapers.filter(p => 
    p.title?.toLowerCase().includes(query) ||
    p.authors?.toLowerCase().includes(query) ||
    p.abstract?.toLowerCase().includes(query)
  );
  displayPapers(filtered.slice(0, 10));
});

// Sort functionality
document.getElementById('sort-papers')?.addEventListener('change', (e) => {
  let sorted = [...allPapers];
  
  switch(e.target.value) {
    case 'title':
      sorted.sort((a, b) => (a.title || '').localeCompare(b.title || ''));
      break;
    case 'citations':
      sorted.sort((a, b) => (b.citation_count || 0) - (a.citation_count || 0));
      break;
    case 'recent':
    default:
      sorted.sort((a, b) => parseInt(b.year || 0) - parseInt(a.year || 0));
  }
  
  displayPapers(sorted.slice(0, 10));
});
</script>
