---
layout: item
title: asimov-gracedb
type: utility
status: development
verified: true
github: https://github.com/etive-io/asimov-gracedb
description: GraceDB integration for event and superevent lookup
maintainer: Daniel Williams
---

# asimov-gracedb

Integration between Asimov and GraceDB, the gravitational-wave candidate event database.

## Features

- **Event and superevent lookup** directly from Asimov via `asimov apply -p gracedb`
- **Optional dependency** - moved out of Asimov core so `ligo-gracedb` isn't a hard dependency of the base package
- **Hook-based architecture** implementing Asimov's applicator and filesource plugin interfaces

## Installation

```bash
pip install asimov-gracedb
```

## Purpose

GraceDB is the database LIGO/Virgo/KAGRA use to track candidate gravitational-wave events and superevents. This plugin lets Asimov create and populate projects directly from GraceDB records without requiring every Asimov installation to depend on the GraceDB client.

## Documentation

- [asimov-gracedb README](https://github.com/etive-io/asimov-gracedb#readme)
- [GraceDB](https://gracedb.ligo.org/)

## Status

**Development** - Early-stage plugin, no tagged releases yet

## Use Cases

- Creating Asimov projects from a GraceDB superevent or event ID
- Keeping event metadata in sync with GraceDB without a core dependency
