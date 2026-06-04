# Architecture

## Overview

The Ocean Infrastructure Intelligence Platform (OIIP) is an open-source geospatial intelligence platform designed to integrate oceanographic, infrastructure, environmental, energy, economic, and AI-related datasets into a unified analytical system.

The platform supports research, planning, and decision-making for:

* Ocean Thermal Energy Conversion (OTEC)
* Offshore Renewable Energy
* Marine Infrastructure
* Oceanographic Intelligence
* Climate Technology
* AI Datacenter Site Selection

---

# Architectural Principles

The architecture is guided by the following principles:

* Modular design
* Open standards
* Reproducible science
* Data-driven decision making
* Spatial-first architecture
* API-first development
* Cloud-native deployment
* Extensibility

---

# High-Level Architecture

```text
External Data Sources
        │
        ▼
Data Providers
        │
        ▼
Data Processing Pipelines
        │
        ▼
Spatial Data Platform (PostGIS)
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

---

# System Layers

The platform is organized into multiple layers.

## Data Provider Layer

Responsible for acquiring data from external systems.

Examples:

* Copernicus Marine Service
* NOAA
* GEBCO
* OpenStreetMap
* AIS Providers
* IBTrACS
* Infrastructure Datasets

Responsibilities:

* Authentication
* Data retrieval
* Metadata extraction
* Data normalization

---

## Processing Layer

Responsible for transforming raw data into platform-ready datasets.

Responsibilities:

* Validation
* Cleaning
* Harmonization
* Aggregation
* Feature extraction

Outputs:

* PostGIS records
* Parquet datasets
* Derived analytical layers

---

## Spatial Data Platform

The platform uses PostgreSQL with PostGIS as the primary data store.

Benefits:

* Spatial indexing
* Geospatial queries
* Spatial joins
* Distance calculations
* Geographic aggregation

All major analytical workflows are built around spatial operations.

---

# Core Domains

The platform is divided into several domains.

## Oceanography

Responsible for:

* Temperature profiles
* Salinity
* Ocean currents
* Waves
* Ocean depth

Example datasets:

* SST
* Thermocline profiles
* Bathymetry

---

## Infrastructure

Responsible for:

* Submarine cables
* Cable landing stations
* Ports
* Power grid assets
* Logistics infrastructure

Key questions:

* How far is a candidate site from infrastructure?
* What connectivity options exist?
* What logistics constraints apply?

---

## Energy

Responsible for:

* OTEC analysis
* Offshore wind
* Wave energy
* Hybrid systems

Capabilities:

* Resource estimation
* Power modeling
* Feasibility assessment

---

## Risk

Responsible for:

* Cyclones
* Tsunamis
* Shipping density
* Seismic activity

Outputs:

* Risk scores
* Historical risk assessments
* Site constraints

---

## Economics

Responsible for:

* CAPEX estimation
* OPEX estimation
* NPV calculations
* IRR calculations
* LCOE calculations

Outputs:

* Economic feasibility metrics
* Comparative analysis
* Scenario simulations

---

## AI Infrastructure

Responsible for:

* Datacenter suitability
* Cooling potential
* Infrastructure readiness
* Connectivity analysis

Primary output:

* AI Datacenter Suitability Index (ADCSI)

---

# Data Flow

The platform follows a staged processing model.

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

# Provider Architecture

Each provider follows a common structure.

```text
Provider
    │
    ├── Client
    ├── DTO
    ├── Mapper
    └── Service
```

Example:

```text
providers/

└── copernicus/
    ├── client.py
    ├── dto.py
    ├── mapper.py
    ├── provider.py
    └── service.py
```

Responsibilities:

* Download data
* Transform source formats
* Convert to internal models

---

# Storage Architecture

The platform uses multiple storage systems.

## PostgreSQL / PostGIS

Primary operational database.

Stores:

* Sites
* Oceanographic observations
* Infrastructure layers
* Scores
* Risk assessments

---

## Parquet

Used for:

* Analytical datasets
* Intermediate processing
* Large-scale data exports

---

## Object Storage

Used for:

* Raw datasets
* NetCDF files
* Raster layers
* Generated reports

Examples:

* MinIO
* S3-compatible storage

---

## Redis

Used for:

* Caching
* Temporary processing state
* Job coordination

---

# Geospatial Architecture

OIIP is fundamentally a spatial intelligence platform.

Coordinate Reference System:

```text
EPSG:4326
```

Supported geometries:

* Point
* LineString
* Polygon
* MultiPolygon

Common operations:

* Distance calculations
* Nearest infrastructure search
* Spatial overlays
* Spatial clustering
* Candidate site generation

---

# Candidate Site Model

A candidate site represents a potential ocean infrastructure location.

A site may include:

* Geographic coordinates
* Oceanographic characteristics
* Infrastructure metrics
* Risk indicators
* Economic indicators
* AI suitability indicators

All scoring systems operate on candidate sites.

---

# Scoring Architecture

Multiple independent scoring systems are combined into final rankings.

Examples:

* OTEC Score
* Infrastructure Score
* Risk Score
* Economic Score
* ADCSI Score

Final ranking:

```text
Site Score
    =
Weighted Combination
    of Domain Scores
```

Weighting models may evolve over time.

---

# API Architecture

The platform follows an API-first design.

Example domains:

```text
/api/sites
/api/maps
/api/reports
/api/search
/api/analytics
```

Responsibilities:

* Data access
* Search
* Filtering
* Reporting
* Integration

---

# Frontend Architecture

Planned frontend stack:

* Qwik
* TypeScript
* Leaflet
* MapLibre

Responsibilities:

* Interactive maps
* Layer visualization
* Site comparison
* Report generation

---

# AI Agent Architecture

Future versions may include specialized agents.

Examples:

* Research Agent
* Site Selection Agent
* Investment Agent
* Policy Agent

Potential capabilities:

* Dataset discovery
* Literature review
* Site recommendation
* Report generation

Agents should remain explainable and auditable.

---

# Security Architecture

Security considerations include:

* API authentication
* Secret management
* Dependency scanning
* Container security
* Data integrity

See:

```text
SECURITY.md
```

for detailed policies.

---

# Observability

Production deployments should include:

* Logging
* Metrics
* Health checks
* Performance monitoring

Planned tools:

* Prometheus
* Grafana
* Loki

---

# Deployment Architecture

Local Development:

```text
Developer
    │
    ▼
Docker Compose
    │
    ├── API
    ├── PostgreSQL
    ├── PostGIS
    ├── Redis
    └── MinIO
```

Production:

```text
Load Balancer
        │
        ▼
API Services
        │
        ▼
PostGIS Cluster
        │
        ▼
Object Storage
```

Future deployments may include Kubernetes and managed cloud services.

---

# Future Architecture Evolution

Future versions may introduce:

* Distributed processing
* Data lake architecture
* Real-time AIS ingestion
* Global-scale analytics
* Digital ocean twins
* Autonomous research agents

The architecture is intentionally modular to support future expansion without major redesign.

---

# Related Documents

Additional architecture documentation is located in:

```text
docs/architecture/
```

Planned documents include:

* system-overview.md
* erd.md
* api.md
* event-model.md
* deployment.md

These documents provide detailed specifications for individual subsystems.
