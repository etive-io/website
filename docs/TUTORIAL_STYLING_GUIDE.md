<!-- Tutorial Step-by-Step Template Guide -->

This document shows how to use the new procedural step styling in tutorials.

## Basic Step-by-Step Format

Use this HTML structure for numbered steps:

```html
<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Step Title Here</h3>
      <p>Description of what to do in this step.</p>
      <pre><code>command to run</code></pre>
    </div>
  </div>
  
  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Next Step Title</h3>
      <p>More instructions...</p>
    </div>
  </div>
</div>
```

## Notes and Callouts

Within step content, use these callout styles:

### Info Note
```html
<div class="step-note">
  <strong>Additional Context</strong>
  <p>This information is helpful but not required.</p>
</div>
```

### Warning
```html
<div class="step-warning">
  <strong>Be Careful</strong>
  <p>This action has potential side effects.</p>
</div>
```

### Tip
```html
<div class="step-tip">
  <strong>Pro Tip</strong>
  <p>This will make your workflow more efficient.</p>
</div>
```

### Important
```html
<div class="step-important">
  <strong>Required</strong>
  <p>You must do this for the tutorial to work.</p>
</div>
```

## Multiple Options

For steps with alternatives:

```html
<div class="step-options">
  <div class="step-option">
    <strong>Option A: Interactive Wizard (Recommended for new users)</strong>
    <p>If you prefer guided setup, use this approach.</p>
    <pre><code>command for option A</code></pre>
  </div>
  
  <div class="step-option">
    <strong>Option B: Direct Command (For experienced users)</strong>
    <p>If you know exactly what you want, use this.</p>
    <pre><code>command for option B</code></pre>
  </div>
</div>
```

## Subsections Within Steps

For detailed breakdown of a step:

```html
<div class="procedural-step-content">
  <h3>Install Dependencies</h3>
  <p>This step installs three main components:</p>
  
  <div class="step-substep">
    <h5>Install Python</h5>
    <p>First, install Python 3.11...</p>
  </div>
  
  <div class="step-substep">
    <h5>Install Libraries</h5>
    <p>Next, install the necessary libraries...</p>
  </div>
</div>
```

## Tutorial Introduction

For the intro section of a tutorial:

```html
<div class="tutorial-intro">
  <h2>Tutorial: Your First Analysis</h2>
  <div class="intro-item">
    <strong>What you'll learn:</strong> How to set up and run your first analysis
  </div>
  <div class="intro-item">
    <strong>Time required:</strong> About 15 minutes
  </div>
  <div class="intro-item">
    <strong>Prerequisites:</strong> Python 3.9+ and conda
  </div>
</div>
```

## Usage in Markdown

In your Markdown tutorials, you can mix Markdown headers with HTML step divs:

```markdown
## Step 1: Install Dependencies

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Create Environment</h3>
      <p>Create a new conda environment for isolation:</p>
      <pre><code class="language-bash">conda create -n tutorial python=3.11
conda activate tutorial</code></pre>
      
      <div class="step-note">
        <strong>Why isolate?</strong>
        <p>This keeps your tutorial environment separate from other projects.</p>
      </div>
    </div>
  </div>
</div>
```

## CSS Classes Quick Reference

| Class | Purpose |
|-------|---------|
| `.procedural-steps` | Container for all steps |
| `.procedural-step` | Single step (includes number + content) |
| `.procedural-step-number` | Numbered circle |
| `.procedural-step-content` | Step description and details |
| `.step-note` | ℹ️ Blue informational callout |
| `.step-warning` | ⚠️ Yellow warning callout |
| `.step-tip` | 💡 Green tip callout |
| `.step-important` | ⭐ Red important callout |
| `.step-substep` | Subsection within a step |
| `.step-options` | Container for alternative approaches |
| `.step-option` | Single option/alternative |
| `.tutorial-intro` | Introduction section with metadata |
