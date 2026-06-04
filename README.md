# Ocean Infrastructure Intelligence Platform (OIIP)

> Open-source geospatial intelligence platform for ocean energy, marine infrastructure, oceanographic analytics, and AI datacenter site selection.

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Status](https://img.shields.io/badge/status-early%20development-orange.svg)
![Python](https://img.shields.io/badge/python-3.13+-green.svg)
![PostGIS](https://img.shields.io/badge/PostGIS-enabled-blue.svg)

---

## Vision

The world's oceans contain vast untapped resources for sustainable energy production, cooling infrastructure, telecommunications, and next-generation AI computing facilities.

The Ocean Infrastructure Intelligence Platform (OIIP) aims to provide an open-source geospatial intelligence framework that integrates oceanographic, infrastructure, environmental, and economic datasets into a unified decision-support platform.

The platform is designed to help researchers, engineers, investors, policymakers, and climate-tech innovators identify and evaluate opportunities for:

* Ocean Thermal Energy Conversion (OTEC)
* Offshore Renewable Energy
* AI Datacenter Site Selection
* Submarine Cable Infrastructure
* Maritime Logistics
* Ocean Infrastructure Development
* Climate Technology Projects

---

## Mission

Build open tools, datasets, and intelligence systems that help researchers, engineers, organizations, and governments better understand and develop sustainable ocean infrastructure.

---

## Core Concepts

The platform combines multiple data layers:

```text
Oceanography
    +
Infrastructure
    +
Energy
    +
Risk
    +
Economics
    +
AI Infrastructure
    =
Ocean Intelligence
```

Each layer contributes information used to evaluate candidate locations for future ocean infrastructure development.

---

## Key Objectives

### Ocean Energy

* Analyze OTEC potential
* Evaluate thermal gradients
* Assess offshore renewable energy opportunities
* Model power generation scenarios

### Ocean Infrastructure

* Map submarine cable networks
* Analyze coastal infrastructure
* Evaluate port accessibility
* Assess grid connectivity

### Ocean Intelligence

* Integrate oceanographic datasets
* Analyze bathymetry
* Study ocean currents
* Evaluate environmental constraints

### AI Datacenter Intelligence

* Identify suitable locations for AI-ready infrastructure
* Evaluate cooling potential
* Assess connectivity and power availability
* Model long-term operational costs

---

## Architecture

```text
External Data Sources
        │
        ▼
 Data Providers
        │
        ▼
 Processing Pipelines
        │
        ▼
 Spatial Database
    (PostGIS)
        │
        ├── Analytics Engine
        ├── Scoring Engine
        ├── Economic Models
        └── AI Agents
                │
                ▼
            API Layer
                │
                ▼
          Web Dashboard
```

### Architecture Documentation

| Document                                                                     | Description                                 |
| ---------------------------------------------------------------------------- | ------------------------------------------- |
| [ARCHITECTURE.md](ARCHITECTURE.md)                                           | Platform architecture overview              |
| [docs/architecture/system-overview.md](docs/architecture/system-overview.md) | High-level technical specification          |
| [docs/architecture/erd.md](docs/architecture/erd.md)                         | PostGIS data model and entity relationships |

---

## Main Components

### Oceanography

* Sea Surface Temperature (SST)
* Deep Water Temperature
* Thermal Profiles
* Salinity
* Ocean Currents
* Waves
* Bathymetry

### Energy

* OTEC Modeling
* Offshore Wind
* Wave Energy
* Hybrid Energy Systems

### Infrastructure

* Submarine Cables
* Cable Landing Stations
* Ports
* Electrical Grid Assets
* Logistics Infrastructure

### Risk Analysis

* Cyclones
* Tsunami Risk
* Shipping Density
* Seismic Activity

### Economics

* CAPEX
* OPEX
* NPV
* IRR
* LCOE
* Monte Carlo Simulation

### AI Infrastructure

* AI Datacenter Suitability Index (ADCSI)
* Cooling Potential Assessment
* Connectivity Analysis
* Infrastructure Readiness Evaluation

---

## AI Datacenter Suitability Index (ADCSI)

One of the primary goals of OIIP is the development of the AI Datacenter Suitability Index (ADCSI).

ADCSI evaluates locations based on:

* Energy Availability
* Ocean Cooling Potential
* Connectivity
* Cable Proximity
* Infrastructure Readiness
* Environmental Risk
* Logistics Accessibility

The objective is to identify optimal locations for future AI infrastructure powered by sustainable ocean-based energy systems.

---

## Technology Stack

### Backend

* Python 3.13+
* FastAPI
* SQLAlchemy
* PostgreSQL
* PostGIS
* Redis

### Scientific Computing

* NumPy
* SciPy
* Pandas
* Xarray
* Dask

### Geospatial

* GeoPandas
* GDAL
* Shapely
* PyProj

### Frontend

* Qwik
* TypeScript
* Leaflet
* MapLibre

### Infrastructure

* Docker
* GitHub Actions
* Terraform

### AI & Agents

* OpenAI SDK
* LangGraph
* MCP
* Agent-to-Agent (A2A)

---

## Repository Structure

```text
.
├── backend/
│   ├── api/
│   ├── providers/
│   ├── analytics/
│   ├── scoring/
│   ├── economics/
│   └── agents/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── maps/
│   └── routes/
│
├── database/
│   ├── migrations/
│   ├── schemas/
│   └── seeds/
│
├── docs/
│   └── architecture/
│
├── infra/
│   ├── docker/
│   ├── terraform/
│   └── kubernetes/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
│
├── notebooks/
├── scripts/
├── tests/
└── .github/
```

See:

* [ARCHITECTURE.md](ARCHITECTURE.md)
* [docs/architecture/system-overview.md](docs/architecture/system-overview.md)
* [docs/architecture/erd.md](docs/architecture/erd.md)

---

## Project Documentation

### Getting Started

* [README.md](README.md)
* [ROADMAP.md](ROADMAP.md)
* [SUPPORT.md](SUPPORT.md)

### Community

* [CONTRIBUTING.md](CONTRIBUTING.md)
* [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
* [GOVERNANCE.md](GOVERNANCE.md)

### Security

* [SECURITY.md](SECURITY.md)

### Architecture

* [ARCHITECTURE.md](ARCHITECTURE.md)
* [docs/architecture/system-overview.md](docs/architecture/system-overview.md)
* [docs/architecture/erd.md](docs/architecture/erd.md)

---

## Initial Geographic Focus

### Phase 1

Primary research region:

* Thailand
* Gulf of Thailand
* Andaman Sea

### Phase 2

Regional expansion:

* Indonesia
* Philippines
* Vietnam
* Malaysia

### Phase 3

Global tropical ocean coverage:

* Pacific Ocean
* Indian Ocean
* Atlantic Ocean
* Caribbean Region

---

## Current Research Focus

The project currently prioritizes research related to:

* Thailand OTEC opportunities
* Gulf of Thailand thermal gradients
* Andaman Sea energy potential
* Offshore infrastructure mapping
* Submarine cable connectivity
* AI datacenter site selection
* Ocean-based cooling systems

The initial goal is to identify and evaluate candidate locations for sustainable ocean infrastructure development in Southeast Asia.

---

## Roadmap

The long-term development plan is maintained in:

* [ROADMAP.md](ROADMAP.md)

Current priorities include:

* PostGIS foundation
* Oceanographic data ingestion
* Thailand OTEC research
* Infrastructure intelligence
* AI Datacenter Suitability Index (ADCSI)
* Interactive GIS platform

---

## Community

We welcome contributions from:

* Software Engineers
* GIS Specialists
* Oceanographers
* Marine Engineers
* Climate-Tech Researchers
* Data Scientists
* Infrastructure Analysts
* Students and Open-Source Contributors

Before contributing, please review:

* [CONTRIBUTING.md](CONTRIBUTING.md)
* [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
* [GOVERNANCE.md](GOVERNANCE.md)

Questions and support:

* [SUPPORT.md](SUPPORT.md)

---

## Research and Data Sources

The project plans to integrate publicly available datasets from organizations such as:

* Copernicus Marine Service
* NOAA
* GEBCO
* OpenStreetMap
* IBTrACS
* National Oceanographic Institutions

All dataset ownership remains with their respective providers.

---

## Security

Please review:

* [SECURITY.md](SECURITY.md)

Do not report security vulnerabilities through public GitHub Issues.

Follow the responsible disclosure process described in the Security Policy.

---

## Project Status

Current Stage:

```text
Phase 0 — Foundation
```

Completed:

* Project vision and mission
* Governance model
* Community guidelines
* Security policy
* Initial architecture
* Initial ERD design

In Progress:

* PostGIS schema implementation
* Data provider framework
* Thailand OTEC research MVP

---

## License

Licensed under the Apache License 2.0.

See:

```text
LICENSE
```

---

## Organization

GitHub Organization:

https://github.com/ocean-infrastructure-intelligence

---

## Mission Statement

Building open tools and intelligence systems for:

* Ocean Infrastructure Intelligence
* Ocean Thermal Energy Conversion (OTEC)
* Offshore Renewable Energy
* Marine Infrastructure Analytics
* Oceanographic Data Integration
* AI Datacenter Site Selection
* Sustainable Ocean Development

Together, we are building open science, open data, and open-source technology for the future of ocean infrastructure intelligence.
