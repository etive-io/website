---
layout: post
title: Step-by-Step Tutorial Styling Reference
category: documentation
order: 99
---

This tutorial demonstrates all available step-by-step styling features. Use this as a reference when creating your own tutorials.

## Introduction Section

<div class="tutorial-intro">
  <h2>Example: Building Your First Project</h2>
  <div class="intro-item">
    <strong>What you'll learn:</strong> How to structure and organize a project with best practices
  </div>
  <div class="intro-item">
    <strong>Time required:</strong> About 10 minutes
  </div>
  <div class="intro-item">
    <strong>Prerequisites:</strong> Basic familiarity with command line
  </div>
</div>

## Basic Procedural Steps

Steps are displayed with numbered circles, vertical connectors, and clear organization:

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Set Up Your Environment</h3>
      <p>First, create a dedicated directory and initialize version control:</p>
      <pre><code class="language-bash">mkdir my-project
cd my-project
git init</code></pre>
      <div class="step-tip">
        <strong>Why version control?</strong>
        <p>Git helps you track changes and collaborate with others.</p>
      </div>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Install Dependencies</h3>
      <p>Install the required packages in your environment:</p>
      <pre><code class="language-bash">pip install asimov bilby-pipe</code></pre>
      <div class="step-note">
        <strong>Virtual environments</strong>
        <p>Consider using a virtual environment to avoid conflicts with other projects.</p>
      </div>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">3</div>
    <div class="procedural-step-content">
      <h3>Verify Installation</h3>
      <p>Check that everything is installed correctly:</p>
      <pre><code class="language-bash">asimov --version
bilby --version</code></pre>
      <div class="step-warning">
        <strong>Check output</strong>
        <p>If you see "command not found," the installation didn't complete. Reinstall the packages.</p>
      </div>
    </div>
  </div>
</div>

## Multiple Options

When a step has alternatives, present them as options:

<div class="step-options">
  <div class="step-option">
    <strong>Option A: Interactive Setup (Recommended for beginners)</strong>
    <p>Use the guided wizard to configure your project step by step:</p>
    <pre><code class="language-bash">asimov setup --interactive</code></pre>
    <p>This walks you through each configuration choice with helpful explanations.</p>
  </div>

  <div class="step-option">
    <strong>Option B: Configuration File (For advanced users)</strong>
    <p>Create a configuration file with all settings upfront:</p>
    <pre><code class="language-bash">cat > config.yml << EOF
name: my-project
pipeline: bilby
events:
  - GW150914
EOF
asimov setup -c config.yml</code></pre>
    <p>This is faster if you know exactly what you want.</p>
  </div>
</div>

## Step Callouts

Use callouts to highlight important information:

### Information Note
<div class="step-note">
  <strong>Additional context</strong>
  <p>This note provides helpful context that isn't essential to complete the step, but will make your experience better.</p>
</div>

### Warning
<div class="step-warning">
  <strong>Potential issue</strong>
  <p>Pay attention here—this action could cause problems if not done correctly.</p>
</div>

### Tip
<div class="step-tip">
  <strong>Pro tip</strong>
  <p>This will make your workflow more efficient or help you avoid common mistakes.</p>
</div>

### Important
<div class="step-important">
  <strong>Required step</strong>
  <p>You must complete this action for the tutorial to work correctly.</p>
</div>

## Substeps Within a Step

For complex steps, break them down with substeps:

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Configure Your Analysis</h3>
      <p>The configuration process involves several substeps:</p>

      <div class="step-substep">
        <h5>1. Select Your Pipeline</h5>
        <p>Choose which analysis pipeline you want to use. Options include bilby, PyCBC, or LALInference.</p>
        <pre><code>asimov setup
> Which pipeline? [bilby/pycbc/lal]: bilby</code></pre>
      </div>

      <div class="step-substep">
        <h5>2. Configure Event Data</h5>
        <p>Specify which gravitational wave events you want to analyze:</p>
        <pre><code>> Events to analyze: GW150914 GW151226</code></pre>
      </div>

      <div class="step-substep">
        <h5>3. Set Analysis Parameters</h5>
        <p>Configure the details of your analysis:</p>
        <pre><code>> Duration (seconds): 4
> Sample rate (Hz): 2048
> Prior type: [uniform/bilby-default]: bilby-default</code></pre>
      </div>
    </div>
  </div>
</div>

## Combining Callouts and Code

You can mix callouts with code examples:

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Submit Your First Job</h3>
      <p>Once everything is configured, submit your analysis:</p>
      <pre><code class="language-bash">asimov manage build
asimov manage submit</code></pre>

      <div class="step-note">
        <strong>What just happened?</strong>
        <p><code>build</code> generated configuration files for your pipeline. <code>submit</code> sent them to the scheduler.</p>
      </div>

      <div class="step-tip">
        <strong>Check status</strong>
        <p>Use <code>asimov monitor</code> to watch your job progress in real time.</p>
      </div>

      <div class="step-important">
        <strong>Wait for completion</strong>
        <p>Analyses can take hours. Don't close your terminal or shut down the monitoring process prematurely.</p>
      </div>
    </div>
  </div>
</div>

## Summary

The new tutorial styling provides:

- **Numbered steps** with visual circles and connecting lines for clear flow
- **Multiple callout types** (notes, warnings, tips, important) with emoji indicators
- **Option containers** for presenting alternatives side-by-side
- **Substeps** for breaking down complex procedures
- **Consistent spacing and colors** that match the site's design

For detailed implementation instructions, see [Tutorial Styling Guide]({{ "/docs/TUTORIAL_STYLING_GUIDE.md" | relative_url }}).
