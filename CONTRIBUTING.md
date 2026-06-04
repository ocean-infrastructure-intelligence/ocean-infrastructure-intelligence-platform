# Contributing to Ocean Infrastructure Intelligence Platform (OIIP)

First of all, thank you for considering contributing to the Ocean Infrastructure Intelligence Platform (OIIP).

OIIP is an open-source initiative focused on ocean energy, marine infrastructure, oceanographic intelligence, and AI datacenter site selection. We welcome contributions from software engineers, GIS specialists, oceanographers, researchers, climate-tech professionals, students, and open-source contributors.

---

# Our Mission

Our goal is to build an open, transparent, and scientifically grounded platform for analyzing ocean infrastructure opportunities worldwide.

The project focuses on:

* Ocean Thermal Energy Conversion (OTEC)
* Oceanography and marine analytics
* Offshore renewable energy
* Submarine cable infrastructure
* Maritime logistics
* AI datacenter site selection
* Climate technology

---

# Ways to Contribute

You can contribute in many ways:

## Software Development

* Backend development
* Frontend development
* GIS development
* API development
* Database design
* Infrastructure automation

## Scientific Contributions

* Oceanography
* Marine engineering
* Energy modeling
* Climate science
* Environmental analysis
* Economic modeling

## Data Contributions

* Public datasets
* Data processing pipelines
* Metadata improvements
* Data validation

## Documentation

* Technical documentation
* Tutorials
* Architecture documentation
* Research summaries

---

# Before You Start

Please:

* Read the README.md
* Review the project architecture documentation
* Search existing issues before creating a new one
* Discuss large changes before implementation

For major changes, create an issue first.

---

# Development Workflow

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

4. Push your branch

5. Open a Pull Request

---

# Commit Message Convention

We use Conventional Commits.

Examples:

```text
feat: add Copernicus temperature provider

fix: correct shoreline distance calculation

docs: update architecture documentation

refactor: simplify site ranking engine

test: add PostGIS repository tests
```

Common prefixes:

* feat
* fix
* docs
* refactor
* test
* chore
* ci

---

# Coding Standards

## Python

Requirements:

* Python 3.13+
* Type hints required
* Ruff
* Black
* Pytest

Example:

```python
def calculate_delta_t(
    surface_temp: float,
    deep_temp: float,
) -> float:
    return surface_temp - deep_temp
```

Avoid:

* Global mutable state
* Hidden side effects
* Unclear variable names

---

# Architecture Principles

We follow several core principles.

## Separation of Concerns

Keep layers independent:

* Providers
* Storage
* Geospatial
* Domain
* API

Avoid mixing responsibilities.

## Reproducibility

Scientific results should be reproducible.

All calculations should:

* Document assumptions
* Reference data sources
* Record calculation methods

## Open Standards

Prefer:

* GeoJSON
* NetCDF
* Parquet
* PostGIS
* Open APIs

---

# Geospatial Guidelines

Use:

* PostGIS for spatial storage
* EPSG:4326 for geographic coordinates
* Explicit CRS declarations

Always document:

* Coordinate system
* Units
* Data source

Avoid storing geometry without CRS information.

---

# Data Source Policy

OIIP integrates data from multiple external sources.

Examples:

* Copernicus Marine Service
* NOAA
* GEBCO
* OpenStreetMap
* IBTrACS

Contributors must:

* Respect source licenses
* Preserve attribution
* Avoid uploading copyrighted datasets

Whenever possible:

* Store metadata
* Store references
* Avoid storing duplicated source data

---

# Testing

All new code should include tests whenever practical.

Preferred structure:

```text
tests/

├── unit/
├── integration/
├── geospatial/
└── api/
```

Run tests before submitting:

```bash
pytest
```

---

# Documentation Requirements

New features should include:

* Code documentation
* Architecture updates (if applicable)
* Usage examples

Documentation is considered part of the contribution.

---

# Pull Requests

A good Pull Request should:

* Solve a single problem
* Include clear description
* Reference related issues
* Include tests where appropriate

Large Pull Requests may be asked to be split into smaller changes.

---

# Research Contributions

Research contributions are welcome.

Examples:

* OTEC studies
* Oceanographic reports
* Infrastructure analyses
* Technical papers
* Feasibility assessments

Please include:

* Sources
* Assumptions
* Methodology
* References

Scientific transparency is important.

---

# Code of Conduct

Be respectful.

We value:

* Scientific rigor
* Open collaboration
* Constructive discussion
* Evidence-based reasoning

Harassment, discrimination, or abusive behavior will not be tolerated.

---

# Recognition

All contributors help advance open knowledge about ocean infrastructure and sustainable energy systems.

Thank you for helping build Ocean Infrastructure Intelligence Platform.
