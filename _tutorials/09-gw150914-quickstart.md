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

**New features** in asimov 0.7.0 that make this easier:
- The new **asimov-gwdata plugin** with smart project setup commands
- **Improved dependency resolution** for complex multi-stage analyses  
- **Better Python API** for programmatic project creation
- **Enhanced HTML reporting** with workflow visualization
- **State machine-based monitoring** for more robust job tracking

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
      <h3>Install Asimov and the GWData Plugin</h3>
      <p>Since asimov 0.7.0 is currently in pre-release, we need to use pip with the pre-release flag:</p>
      <pre><code class="language-bash"># Install asimov 0.7.0 (pre-release)
pip install --pre 'asimov>=0.7.0a1'

# Install the gwdata plugin (0.7.0-alpha)
pip install --pre 'asimov-gwdata>=0.7.0a1'</code></pre>
      
      <p>After the official release, this simplifies to:</p>
      <pre><code class="language-bash">pip install asimov asimov-gwdata</code></pre>
      
      <div class="step-important">
        <strong>Keep the pre-release flag</strong>
        <p>The <code>--pre</code> flag is required to download pre-release versions. Without it, pip won't find the right version.</p>
      </div>
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
      <pre><code class="language-bash">asimov --version
asimov gw events list --catalog gwtc-2-1 | head -5</code></pre>
      
      <p>You should see asimov's version number and a short list of events.</p>
      
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

## Step 1: Explore Available Events and Analyses

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Browse Available Events</h3>
      <p>Before setting up your project, let's see what's available. The asimov-gwdata plugin provides convenient commands to discover events and analysis configurations:</p>
      <pre><code class="language-bash"># List all available events from the GWTC-2.1 catalogue
asimov gw events list --catalog gwtc-2-1

# Get detailed information about GW150914
asimov gw events show GW150914_095045</code></pre>
      
      <p>This will show you:</p>
      <ul>
        <li>The exact time the signal was detected</li>
        <li>Which detectors (LIGO Hanford and LIGO Livingston) observed it</li>
        <li>Recommended priors for parameter estimation</li>
        <li>Data quality information</li>
      </ul>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Browse Available Analysis Templates</h3>
      <p>Now let's see what analysis configurations are available:</p>
      <pre><code class="language-bash"># List all available analysis templates
asimov gw analyses list

# Show details about the production configuration
asimov gw analyses show production-default</code></pre>
    </div>
  </div>
</div>

## Step 2: Set Up Your Project

<div class="procedural-steps">
  <div class="procedural-step">
    <div class="procedural-step-number">1</div>
    <div class="procedural-step-content">
      <h3>Create Project Directory</h3>
      <p>First, create a directory for your project and move into it:</p>
      <pre><code class="language-bash">mkdir gw150914-tutorial
cd gw150914-tutorial</code></pre>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Choose Your Setup Method</h3>
      <p>Now you have two options for setting up your analysis:</p>
      
      <div class="step-options">
        <div class="step-option">
          <strong>Option A: Interactive Wizard (Recommended for new users)</strong>
          <p>If you prefer a guided, step-by-step approach, use the interactive wizard:</p>
          <pre><code class="language-bash">asimov gw quickstart</code></pre>
          <p>This will walk you through friendly prompts to choose your analysis preset, select events, pick analyses, and configure options. The wizard then automatically sets everything up for you.</p>
        </div>

        <div class="step-option">
          <strong>Option B: Direct Command (For experienced users)</strong>
          <p>If you know exactly what you want, use the direct setup command:</p>
          <pre><code class="language-bash">asimov gw setup \
  --events GW150914_095045 \
  --analyses production-default</code></pre>
          <p>This command downloads configurations, sets up pipelines, initializes git, and resolves dependencies automatically.</p>
        </div>
      </div>
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
│       ├── bayeswave/         # Bayeswave on-source PSD job
│       └── bilby/             # Bilby parameter estimation job
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
  - Prod0[bayeswave]    ready
  - Prod1[bilby]        ready (waiting for Prod0)</code></pre>
      
      <div class="step-note">
        <strong>Dependency resolution</strong>
        <p>Notice how Prod1 (bilby) is marked as "waiting"—asimov's improved dependency resolution (new in 0.7.0) knows that bilby needs the power spectral density (PSD) estimates from bayeswave before it can start.</p>
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
      <p>Create all the pipeline-specific configuration files:</p>
      <pre><code class="language-bash">asimov manage build</code></pre>
      
      <p>You'll see output like:</p>
      <pre><code>● Working on GW150914_095045
  Working on production Prod0
  Production config Prod0 created.</code></pre>
      
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
        <p>This submits the bayeswave job (Prod0) to the scheduler. The bilby job (Prod1) won't submit yet because it's waiting for bayeswave to complete—that's the dependency system in action.</p>
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
      
      <p>This checks the job status once and shows you what's happening:</p>
      <pre><code>GW150914_095045
  - Prod0[bayeswave]
    ● Running (HTCondor ID: 12345)
  - Prod1[bilby]  
    ● Waiting (ready to run after Prod0 completes)</code></pre>
    </div>
  </div>

  <div class="procedural-step">
    <div class="procedural-step-number">2</div>
    <div class="procedural-step-content">
      <h3>Continuous Monitoring (Recommended)</h3>
      <p>For longer jobs, set up automated monitoring that will:</p>
      <ul>
        <li>Check job status every 15 minutes</li>
        <li>Automatically submit dependent jobs when their dependencies complete</li>
        <li>Run post-processing when analyses finish</li>
        <li>Provide real-time HTML reports (new in 0.7.0)</li>
      </ul>
      
      <pre><code class="language-bash">asimov start</code></pre>
      
      <p>You'll see:</p>
      <pre><code>● Asimov is running (process ID: 54321)</code></pre>
      
      <p>This starts a background process. You can check the logs at any time with:</p>
      <pre><code class="language-bash">tail -f asimov.log</code></pre>
      
      <p>And stop monitoring whenever you're ready:</p>
      <pre><code class="language-bash">asimov stop</code></pre>
      
      <div class="step-tip">
        <strong>Pro tip: Let it run</strong>
        <p>For production analyses, we recommend leaving monitoring running in a <code>screen</code> or <code>tmux</code> session so it stays active even if you disconnect.</p>
      </div>
    </div>
  </div>
</div>

## Step 6: Understanding the Analysis

While your job is running, let's understand what's happening:

<div class="step-substep">
  <h4>The Multi-Stage Workflow</h4>
  <p>Your project has two analyses working together:</p>
  <ol>
    <li><strong>Bayeswave (Prod0):</strong> Produces an estimate of the power spectral density (the noise characteristics) of the detector during the GW150914 observation. This typically takes hours to days.</li>
    <li><strong>Bilby (Prod1):</strong> Uses the PSD from Bayeswave to perform the actual parameter estimation—inferring properties like the masses and spins of the merging black holes. This uses Bayesian inference to calculate the probability of different parameters given the observed signal.</li>
  </ol>
  <p>The state machine monitoring (new in 0.7.0) automatically handles submitting Prod1 once Prod0 completes.</p>
</div>

<div class="step-substep">
  <h4>Tracking Progress with Reports</h4>
  <p>Once monitoring is running, asimov generates HTML reports showing:</p>
  <ul>
    <li>Current job status</li>
    <li>Workflow dependency graphs (new in 0.7.0)</li>
    <li>Historical information</li>
    <li>Any errors or warnings</li>
  </ul>
  <p>These are stored in the <code>results/</code> directory.</p>
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
    <p>Add another event to your existing project:</p>
    <pre><code class="language-bash">asimov gw events add GW151012_095443 --analyses production-default
asimov manage build && asimov manage submit</code></pre>
  </div>

  <div class="step-option">
    <strong>Customize Your Analysis</strong>
    <p>Edit <code>.asimov/ledger.yml</code> to adjust analysis settings like prior ranges, sampler settings, and waveform approximants. Then rebuild:</p>
    <pre><code class="language-bash">asimov manage build && asimov manage submit</code></pre>
  </div>

  <div class="step-option">
    <strong>Use a Different Pipeline</strong>
    <p>Instead of <code>production-default</code>, you could use alternatives like <code>bilby-IMRPhenomXPHM</code> or custom configurations. See <code>asimov gw analyses list</code> for all options.</p>
  </div>

  <div class="step-option">
    <strong>Contribute to Asimov</strong>
    <p>Check out the <a href="/contributing">Contributing Guide</a> to get involved with development!</p>
  </div>
</div>

## Troubleshooting

<div class="step-substep">
  <h4>HTCondor not found</h4>
  <p>Make sure HTCondor is installed and the <code>condor</code> commands are in your PATH:</p>
  <pre><code class="language-bash">which condor_q</code></pre>
  <p>If this fails, refer to the <a href="#appendix-single-machine-setup-optional">Single-Machine Setup appendix</a> below.</p>
</div>

<div class="step-substep">
  <h4>Project ledger is corrupted</h4>
  <p>If your <code>.asimov/ledger.yml</code> file becomes corrupted, you can regenerate it:</p>
  <pre><code class="language-bash">rm -rf .asimov/
asimov init "My Project"
asimov apply -f ...  # Re-apply your configurations</code></pre>
</div>

<div class="step-substep">
  <h4>Job won't submit</h4>
  <p>Check the working directory for HTCondor error logs:</p>
  <pre><code class="language-bash">cat working/GW150914_095045/Prod0/*.err</code></pre>
</div>

<div class="step-substep">
  <h4>Results are missing</h4>
  <p>Check that the job completed successfully:</p>
  <pre><code class="language-bash">asimov monitor</code></pre>
  <p>Look for status messages in <code>asimov.log</code>:</p>
  <pre><code class="language-bash">tail -n 100 asimov.log</code></pre>
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

### Future Improvements

We're actively working to make asimov easier to use without requiring HTCondor. Upcoming features will include:
- Direct cloud computing support (AWS, Google Cloud, etc.)
- Local multiprocessing support
- Slurm scheduler integration
- Better containerization

Stay tuned for updates!
