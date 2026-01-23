---
layout: default
title: asimov-bilby
type: parameter-estimation
status: stable
verified: true
github: https://github.com/transientlunatic/asimov-bayeswave
description: Bilby pipeline integration for gravitational wave parameter estimation
maintainer: LIGO Scientific Collaboration
---

# asimov-bilby

Integration between Asimov and the Bilby inference library for gravitational wave parameter estimation.

## Features

- **Fast Bayesian inference** for parameter estimation
- **Multiple sampler support** including Dynesty and CPNest
- **Flexible waveform models** including IMRPhenomXPHM and other modern approximants
- **Parallelized likelihood evaluation** for efficient computation
- **Easy prior specification** through asimov blueprints

## Installation

```bash
pip install asimov-bilby
```

## Quick Start

Use the `production-default` analysis template in your asimov project:

```bash
asimov apply -f https://git.ligo.org/asimov/data/-/raw/main/analyses/production-default.yaml -e GW150914_095045
```

## Documentation

- [Bilby Documentation](https://lscsoft.docs.ligo.org/bilby/)
- [Asimov Getting Started Guide](/tutorials/analyzing-gw150914-with-asimov-0-7-0)

## Status

**Stable** - Actively maintained and production-ready

## Use Cases

- Parameter estimation for gravitational wave events
- Bayesian inference on detector data
- Waveform model comparison studies
