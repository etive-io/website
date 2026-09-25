---
layout: post
title: Analysing your first gravitational wave candidate with asimov
category: getting-started
pin: true
order: 1
---


## Introduction

<div class="tutorial-intro">
  <h2>Tutorial: Analysing your first gravitational wave candidate</h2>
  <div class="intro-item">
    <strong>What you'll learn:</strong> How to use asimov's new quickstart infrastructure to go from zero to a running parameter estimation job in minutes
  </div>
  <div class="intro-item">
    <strong>Time required:</strong> About 30 minutes for setup, then hours to days for analysis to run
  </div>
  <div class="intro-item">
    <strong>What is GW150914?</strong> The first gravitational wave ever detected, from the merger of two black holes approximately 1.3 billion light-years away. Analyzing it is a classic "hello world" example for parameter estimation workflows
  </div>
</div>

This tutorial uses **asimov 0.7.1** (released 2026-09-18; 0.7.0 was released 2026-08-17). It relies on three plugins: **asimov-gwdata** to fetch strain data, **bayeswave** to estimate the detector noise PSD, and **bilby** to perform the parameter estimation itself.

## Prerequisites

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Set Up Your Python Environment</h3>
      <p>We recommend using conda (a package and environment manager) to isolate your asimov installation. If you don't have conda installed yet, <a href="https://docs.conda.io/projects/miniconda/en/latest/">download miniconda</a> (a lightweight version of Anaconda).</p>
      
      <p>Create a new conda environment:</p>
      <pre><code class="language-bash">conda create -n gw-analysis python=3.11
conda activate gw-analysis</code></pre>
      
      <div class="step-tip">
        <strong>Why isolate?</strong>
        <p>This creates a separate Python environment called <code>gw-analysis</code> so you don't affect other projects on your computer. Always make sure to activate this environment before working with asimov.</p>
      </div>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Install the IGWN Software Stack</h3>
      <p>The International Gravitational-Wave Network (IGWN) provides a curated conda environment with all the gravitational wave analysis tools pre-configured:</p>
      <pre><code class="language-bash"># Add the IGWN conda channel
conda config --add channels conda-forge
conda config --add channels igwn

# Install the IGWN environment
conda install -c conda-forge -c igwn igwn-software</code></pre>
      
      <p>This installs:</p>
      <ul>
        <li>All required gravitational wave analysis tools</li>
        <li>The necessary data analysis libraries</li>
        <li>Git and other utilities</li>
      </ul>
      
      <div class="step-note">
        <strong>Installation time</strong>
        <p>This step may take 5-15 minutes depending on your internet connection.</p>
      </div>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">3</div>
    <div class="procedural-step-content">
      <h3>Install Asimov and the Pipeline Plugins</h3>
      <p>Install asimov itself, plus the three pipeline plugins this tutorial uses: <code>asimov-gwdata</code> (fetches strain data), <code>bayeswave</code> (PSD estimation), and <code>bilby</code> (parameter estimation).</p>
      <pre><code class="language-bash"># Via pip
pip install asimov asimov-gwdata bilby_pipe bilby

# Or via conda
conda install -c conda-forge bilby bayeswave asimov-gwdata</code></pre>
      <p class="text-muted">The <code>bayeswave</code> package is currently only available via conda-forge.</p>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">4</div>
    <div class="procedural-step-content">
      <h3>Configure Git</h3>
      <p>Asimov uses git to track your project. Configure it globally if you haven't already:</p>
      <pre><code class="language-bash">git config --global user.email "you@example.com"
git config --global user.name "Your Name"</code></pre>
      
      <p>Replace the email and name with your own values.</p>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">5</div>
    <div class="procedural-step-content">
      <h3>Check Your HTCondor Installation</h3>
      <p>This tutorial assumes HTCondor (a job scheduler) is already installed and running on your system. Test it:</p>
      <pre><code class="language-bash">which condor_q
condor_q</code></pre>
      
      <div class="step-warning">
        <strong>HTCondor required</strong>
        <p>If these commands don't work, refer to the <a href="#appendix-single-machine-setup-optional">Single-Machine Setup appendix</a> below to install minicondor.</p>
      </div>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">6</div>
    <div class="procedural-step-content">
      <h3>Verify Your Complete Setup</h3>
      <p>Make sure everything is installed correctly:</p>
      <pre><code class="language-bash">asimov --version</code></pre>
      
      <p>You should see asimov's version number printed (0.7.1 or later).</p>
      
      <div class="step-note">
        <strong>Troubleshooting</strong>
        <p>If you see errors, make sure you've:</p>
        <ul>
          <li>Activated the conda environment: <code>conda activate gw-analysis</code></li>
          <li>Installed all packages successfully</li>
          <li>Configured git globally</li>
        </ul>
      </div>
    </div>
  </div>
</div>

## Step 1: About GW150914

GW150914 was the first gravitational wave ever detected, observed by the LIGO Hanford and Livingston
detectors on 14 September 2015. It's a common "hello world" event for parameter-estimation tutorials
because it's well studied and its blueprints are readily available. asimov doesn't ship its own
catalogue browser—instead, events and analysis defaults are distributed as YAML blueprint files that
you apply directly to your project, which is what the next step does.

## Step 2: Set Up Your Project

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Create Project Directory</h3>
      <p>First, create a directory for your project, move into it, and initialize an asimov project:</p>
      <pre><code class="language-bash">mkdir gw150914-tutorial
cd gw150914-tutorial
asimov init "GW150914 Analysis Tutorial"</code></pre>
      <p class="text-muted">This sets up the project's directory structure and a blank, git-tracked ledger.</p>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Apply the Project-Wide Defaults</h3>
      <p>Asimov ships pipelines with a minimal set of default settings. A blueprint with the settings normally used for LVK production analyses is maintained in the asimov data repository—apply the resource-allocation defaults and the prior defaults:</p>
      <pre><code class="language-bash">asimov apply -f https://git.ligo.org/asimov/data/-/raw/main/defaults/production-pe.yaml
asimov apply -f https://git.ligo.org/asimov/data/-/raw/main/defaults/production-pe-priors.yaml</code></pre>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">3</div>
    <div class="procedural-step-content">
      <h3>Add the Event</h3>
      <p>Add GW150914 to the project by applying its event blueprint, which is also maintained in the data repository:</p>
      <pre><code class="language-bash">asimov apply -f https://git.ligo.org/asimov/data/-/raw/main/events/gwtc-2-1/GW150914_095045.yaml</code></pre>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">4</div>
    <div class="procedural-step-content">
      <h3>Define the Workflow</h3>
      <p>The standard workflow for a gravitational-wave analysis has three stages: fetch data (<code>gwdata</code>), estimate the noise PSD (<code>bayeswave</code>), then run parameter estimation (<code>bilby</code>), with each stage declaring the previous one as a dependency via <code>needs</code>. Save the following as <code>workflow.yaml</code>:</p>
      <pre><code class="language-yaml">kind: analysis
name: get-data
pipeline: gwdata
file length: 4096
download:
  - frames
scheduler:
  accounting group: ligo.dev.o4.cbc.pe.bilby
  request memory: 1024
  request post memory: 16384
---
kind: analysis
name: generate-psd
pipeline: bayeswave
comment: Bayeswave on-source PSD estimation process
needs:
  - get-data
---
kind: analysis
name: bilby-IMRPhenomXPHM-cosmo
pipeline: bilby
waveform:
  approximant: IMRPhenomXPHM
comment: PE job using IMRPhenomXPHM and bilby
needs:
  - generate-psd</code></pre>
      <p>Then apply the workflow to the event you added above, using its full name:</p>
      <pre><code class="language-bash">asimov apply -f workflow.yaml -e GW150914_095045</code></pre>
    </div>
  </div>
</div>

## Step 3: Understand Your Project Structure

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Review Your Project Layout</h3>
      <p>Your new project has a carefully organized structure:</p>
      <pre><code>gw150914-tutorial/
├── .asimov/                    # Asimov's internal directory
│   └── ledger.yml             # The project database (git-tracked)
├── checkouts/                  # Working directories for each analysis
│   └── GW150914_095045/       # Event directory
│       ├── get-data/          # gwdata download job
│       ├── generate-psd/      # Bayeswave on-source PSD job
│       └── bilby-IMRPhenomXPHM-cosmo/  # Bilby parameter estimation job
├── results/                    # Where results will be stored
├── working/                    # HTCondor job submission files
└── README.md                   # Project information</code></pre>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Check Your Analysis Status</h3>
      <p>To see the current status of your analyses, run:</p>
      <pre><code class="language-bash">asimov report status</code></pre>
      
      <p>You should see something like:</p>
      <pre><code>GW150914_095045
  Analyses
  - get-data[gwdata]                      ready
  - generate-psd[bayeswave]               waiting (needs get-data)
  - bilby-IMRPhenomXPHM-cosmo[bilby]      waiting (needs generate-psd)</code></pre>
      
      <div class="step-note">
        <strong>Dependency resolution</strong>
        <p>The <code>needs</code> entries in <code>workflow.yaml</code> tell asimov that <code>generate-psd</code> needs the strain data from <code>get-data</code>, and the bilby analysis needs the PSD from <code>generate-psd</code>, before each can be built and submitted.</p>
      </div>
    </div>
  </div>
</div>

## Step 4: Build and Submit Your Jobs

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Build Configuration Files</h3>
      <p>Asimov works out which stages of the workflow are ready to run and produces the configuration needed to submit them to the scheduler. Since only <code>get-data</code> has no unmet dependencies, this is the stage that gets built first:</p>
      <pre><code class="language-bash">asimov manage build</code></pre>
      
      <div class="step-tip">
        <strong>Check the working directory</strong>
        <p>Look in the <code>working/</code> directory—you'll find HTCondor job description files here.</p>
      </div>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Submit Jobs to the Scheduler</h3>
      <p>Now submit the first analysis to HTCondor:</p>
      <pre><code class="language-bash">asimov manage submit</code></pre>
      
      <div class="step-note">
        <strong>Dependency handling</strong>
        <p>This submits the <code>get-data</code> job to the scheduler. <code>generate-psd</code> and the bilby analysis won't submit yet, because they're waiting on their dependencies—run <code>asimov manage build</code> and <code>asimov manage submit</code> again as each stage completes, or use <code>asimov start</code> below to automate this.</p>
      </div>
    </div>
  </div>
</div>

## Step 5: Monitor Your Analysis

Now we need to watch our job. Asimov provides several ways to do this:

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>One-time Status Check</h3>
      <p>For a quick status check:</p>
      <pre><code class="language-bash">asimov monitor</code></pre>
      
      <p>This checks the job status once and shows you what's happening, similar to <code>asimov report status</code>.</p>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Continuous Monitoring (Recommended)</h3>
      <p>You probably don't want to check on these jobs by hand. Asimov can automate the process instead: checking the status of each analysis, and building and submitting the next stage automatically once its dependencies complete.</p>
      
      <pre><code class="language-bash">asimov start</code></pre>
      
      <p>This starts a background monitoring process, and stops once everything is done, or you can stop it yourself with:</p>
      <pre><code class="language-bash">asimov stop</code></pre>
    </div>
  </div>
</div>

## Step 6: Understanding the Analysis

While your job is running, let's understand what's happening:

<div class="step-substep">
  <h4>The Multi-Stage Workflow</h4>
  <p>Your project has three analyses working together:</p>
  <ol>
    <li><strong>get-data:</strong> Fetches the strain data needed for the analysis, via the <code>gwdata</code> plugin.</li>
    <li><strong>generate-psd (Bayeswave):</strong> Produces an estimate of the power spectral density (the noise characteristics) of the detector during the GW150914 observation. This typically takes hours to days.</li>
    <li><strong>bilby-IMRPhenomXPHM-cosmo (Bilby):</strong> Uses the PSD from Bayeswave to perform the actual parameter estimation—inferring properties like the masses and spins of the merging black holes, using Bayesian inference to calculate the probability of different parameters given the observed signal.</li>
  </ol>
  <p>Asimov's dependency resolution, declared with <code>needs</code> in <code>workflow.yaml</code>, submits each stage automatically once the one before it completes.</p>
</div>

<div class="step-substep">
  <h4>Tracking Progress with Reports</h4>
  <p>You can generate an HTML status report for the project at any time with:</p>
  <pre><code class="language-bash">asimov report html</code></pre>
  <p>By default this is written to the project's configured web directory; PESummary-based pages for a completed bilby analysis are written under <code>pages/</code>.</p>
</div>

## Step 7: When Jobs Complete

After your jobs finish (this can take days or weeks for production-quality analyses!), asimov will:

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Automatic Post-Processing</h3>
      <p>Asimov automatically:</p>
      <ul>
        <li>Runs post-processing with PESummary to generate summary statistics and plots</li>
        <li>Moves results to the <code>results/</code> directory</li>
        <li>Generates comprehensive HTML reports with visualization of the posterior distributions</li>
        <li>Marks analyses as complete</li>
      </ul>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Examine Your Results</h3>
      <p>You can then examine the results:</p>
      <pre><code class="language-bash">ls results/GW150914_095045/</code></pre>
      
      <p>This directory contains all your output files, plots, and reports.</p>
    </div>
  </div>
</div>

## Next Steps

<div class="step-options">
  <div class="step-option">
    <strong>Run More Events</strong>
    <p>Add another event by applying its blueprint from the data repository, then apply a similar workflow blueprint to it:</p>
    <pre><code class="language-bash">asimov apply -f https://git.ligo.org/asimov/data/-/raw/main/events/gwtc-2-1/GW151012_095443.yaml
asimov apply -f workflow.yaml -e GW151012_095443
asimov manage build && asimov manage submit</code></pre>
  </div>

  <div class="step-option">
    <strong>Customize Your Analysis</strong>
    <p>Edit <code>workflow.yaml</code> to adjust settings like waveform approximants, priors, or sampler settings, then re-apply it and rebuild:</p>
    <pre><code class="language-bash">asimov apply -f workflow.yaml -e GW150914_095045
asimov manage build && asimov manage submit</code></pre>
  </div>

  <div class="step-option">
    <strong>Use a Different Pipeline</strong>
    <p>Swap <code>pipeline: bilby</code> for another supported sampler, such as <code>lalinference</code> or <code>rift</code>, provided the corresponding plugin is installed. See the <a href="{{ "/plugins" | relative_url }}">plugins directory</a> for what's available.</p>
  </div>

  <div class="step-option">
    <strong>Contribute to Asimov</strong>
    <p>Check out the <a href="{{ "/contributing" | relative_url }}">Contributing Guide</a> to get involved with development.</p>
  </div>
</div>



---

## Appendix: Single-Machine Setup (Optional)

If you're working on a single machine without an existing HTCondor installation, you can use **HTCondor's mini version**, minicondor, which is designed for personal workstations.

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Install Minicondor</h3>
      <p>HTCondor provides pre-built installers. Visit <a href="https://htcondor.readthedocs.io/en/latest/getting-htcondor/">htcondor.readthedocs.io</a> and follow the installation guide for your operating system.</p>
      
      <p><strong>On Linux (Ubuntu/Debian):</strong></p>
      <pre><code class="language-bash"># Add HTCondor repository
wget -qO - https://research.cs.wisc.edu/htcondor/yum/HTCondor/repo.key | sudo apt-key add -
echo "deb [arch=amd64] https://research.cs.wisc.edu/htcondor/yum/HTCondor/ubuntu focal main" | \
  sudo tee /etc/apt/sources.list.d/htcondor.list

# Install minicondor
sudo apt-get update
sudo apt-get install minicondor</code></pre>
      
      <p><strong>On macOS:</strong></p>
      <pre><code class="language-bash"># Using Homebrew
brew tap htcondor/htcondor
brew install htcondor</code></pre>
      
      <p>For other systems, follow the <a href="https://htcondor.readthedocs.io/en/latest/getting-htcondor/">official installation guide</a>.</p>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Configure Minicondor</h3>
      <p>After installation, start the HTCondor daemon:</p>
      <pre><code class="language-bash"># Start the HTCondor daemon
sudo /etc/init.d/condor start

# Or on systems using systemd
sudo systemctl start condor</code></pre>
      
      <p>For personal workstations, limit resource usage by editing <code>/etc/condor/condor_config.d/personal.conf</code>:</p>
      <pre><code>NUM_SLOTS = 1
NUM_SLOTS_TYPE_1 = 1</code></pre>
      
      <p>This ensures only one job runs at a time on your machine.</p>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">3</div>
    <div class="procedural-step-content">
      <h3>Verify Installation</h3>
      <p>Test that HTCondor is working:</p>
      <pre><code class="language-bash">condor_q          # List jobs (should be empty)
condor_status     # Show available slots</code></pre>
      
      <p>Now you can follow the main tutorial above!</p>
    </div>
  </div>
</div>

### Important Notes on Single-Machine Use

<div class="step-substep">
  <h4>Advantages</h4>
  <ul>
    <li>Learn asimov on your personal computer</li>
    <li>Good for testing and development</li>
    <li>Useful for small analyses</li>
  </ul>
</div>

<div class="step-substep">
  <h4>Limitations</h4>
  <ul>
    <li>Jobs run sequentially on limited resources</li>
    <li>Parameter estimation analyses will be <strong>very slow</strong> on most personal computers</li>
    <li>Not suitable for production catalogue analyses</li>
  </ul>
</div>

<div class="step-note">
  <strong>For production work</strong>
  <p>We recommend using institutional computing clusters with HTCondor, or work with your institution's computing facility to set up access.</p>
</div>

### Other Schedulers

Besides HTCondor, asimov also supports submitting and monitoring jobs on **Slurm**. If your institution's
cluster runs Slurm rather than HTCondor, see the asimov documentation for how to configure it as your
scheduler backend.
