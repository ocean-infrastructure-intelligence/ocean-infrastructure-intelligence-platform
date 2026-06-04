# System Overview

## Purpose

The Ocean Infrastructure Intelligence Platform (OIIP) is an open-source geospatial intelligence system for evaluating ocean-based energy, infrastructure, and AI datacenter opportunities.

The platform integrates oceanographic, infrastructure, environmental, risk, and economic datasets into a unified spatial analytics environment.

Its primary objective is to identify and evaluate candidate locations for:

* Ocean Thermal Energy Conversion (OTEC)
* Offshore Renewable Energy
* AI Datacenters
* Marine Infrastructure Projects
* Climate Technology Initiatives

---

# Project Scope

OIIP is not a single-purpose OTEC calculator.

Instead, it serves as a spatial intelligence platform capable of supporting multiple ocean infrastructure use cases.

Current focus areas include:

* Oceanography
* OTEC
* Marine Infrastructure
* Submarine Cables
* Power Infrastructure
* Maritime Logistics
* Environmental Risk Assessment
* AI Datacenter Site Selection

---

# Core Concept

The platform combines multiple independent data layers.

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

Each layer contributes information used to evaluate candidate locations.

---

# High-Level System Architecture

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
        ├── Analytics
        ├── Scoring
        ├── Economics
        ├── GIS Services
        └── AI Agents
                │
                ▼
            API Layer
                │
                ▼
          Web Dashboard
```

---

# Major Subsystems

## Data Providers

Responsible for retrieving information from external systems.

Examples:

* Copernicus Marine Service
* NOAA
* GEBCO
* OpenStreetMap
* AIS Providers
* IBTrACS
* National Infrastructure Datasets

Responsibilities:

* Authentication
* Data Retrieval
* Metadata Collection
* Source Normalization

---

## Processing Pipelines

Transform raw datasets into platform-ready formats.

Responsibilities:

* Validation
* Cleaning
* Transformation
* Enrichment
* Aggregation

Outputs:

* PostGIS records
* Parquet datasets
* Derived analytical layers

---

## Spatial Data Platform

PostgreSQL + PostGIS is the central system of record.

Responsibilities:

* Spatial storage
* Spatial indexing
* Distance calculations
* Geospatial joins
* Candidate site storage

All major analytics depend on PostGIS.

---

## Analytics Engine

Performs scientific and engineering calculations.

Responsibilities:

* Thermal gradient analysis
* OTEC modeling
* Infrastructure analysis
* Risk calculations
* Site evaluation

Outputs:

* Metrics
* Scores
* Rankings

---

## Economic Engine

Evaluates project feasibility.

Responsibilities:

* CAPEX estimation
* OPEX estimation
* NPV calculations
* IRR calculations
* LCOE calculations
* Scenario analysis

Outputs:

* Economic indicators
* Investment attractiveness metrics

---

## Scoring Engine

Combines analytical results into decision-support metrics.

Examples:

* OTEC Score
* Infrastructure Score
* Risk Score
* Economic Score
* AI Datacenter Suitability Index (ADCSI)

Outputs:

* Site rankings
* Opportunity maps
* Comparative reports

---

## API Layer

Provides access to platform data and analytics.

Typical consumers:

* Web dashboard
* Research notebooks
* External applications
* AI agents

Example endpoints:

```text
/api/sites
/api/search
/api/maps
/api/analytics
/api/reports
```

---

## Web Dashboard

Provides interactive access to platform functionality.

Capabilities:

* Interactive maps
* Layer management
* Site search
* Site comparison
* Report generation

Planned technology stack:

* Qwik
* TypeScript
* Leaflet
* MapLibre

---

# Core Domains

The platform is organized around several domains.

## Oceanography

Responsible for:

* Temperature Profiles
* Sea Surface Temperature
* Deep Water Temperature
* Salinity
* Currents
* Waves
* Bathymetry

---

## Infrastructure

Responsible for:

* Submarine Cables
* Landing Stations
* Ports
* Logistics Assets
* Power Grid Infrastructure

---

## Energy

Responsible for:

* OTEC
* Offshore Wind
* Wave Energy
* Hybrid Energy Systems

---

## Risk

Responsible for:

* Cyclones
* Tsunamis
* Seismic Activity
* Shipping Density

---

## Economics

Responsible for:

* Financial Modeling
* Cost Estimation
* Feasibility Analysis

---

## AI Infrastructure

Responsible for:

* Datacenter Site Selection
* Cooling Potential
* Connectivity Analysis
* Infrastructure Readiness

---

# Candidate Site Model

A candidate site is the primary analytical object in the platform.

A site represents a potential location for future ocean infrastructure development.

Each site contains:

* Geographic Information
* Oceanographic Metrics
* Infrastructure Metrics
* Risk Indicators
* Economic Metrics
* Suitability Scores

All major analytics operate on candidate sites.

---

# Data Flow

The platform follows a reproducible data processing workflow.

```text
Acquire
    │
    ▼
Validate
    │
    ▼
Normalize
    │
    ▼
Store
    │
    ▼
Analyze
    │
    ▼
Score
    │
    ▼
Visualize
```

Each stage should be independently testable and reproducible.

---

# Geographic Focus

## Phase 1

Thailand

Focus areas:

* Gulf of Thailand
* Andaman Sea

---

## Phase 2

Southeast Asia

Target regions:

* Indonesia
* Philippines
* Vietnam
* Malaysia

---

## Phase 3

Global Tropical Ocean Belt

Coverage:

* Pacific Ocean
* Indian Ocean
* Atlantic Ocean
* Caribbean Region

---

# AI Datacenter Suitability Index (ADCSI)

ADCSI is a composite indicator designed to evaluate locations for future AI infrastructure.

Evaluation criteria include:

* Cooling Potential
* Energy Availability
* Cable Connectivity
* Infrastructure Readiness
* Environmental Risk
* Logistics Accessibility

The objective is to identify locations where ocean resources can support large-scale computing infrastructure.

---

# Non-Goals

OIIP is not intended to:

* Replace official oceanographic services
* Replace engineering feasibility studies
* Provide investment advice
* Act as a real-time operational control system

The platform is intended to support research, planning, and decision-making.

---

# Future Evolution

Planned future capabilities include:

* AI Research Agents
* Autonomous Site Discovery
* Digital Ocean Twins
* Real-Time AIS Processing
* Global Infrastructure Mapping
* Climate Impact Modeling
* Floating Datacenter Analysis

---

# Related Documents

For detailed architecture information see:

```text
docs/architecture/erd.md
docs/architecture/api.md
docs/architecture/event-model.md
docs/architecture/deployment.md
```

For contribution guidelines see:

```text
CONTRIBUTING.md
```

For project governance see:

```text
GOVERNANCE.md
```

For development plans see:

```text
ROADMAP.md
```
