---
layout: default
title: Analysing your first gravitational wave candidate with asimov
category: getting-started
pin: true
order: 1
---


## Introduction

This tutorial will guide you through setting up and running a gravitational wave analysis using asimov 0.7.0 on GW150914—the first gravitational wave ever detected. GW150914 resulted from the merger of two black holes approximately 1.3 billion light-years away, and analyzing it is a classic "hello world" example for parameter estimation workflows.

**What you'll learn:** How to use asimov's new quickstart infrastructure to go from zero to a running parameter estimation job in minutes.

**New features** in asimov 0.7.0 that make this easier:
- The new **asimov-gwdata plugin** with smart project setup commands
- **Improved dependency resolution** for complex multi-stage analyses  
- **Better Python API** for programmatic project creation
- **Enhanced HTML reporting** with workflow visualization
- **State machine-based monitoring** for more robust job tracking

## Prerequisites

### 1. Setting Up Your Python Environment

We recommend using conda (a package and environment manager) to isolate your asimov installation. If you don't have conda installed yet, you can [download miniconda](https://docs.conda.io/projects/miniconda/en/latest/) (a lightweight version of Anaconda).

**Create a new conda environment:**

```bash
conda create -n gw-analysis python=3.11
conda activate gw-analysis
```

This creates a separate Python environment called `gw-analysis` so you don't affect other projects on your computer. Always make sure to activate this environment before working with asimov.

### 2. Installing the IGWN Software Stack

The International Gravitational-Wave Network (IGWN) provides a curated conda environment with all the gravitational wave analysis tools pre-configured. This is the easiest way to get everything you need:

```bash
# Add the IGWN conda channel
conda config --add channels conda-forge
conda config --add channels igwn

# Install the IGWN environment into your conda environment
conda install -c conda-forge -c igwn igwn-software
```

This installs:
- All required gravitational wave analysis tools
- The necessary data analysis libraries
- Git and other utilities

### 3. Installing Asimov and the GWData Plugin

Since asimov 0.7.0 is currently in pre-release, we need to use pip to install it with the pre-release flag:

```bash
# Install asimov 0.7.0 (pre-release)
pip install --pre 'asimov>=0.7.0a1'

# Install the gwdata plugin (0.7.0-alpha)
pip install --pre 'asimov-gwdata>=0.7.0a1'
```

After the official release, these commands will simplify to:
```bash
pip install asimov asimov-gwdata
```

### 4. Configuring Git

Asimov uses git to track your project. Configure it globally if you haven't already:

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### 5. Checking Your HTCondor Installation

This tutorial assumes HTCondor (a job scheduler) is already installed and running on your system. Test it:

```bash
which condor_q
condor_q
```

If these commands don't work, refer to the [Single-Machine Setup](#single-machine-setup-optional) appendix below to install minicondor.

> **Note:** HTCondor is required for this tutorial. We're actively working to make asimov easier to use without a scheduler—stay tuned for updates!

### Verifying Your Setup

To make sure everything is installed correctly, run:

```bash
asimov --version
asimov gw events list --catalog gwtc-2-1 | head -5
```

You should see asimov's version number and a short list of events. If you see errors, make sure you've:
1. Activated the conda environment: `conda activate gw-analysis`
2. Installed all packages successfully
3. Configured git globally

## Step 1: Explore Available Events and Analyses

Before setting up your project, let's see what's available. The asimov-gwdata plugin provides convenient commands to discover events and analysis configurations:

```bash
# List all available events from the GWTC-2.1 catalogue
asimov gw events list --catalog gwtc-2-1

# Get detailed information about GW150914
asimov gw events show GW150914_095045
```

This will show you:
- The exact time the signal was detected
- Which detectors (LIGO Hanford and LIGO Livingston) observed it
- Recommended priors for parameter estimation
- Data quality information

Now let's see what analysis configurations are available:

```bash
# List all available analysis templates
asimov gw analyses list

# Show details about the production configuration
asimov gw analyses show production-default
```

## Step 2: Set Up Your Project

First, create a directory for your project and move into it:

```bash
mkdir gw150914-tutorial
cd gw150914-tutorial
```

Now you have two options for setting up your analysis:

### Option A: Interactive Wizard (Recommended for new users)

If you prefer a guided, step-by-step approach, use the interactive wizard:

```bash
asimov gw quickstart
```

This will walk you through a series of friendly prompts:
- Choose your analysis preset (production or testing)
- Select which events you want to analyze
- Pick which analyses to run
- Configure any additional options

The wizard then automatically sets everything up for you. This is great if you're new to asimov or want to explore what's available.

### Option B: Direct Command (For experienced users or scripting)

If you know exactly what you want, use the direct setup command:

```bash
asimov gw setup \
  --events GW150914_095045 \
  --analyses production-default
```

This command:
- Downloads and applies the GWTC-2.1 configuration for GW150914
- Sets up production-ready pipeline configurations
- Initializes a git repository for tracking your work
- Automatically resolves dependencies between analyses

Both methods will create the necessary project structure in your current directory.

## Step 3: Understand Your Project Structure

Your new project has a carefully organized structure:

```
gw150914-tutorial/
├── .asimov/                    # Asimov's internal directory
│   └── ledger.yml             # The project database (git-tracked)
├── checkouts/                  # Working directories for each analysis
│   └── GW150914_095045/       # Event directory
│       ├── bayeswave/         # Bayeswave on-source PSD job
│       └── bilby/             # Bilby parameter estimation job
├── results/                    # Where results will be stored
├── working/                    # HTCondor job submission files
└── README.md                   # Project information
```

To see the current status of your analyses, run:

```bash
asimov report status
```

You should see something like:

```
GW150914_095045
  Analyses
  - Prod0[bayeswave]    ready
  - Prod1[bilby]        ready (waiting for Prod0)
```

Notice how Prod1 (bilby) is marked as "waiting"—asimov's improved dependency resolution (new in 0.7.0) knows that the bilby job needs the power spectral density (PSD) estimates from the bayeswave job before it can start.

## Step 4: Build and Submit Your Jobs

Now we'll generate the configuration files and submit them to the scheduler.

**Build:** This creates all the pipeline-specific configuration files:

```bash
asimov manage build
```

You'll see output like:

```
● Working on GW150914_095045
  Working on production Prod0
  Production config Prod0 created.
```

Check the `working/` directory—you'll find HTCondor job description files here.

**Submit:** Now submit the first analysis to HTCondor:

```bash
asimov manage submit
```

This submits the bayeswave job (Prod0) to the scheduler. The bilby job (Prod1) won't submit yet because it's waiting for bayeswave to complete—that's the dependency system in action.

## Step 5: Monitor Your Analysis

Now we need to watch our job. Asimov provides several ways to do this:

### Option A: One-time status check

```bash
asimov monitor
```

This checks the job status once and shows you what's happening:

```
GW150914_095045
  - Prod0[bayeswave]
    ● Running (HTCondor ID: 12345)
  - Prod1[bilby]  
    ● Waiting (ready to run after Prod0 completes)
```

### Option B: Continuous monitoring (recommended)

For longer jobs, you can set up automated monitoring that:
- Checks job status every 15 minutes
- Automatically submits dependent jobs when their dependencies complete
- Runs post-processing when analyses finish
- Provides real-time HTML reports (new in 0.7.0)

```bash
asimov start
```

You'll see:

```
● Asimov is running (process ID: 54321)
```

This starts a background process. You can check the logs at any time with:

```bash
tail -f asimov.log
```

And stop monitoring whenever you're ready:

```bash
asimov stop
```

## Step 6: Understanding the Analysis

While your job is running, let's understand what's happening:

### The Multi-Stage Workflow

Your project has two analyses working together:

1. **Bayeswave (Prod0)**: Produces an estimate of the power spectral density (the noise characteristics) of the detector during the GW150914 observation. This typically takes hours to days.

2. **Bilby (Prod1)**: Uses the PSD from Bayeswave to perform the actual parameter estimation—inferring properties like the masses and spins of the merging black holes. This uses Bayesian inference to calculate the probability of different parameters given the observed signal.

The state machine monitoring (new in 0.7.0) automatically handles submitting Prod1 once Prod0 completes.

### Tracking Progress with Reports

Once monitoring is running, asimov generates HTML reports showing:
- Current job status
- Workflow dependency graphs (new in 0.7.0)
- Historical information
- Any errors or warnings

These are stored in the `results/` directory.

## Step 7: When Jobs Complete

After your jobs finish (this can take days or weeks for production-quality analyses!), asimov will:

1. Automatically run post-processing with PESummary to generate summary statistics and plots
2. Move results to the `results/` directory
3. Generate comprehensive HTML reports with visualization of the posterior distributions
4. Mark analyses as complete

You can then examine the results:

```bash
ls results/GW150914_095045/
```

## Next Steps

### Want to run more events?

Add another event to your existing project:

```bash
asimov gw events add GW151012_095443 --analyses production-default
```

Then:

```bash
asimov manage build && asimov manage submit
```

### Want to customize your analysis?

Edit `.asimov/ledger.yml` to adjust analysis settings like:
- Prior ranges for parameters
- Sampler settings
- Waveform approximants
- Data quality requirements

Then rebuild and resubmit:

```bash
asimov manage build && asimov manage submit
```

### Want to use a different pipeline?

Instead of `production-default`, you could use:
- `bilby-IMRPhenomXPHM` - Bilby only with the IMRPhenomXPHM waveform
- Custom analysis configurations

See `asimov gw analyses list` for all available options.

### Want to contribute to asimov?

Check out the [Contributing Guide](/contributing) to get involved with development!

## Troubleshooting

### "HTCondor not found"

Make sure HTCondor is installed and the `condor` commands are in your PATH:

```bash
which condor_q
```

If this fails, refer to the [Single-Machine Setup](#single-machine-setup-optional) appendix below.

### "Project ledger is corrupted"

If your `.asimov/ledger.yml` file becomes corrupted, you can regenerate it:

```bash
rm -rf .asimov/
asimov init "My Project"
asimov apply -f ...  # Re-apply your configurations
```

### "Job won't submit"

Check the working directory for HTCondor error logs:

```bash
cat working/GW150914_095045/Prod0/*.err
```

### "Results are missing"

Check that the job completed successfully:

```bash
asimov monitor
```

Look for status messages in `asimov.log`:

```bash
tail -n 100 asimov.log
```

---

## Appendix: Single-Machine Setup (Optional)

If you're working on a single machine without an existing HTCondor installation, you can use **HTCondor's mini version**, minicondor, which is designed for personal workstations.

### Installing Minicondor

HTCondor provides pre-built installers. Visit [htcondor.readthedocs.io](https://htcondor.readthedocs.io/en/latest/getting-htcondor/) and follow the installation guide for your operating system:

**On Linux (Ubuntu/Debian):**

```bash
# Add HTCondor repository
wget -qO - https://research.cs.wisc.edu/htcondor/yum/HTCondor/repo.key | sudo apt-key add -
echo "deb [arch=amd64] https://research.cs.wisc.edu/htcondor/yum/HTCondor/ubuntu focal main" | \
  sudo tee /etc/apt/sources.list.d/htcondor.list

# Install minicondor
sudo apt-get update
sudo apt-get install minicondor
```

**On macOS:**

```bash
# Using Homebrew
brew tap htcondor/htcondor
brew install htcondor
```

**On other systems:**

Follow the [official installation guide](https://htcondor.readthedocs.io/en/latest/getting-htcondor/) for your platform.

### Configuring Minicondor for Single-Machine Use

After installation, minicondor needs minimal configuration for single-machine use:

```bash
# Start the HTCondor daemon
sudo /etc/init.d/condor start

# Or on systems using systemd
sudo systemctl start condor
```

For personal workstations, you may want to limit resource usage. Edit `/etc/condor/condor_config.d/personal.conf` to set:

```
NUM_SLOTS = 1
NUM_SLOTS_TYPE_1 = 1
```

This ensures only one job runs at a time on your machine.

### Verifying Minicondor Installation

Test that HTCondor is working:

```bash
condor_q          # List jobs (should be empty)
condor_status     # Show available slots
```

Now you can follow the main tutorial above!

### Important Notes on Single-Machine Use

**Advantages:**
- Learn asimov on your personal computer
- Good for testing and development
- Useful for small analyses

**Limitations:**
- Jobs run sequentially on limited resources
- Parameter estimation analyses will be **very slow** on most personal computers
- Not suitable for production catalogue analyses

**For production work:** We recommend using institutional computing clusters with HTCondor, or work with your institution's computing facility to set up access.

### Future Improvements

We're actively working to make asimov easier to use without requiring HTCondor. Upcoming features will include:
- Direct cloud computing support (AWS, Google Cloud, etc.)
- Local multiprocessing support
- Slurm scheduler integration
- Better containerization

Stay tuned for updates!

