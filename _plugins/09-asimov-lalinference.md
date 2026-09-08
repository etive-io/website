---
layout: item
title: asimov-lalinference
type: parameter-estimation
status: development
verified: true
github: https://github.com/etive-io/asimov-lalinference
description: LALInference pipeline integration for parameter estimation
maintainer: Daniel Williams
---

# asimov-lalinference

Integration between Asimov and LALInference, the LIGO Algorithm Library's parameter estimation pipeline.

## Features

- **Plugin architecture** integrating with Asimov via entry points
- **Compatible with Asimov 0.7+** blueprint-driven project configuration
- **Support for cross-checks** against results from newer pipelines

## Installation

```bash
pip install asimov-lalinference
```

## Purpose

LALInference was the original Bayesian parameter estimation pipeline used across LIGO/Virgo analyses. It has been superseded by newer sampling pipelines such as bilby and RIFT, and this integration is not fully reviewed.

> **Warning:** This plugin must not be used for collaboration parameter estimation analyses. It remains useful for cross-checks and for replicating older analyses.

## Documentation

- [asimov-lalinference documentation](https://etive-io.github.io/asimov-lalinference/)
- [LALSuite](https://github.com/lscsoft/lalsuite)

## Status

**Development** - Not fully reviewed; retained for cross-checks and legacy replication only

## Use Cases

- Replicating results from older LALInference-based analyses
- Cross-checking newer-pipeline results against legacy methodology
