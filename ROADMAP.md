# Roadmap

This roadmap outlines the planned evolution of the Ocean Infrastructure Intelligence Platform (OIIP).

The roadmap is intended as a strategic guide rather than a strict schedule. Priorities may evolve as new contributors, datasets, technologies, and research opportunities emerge.

---

# Vision

Build an open-source geospatial intelligence platform that combines oceanographic, infrastructure, environmental, energy, and economic datasets into a unified system for ocean infrastructure analysis and decision support.

Long-term goals include:

* Ocean Thermal Energy Conversion (OTEC)
* Offshore Renewable Energy
* Marine Infrastructure Analytics
* AI Datacenter Site Selection
* Climate Technology Research
* Ocean Intelligence Systems

---

# Phase 0 — Foundation

Status: In Progress

Objectives:

* Establish project organization
* Define governance model
* Define contribution process
* Design system architecture
* Define data model
* Create project documentation

Deliverables:

* README.md
* CONTRIBUTING.md
* CODE_OF_CONDUCT.md
* SECURITY.md
* GOVERNANCE.md
* SUPPORT.md
* ROADMAP.md

Success Criteria:

* Public GitHub organization established
* Core documentation completed
* Initial architecture approved

---

# Phase 1 — Core Platform

Objectives:

* Create backend foundation
* Deploy PostgreSQL/PostGIS
* Build provider framework
* Implement configuration system
* Establish CI/CD pipeline

Deliverables:

* FastAPI backend
* PostGIS integration
* Repository structure
* Docker environment
* GitHub Actions workflows

Success Criteria:

* Local deployment working
* Automated tests running
* Spatial database operational

---

# Phase 2 — Oceanographic Data Layer

Objectives:

* Integrate oceanographic datasets
* Build data synchronization pipelines
* Store ocean profiles
* Create temperature analysis tools

Data Sources:

* Copernicus Marine Service
* NOAA
* GEBCO

Deliverables:

* Copernicus provider
* NOAA provider
* Bathymetry ingestion
* Ocean profile storage

Success Criteria:

* Automated data synchronization
* Historical temperature storage
* Spatial queries operational

---

# Phase 3 — Thailand OTEC Research MVP

Objectives:

* Focus on Thailand
* Analyze Andaman Sea
* Analyze Gulf of Thailand
* Identify potential OTEC sites

Deliverables:

* Thermal gradient calculations
* Candidate site database
* OTEC suitability scoring
* Initial reports

Success Criteria:

* Ranked candidate locations
* Interactive site database
* Reproducible analysis workflow

---

# Phase 4 — Infrastructure Intelligence

Objectives:

* Integrate infrastructure datasets
* Analyze connectivity
* Evaluate logistics

Data Sources:

* OpenStreetMap
* Submarine cable datasets
* Port datasets
* Power infrastructure datasets

Deliverables:

* Cable analysis engine
* Port analysis engine
* Infrastructure scoring

Success Criteria:

* Infrastructure layer integrated
* Distance calculations operational
* Site connectivity scoring available

---

# Phase 5 — Risk Intelligence

Objectives:

* Evaluate environmental and operational risks

Data Sources:

* IBTrACS
* Shipping data
* Seismic datasets
* Wave and storm datasets

Deliverables:

* Cyclone risk model
* Shipping density model
* Risk scoring engine

Success Criteria:

* Risk-adjusted site rankings
* Historical event analysis

---

# Phase 6 — Economics Engine

Objectives:

* Evaluate project feasibility

Models:

* CAPEX
* OPEX
* NPV
* IRR
* LCOE

Deliverables:

* Economic simulation framework
* Monte Carlo engine
* Sensitivity analysis

Success Criteria:

* Economic ranking available
* Scenario modeling supported

---

# Phase 7 — AI Datacenter Suitability Index (ADCSI)

Objectives:

* Develop a methodology for evaluating AI infrastructure opportunities

Evaluation Areas:

* Cooling potential
* Energy availability
* Connectivity
* Infrastructure readiness
* Environmental risk

Deliverables:

* ADCSI framework
* Ranking engine
* Site comparison tools

Success Criteria:

* Operational ADCSI scoring
* Regional ranking reports

---

# Phase 8 — Interactive GIS Platform

Objectives:

* Build public visualization tools

Deliverables:

* Interactive maps
* Site explorer
* Layer management
* Search capabilities

Technology:

* Qwik
* TypeScript
* Leaflet
* MapLibre

Success Criteria:

* Public dashboard available
* Interactive spatial analysis supported

---

# Phase 9 — AI Research Agents

Objectives:

* Introduce AI-assisted research workflows

Agents:

* Research Agent
* Site Selection Agent
* Investment Agent
* Policy Agent

Capabilities:

* Dataset discovery
* Literature review
* Site evaluation
* Report generation

Success Criteria:

* Agent-assisted workflows operational

---

# Phase 10 — Southeast Asia Coverage

Objectives:

Expand beyond Thailand.

Regions:

* Indonesia
* Philippines
* Vietnam
* Malaysia
* Pacific Islands

Success Criteria:

* Regional datasets integrated
* Multi-country analysis supported

---

# Phase 11 — Global Tropical Ocean Coverage

Objectives:

Expand to all major tropical ocean regions.

Regions:

* Pacific Ocean
* Indian Ocean
* Atlantic Ocean
* Caribbean
* Equatorial Regions

Success Criteria:

* Global candidate database
* Global ranking system

---

# Phase 12 — Ocean Infrastructure Intelligence Platform 1.0

Objectives:

Release the first stable version of OIIP.

Deliverables:

* Production-ready platform
* Public API
* GIS dashboard
* Analytics engine
* Documentation portal

Success Criteria:

* Version 1.0 release
* Stable architecture
* Public adoption

---

# Milestones

## M0 — PostGIS Foundation Complete ✅

Completed:

- PostgreSQL 17 deployed
- PostGIS 3.5 deployed
- SQLAlchemy configured
- Alembic configured
- First migration created
- Site entity implemented
- Spatial geometry column enabled
- First spatial record inserted
- First PostGIS queries executed

Status:
DONE

## M1 — Core Site Domain Model Complete ✅

- Site
- Geometry(Point,4326)
- GIST index
- SiteStatus Enum
- Validation
- created_at
- updated_at
- description
- country_code constraint
- latitude property
- longitude property
- Site ORM model
- PostGIS POINT geometry
- Lifecycle enum
- Country code validation
- Server-side timestamps
- Geometry helper properties (latitude/longitude)

## Epic 2 — Ocean Data Intelligence Layer

### Goal

Transform OIIP from a synthetic analytical prototype into a real-world ocean intelligence platform powered by scientific datasets.

The objective of this epic is to automatically derive OTEC suitability assessments directly from oceanographic and bathymetric observations instead of manually constructed analytical profiles.

---

### Strategic Outcome

Current workflow:

Site → Manual Temperature Profile → OTEC Analysis

Target workflow:

Coordinates → Ocean Data Retrieval → OTEC Analysis → Suitability Report

After completing this epic, OIIP will be able to evaluate any ocean location automatically using real scientific datasets.

---

### Milestone 2.1 — Ocean Observation Domain Model

Introduce a unified scientific observation model.

Deliverables:

* OceanObservation entity
* Temperature observations
* Depth observations
* Bathymetry observations
* Observation timestamps
* Spatial coordinates support

Example:

```python
@dataclass(frozen=True)
class OceanObservation:
    longitude: float
    latitude: float
    timestamp: datetime

    surface_temperature_c: float

    depth_100m_temperature_c: float
    depth_500m_temperature_c: float
    depth_1000m_temperature_c: float

    seafloor_depth_m: float
```

Success Criteria:

* Single scientific data model established
* Independent from data providers
* Reusable across all analytics modules

---

### Milestone 2.2 — GEBCO Bathymetry Integration

Integrate global bathymetric datasets.

Data Source:

* GEBCO Global Bathymetry

Capabilities:

* Retrieve seafloor depth
* Calculate distance to critical isobaths
* Generate BathymetryProfile automatically

Outputs:

* BathymetryProfile
* Distance to 500m contour
* Distance to 1000m contour
* Distance to 1500m contour

Success Criteria:

* Automatic bathymetric assessment from coordinates

---

### Milestone 2.3 — Ocean Temperature Data Adapters

Integrate oceanographic temperature datasets.

Primary Sources:

* Copernicus Marine
* NOAA World Ocean Atlas
* Argo Profiles

Capabilities:

* Surface temperature retrieval
* Deep-water temperature retrieval
* Seasonal climatology generation
* Monthly thermal observations

Outputs:

* TemperatureProfile
* HydroclimatologyProfile

Success Criteria:

* Generate thermal profiles without manual inputs

---

### Milestone 2.4 — Site Assessment Engine

Create a high-level analytical service.

Interface:

```python
report = site_assessment_service.evaluate(
    longitude=98.45,
    latitude=8.12,
)
```

Processing Pipeline:

1. Retrieve ocean observations
2. Build bathymetry profile
3. Build climatology profile
4. Run OTEC analysis
5. Run MCDA scoring
6. Generate suitability report

Output:

```python
OtecSuitabilityReport
```

Success Criteria:

* Fully automated site evaluation

---

### Milestone 2.5 — Thailand Ocean Coverage MVP

Generate the first national-scale suitability map.

Regions:

* Gulf of Thailand
* Andaman Sea

Capabilities:

* Grid-based analysis
* Automatic ranking
* Tier classification

Outputs:

* Tier 1 locations
* Tier 2 locations
* Tier 3 locations
* Rejected locations

Success Criteria:

* Complete Thailand OTEC suitability dataset

---

### Deliverables

* OceanObservation model
* GEBCO adapter
* Copernicus adapter
* NOAA adapter
* Automated profile generation
* Site Assessment Engine
* Thailand coverage dataset

---

### Definition of Done

The following workflow must work without manual analytical inputs:

```python
report = site_assessment_service.evaluate(
    longitude=98.45,
    latitude=8.12,
)
```

The system automatically retrieves scientific data, evaluates OTEC viability, applies bathymetric and climatological constraints, and produces a complete investment-grade OtecSuitabilityReport.


---

# Future Research Areas

Potential future expansion areas include:

* Floating AI Datacenters
* Deep Ocean Cooling Systems
* Offshore Hydrogen Production
* Ocean Carbon Capture
* Marine Robotics
* Autonomous Ocean Monitoring
* Ocean Digital Twins
* Floating Energy Parks

---

# Guiding Principles

The roadmap is guided by the following principles:

* Open Science
* Open Data
* Open Standards
* Scientific Integrity
* Reproducibility
* Transparency
* Long-Term Sustainability

---

# Community Participation

Contributors are encouraged to:

* Suggest improvements
* Propose new milestones
* Participate in discussions
* Share research
* Contribute datasets
* Build tools and integrations

The future of OIIP will be shaped by its community and contributors.
