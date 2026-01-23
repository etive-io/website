---
layout: item
title: asimov-gwdata
type: utility
status: stable
verified: true
github: https://github.com/etive-io/asimov-pipelines/tree/main/asimov-gwdata
description: Gravitational wave data discovery and retrieval plugin
maintainer: Etive.io
---

# asimov-gwdata

Plugin providing intelligent gravitational wave data discovery, event management, and quickstart infrastructure for asimov projects.

## Features

- **Event discovery** - Browse published gravitational wave events from catalogues
- **Smart project setup** - Create complete asimov projects with one command
- **Interactive wizard** - `asimov gw quickstart` for guided setup
- **Analysis templates** - Curated analysis configurations
- **Data caching** - Local cache of event and analysis metadata
- **Tab completion** - Shell completion for event and analysis names

## Installation

```bash
pip install asimov-gwdata
```

## Quick Start

Set up a new project interactively:

```bash
asimov gw quickstart
```

Or directly:

```bash
asimov gw setup --name my-analysis --events GW150914_095045 --analyses production-default
```

## Documentation

- [asimov-gwdata Quickstart Guide](/tutorials/analyzing-gw150914-with-asimov-0-7-0)
- [Event Discovery Commands](https://github.com/etive-io/asimov-pipelines/blob/main/asimov-gwdata/CLI_QUICK_REFERENCE.md)

## Status

**Stable** - Recommended starting point for new users

## Use Cases

- Discovering available gravitational wave events
- Quick project setup
- Event and analysis exploration
- Batch project creation
- Learning asimov
