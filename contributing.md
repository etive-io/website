---
layout: default
title: "Contributing"
---

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h1 class="section-title">Contributing to asimov</h1>
        <p class="lead text-muted">We welcome contributions from the community! Learn how you can help make gravitational-wave analysis better for everyone.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Ways to Contribute</h2>
        
        <div class="row g-4">
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">Report Bugs</h5>
                <p class="text-muted">Found a bug? Report it on GitHub Issues. Include detailed steps to reproduce, expected behavior, and system information.</p>
                <a href="https://github.com/etive-io" target="_blank" class="btn btn-outline-primary btn-sm">Report Issue</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">Suggest Features</h5>
                <p class="text-muted">Have an idea for a new feature? Open a feature request on GitHub. Describe the use case and how it would help researchers.</p>
                <a href="https://github.com/etive-io" target="_blank" class="btn btn-outline-primary btn-sm">Suggest Feature</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">Improve Documentation</h5>
                <p class="text-muted">Help make our documentation clearer, fix typos, or add examples. Good documentation is crucial for usability.</p>
                <a href="{{ "/documentation" | relative_url }}" class="btn btn-outline-primary btn-sm">View Docs</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">Write Code</h5>
                <p class="text-muted">Submit pull requests to fix bugs, add features, or improve performance. All code contributions are reviewed and tested.</p>
                <a href="https://github.com/etive-io" target="_blank" class="btn btn-outline-primary btn-sm">View Repositories</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">Add Tests</h5>
                <p class="text-muted">Improve code coverage by writing unit tests. Tests ensure reliability and make it easier to refactor code safely.</p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">Share Your Experience</h5>
                <p class="text-muted">Write tutorials, blog posts, or examples showing how you use asimov in your research.</p>
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
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Getting Started</h2>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">1. Set Up Your Development Environment</h5>
            <p class="text-muted">Fork the repository and clone it locally:</p>
            <pre><code>git clone https://github.com/YOUR_USERNAME/asimov.git
cd asimov
pip install -e .[dev]</code></pre>
            <p class="text-muted mt-3">The <code>[dev]</code> extra installs development dependencies including testing frameworks and linters.</p>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">2. Create a Branch</h5>
            <p class="text-muted">Create a new branch for your work:</p>
            <pre><code>git checkout -b feature/your-feature-name</code></pre>
            <p class="text-muted mt-3">Use descriptive branch names like <code>feature/add-new-sampler</code> or <code>bugfix/fix-config-parsing</code>.</p>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">3. Make Your Changes</h5>
            <p class="text-muted">Write your code following our coding standards:</p>
            <ul>
              <li>Follow PEP 8 style guidelines for Python code</li>
              <li>Write docstrings using the numpydoc format</li>
              <li>Add unit tests for new functionality using unittest framework</li>
              <li>Keep changes focused and atomic</li>
              <li>Write clear, descriptive commit messages</li>
            </ul>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">4. Run Tests</h5>
            <p class="text-muted">Ensure all tests pass before submitting:</p>
            <pre><code>python -m unittest discover</code></pre>
            <p class="text-muted mt-3">Run linters to check code style:</p>
            <pre><code>flake8 .
black --check .</code></pre>
          </div>
        </div>
        
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">5. Submit a Pull Request</h5>
            <p class="text-muted">Push your changes and open a pull request:</p>
            <pre><code>git push origin feature/your-feature-name</code></pre>
            <p class="text-muted mt-3">In your pull request description:</p>
            <ul>
              <li>Describe what changes you made and why</li>
              <li>Reference any related issues (e.g., "Fixes #123")</li>
              <li>Explain how you tested your changes</li>
              <li>Note any breaking changes</li>
            </ul>
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
        <h2 class="h3 fw-bold mb-4">Code Standards</h2>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Python Style</h5>
            <p class="text-muted">We follow PEP 8 conventions. Key points:</p>
            <ul class="mb-0">
              <li>Use 4 spaces for indentation (no tabs)</li>
              <li>Maximum line length of 88 characters (Black default)</li>
              <li>Use descriptive variable names</li>
              <li>Use type hints where appropriate</li>
            </ul>
          </div>
        </div>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Documentation</h5>
            <p class="text-muted">All public functions, classes, and modules must have docstrings using the numpydoc format:</p>
            <pre><code>def example_function(param1, param2):
    """
    Brief description of function.

    Longer description if needed.

    Parameters
    ----------
    param1 : type
        Description of param1.
    param2 : type
        Description of param2.

    Returns
    -------
    type
        Description of return value.
    """</code></pre>
          </div>
        </div>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Testing</h5>
            <p class="text-muted mb-2">We use the unittest framework for testing. Key principles:</p>
            <ul class="mb-0">
              <li>Write tests for all new functionality</li>
              <li>Aim for high code coverage (>80%)</li>
              <li>Test edge cases and error conditions</li>
              <li>Keep tests focused and independent</li>
              <li>Use descriptive test names that explain what is being tested</li>
            </ul>
          </div>
        </div>
        
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Command Line Interfaces</h5>
            <p class="text-muted mb-0">For command line interfaces, we use the Click framework. Ensure CLIs are well-documented with help text and examples.</p>
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
        <h2 class="h3 fw-bold mb-4">Code Review Process</h2>
        
        <p class="text-muted mb-4">All contributions go through a code review process to maintain quality and consistency:</p>
        
        <ol class="list-group list-group-numbered">
          <li class="list-group-item">
            <strong>Submit Pull Request</strong> - Open a PR with your changes
          </li>
          <li class="list-group-item">
            <strong>Automated Checks</strong> - CI/CD runs tests and linters automatically
          </li>
          <li class="list-group-item">
            <strong>Code Review</strong> - Maintainers review your code and provide feedback
          </li>
          <li class="list-group-item">
            <strong>Address Feedback</strong> - Make requested changes and push updates
          </li>
          <li class="list-group-item">
            <strong>Approval</strong> - Once approved, a maintainer will merge your PR
          </li>
        </ol>
        
        <div class="alert alert-info mt-4">
          <strong>Be patient!</strong> Maintainers are often busy researchers. It may take some time to review your contribution. Feel free to politely ping after a week if you haven't received feedback.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Community Guidelines</h2>
        
        <p class="text-muted mb-4">The asimov community is committed to providing a welcoming and inclusive environment for all contributors. We expect all participants to:</p>
        
        <ul>
          <li>Be respectful and considerate in all interactions</li>
          <li>Welcome newcomers and help them get started</li>
          <li>Focus on what is best for the community and the science</li>
          <li>Show empathy towards other community members</li>
          <li>Accept constructive criticism gracefully</li>
          <li>Avoid demeaning, discriminatory, or harassing behavior</li>
        </ul>
        
        <p class="text-muted mt-4">By contributing to asimov, you agree to abide by these community guidelines and our code of conduct.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <h2 class="h3 fw-bold mb-4">Questions?</h2>
        
        <p class="text-muted mb-4">If you have questions about contributing or need help getting started:</p>
        
        <div class="row g-3">
          <div class="col-md-6">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">GitHub Discussions</h5>
                <p class="text-muted mb-0">Ask questions and discuss ideas in GitHub Discussions</p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Open an Issue</h5>
                <p class="text-muted mb-0">For specific bugs or features, open an issue on GitHub</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="text-center mt-5">
          <h3 class="h4 fw-bold mb-3">Ready to Contribute?</h3>
          <p class="lead text-muted mb-4">Help us make gravitational-wave analysis fun, easy, and reproducible!</p>
          <a href="https://github.com/etive-io" target="_blank" class="btn btn-primary btn-lg">View Repositories on GitHub</a>
        </div>
      </div>
    </div>
  </div>
</section>
