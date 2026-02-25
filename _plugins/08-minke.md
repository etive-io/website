---
layout: item
title: Minke
type: simulation
status: stable
verified: true
github: https://github.com/transientlunatic/minke
description: Gravitational wave signal injection and simulation
maintainer: Daniel Williams
---

# Minke

Asimov plugin for Minke - automated gravitational wave signal injection for testing and validation.

## Features

- **Realistic signal injection** into detector data
- **Multiple source population models** (BNS, BBH, NSBH)
- **Sensitivity studies** and pipeline validation
- **Detector characterization** for analysis vetting

## Installation

```bash
pip install minke
```

## Quick Start

Add injections to your asimov workflow:

```yaml
kind: analysis
name: injections
pipeline: minke
source:
  type: population
  model: BBH
```

## Documentation

- [Minke Documentation](https://minke.readthedocs.io/)
- [Using Minke with Asimov](/tutorials/using-minke-with-asimov)
- [Signal Injection Best Practices](https://github.com/transientlunatic/minke)

## Status

**Stable** - Production-ready for injection studies

## Use Cases

- Sensitivity studies and pipeline validation
- False alarm rate estimation
- Pipeline efficiency characterization
- Binary population studies
- Signal search optimization
