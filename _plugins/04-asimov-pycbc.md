---
layout: item
title: asimov-pycbc
type: parameter-estimation
status: development
verified: true
github: https://github.com/etive-io/asimov-pycbc
description: PyCBC pipeline integration for parameter estimation
maintainer: Daniel Williams
---

# asimov-pycbc

Integration between Asimov and PyCBC for gravitational wave parameter estimation.

## Features

- **Flexible template banks** for waveform generation
- **Efficient heterodyne likelihood** computation
- **Integration with detector data streams**
- **Customizable priors** and analysis settings

## Installation

```bash
pip install asimov-pycbc
```

## Quick Start

Include PyCBC analyses in your asimov project:

```bash
asimov apply -f custom-analysis.yaml -e GW150914_095045
```

## Documentation

- [PyCBC Documentation](https://pycbc.org/)
- [PyCBC Inference Guide](https://pycbc.org/pycbc/latest/html/inference.html)

## Status

**Development** - Active development with new features being added

## Use Cases

- Parameter estimation with heterodyne likelihoods
- Custom waveform model testing
- PyCBC-specific analysis configurations
- Integration with PyCBC matchedfilter pipelines
