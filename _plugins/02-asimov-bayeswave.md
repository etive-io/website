---
layout: item
title: asimov-bayeswave
type: psd-estimation
status: stable
verified: true
github: https://github.com/transientlunatic/asimov-bayeswave
description: BayesWave pipeline integration for power spectral density estimation
maintainer: Daniel Williams
---

# asimov-bayeswave

Integration between Asimov and BayesWave for on-source power spectral density (PSD) estimation.

## Features

- **Robust on-source PSD estimation** using transient Bayesian inference
- **Glitch characterization** to identify non-Gaussian noise
- **Pre-processing** for parameter estimation pipelines
- **Automatic integration** with Asimov workflows

## Installation

```bash
pip install asimov-bayeswave
```

## Purpose

BayesWave analyzes the noise characteristics of the gravitational wave detectors around the time of a signal. This PSD estimate is then used by parameter estimation pipelines like Bilby to properly account for the detector noise properties.

## Documentation

- [BayesWave Documentation](https://git.ligo.org/lscsoft/bayeswave)
- [Using in Asimov](/tutorials/analyzing-gw150914-with-asimov-0-7-0)

## Status

**Stable** - Part of production LIGO/Virgo analysis workflows

## Use Cases

- On-source PSD estimation for parameter estimation
- Noise characterization during gravitational wave events
- Pre-processing stage in multi-pipeline analyses
