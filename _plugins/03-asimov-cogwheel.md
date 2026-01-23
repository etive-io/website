---
layout: item
title: asimov-cogwheel
type: parameter-estimation
status: stable
verified: true
github: https://github.com/etive-io/asimov-cogwheel
description: Cogwheel pipeline integration with efficient relative binning
maintainer: Etive.io
---

# asimov-cogwheel

Integration between Asimov and Cogwheel for fast parameter estimation using relative binning.

## Features

- **Efficient relative binning** approach reduces memory usage significantly
- **Fast likelihood evaluation** compared to traditional methods
- **Modern waveform models** supported including IMRPhenomXPHM
- **Scalable** to large-scale catalogue studies

## Installation

```bash
pip install asimov-cogwheel
```

## Quick Start

Use cogwheel analysis templates in your asimov project:

```bash
asimov gw events add GW150914_095045 --analyses cogwheel-default
```

## Documentation

- [Cogwheel GitHub Repository](https://github.com/jroulet/cogwheel)
- [Relative Binning Paper](https://arxiv.org/abs/1811.12907)

## Status

**Stable** - Production-ready for parameter estimation workflows

## Use Cases

- Fast parameter estimation when computational efficiency is important
- Large-scale catalogue analyses
- Parameter studies with many events
- Comparison with other waveform approximants
