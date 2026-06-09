# Entity Relationship Diagram (ERD)

## Ocean Infrastructure Intelligence Platform (OIIP)

---

# Purpose

This document describes the logical data model of the Ocean Infrastructure Intelligence Platform (OIIP).

The platform integrates oceanographic, infrastructure, climate, economic, and policy datasets to support the evaluation and development of ocean infrastructure projects.

The data model is designed around two fundamental concepts:

1. Infrastructure Assets and Environmental Data
2. Ocean Infrastructure Projects

The Project is the primary business entity of the platform.

---

# High-Level Domain Model

```text
OceanInfrastructureProject
│
├── Site
├── ResourceAssessment
├── InfrastructureAssessment
├── ClimateAssessment
├── EconomicAssessment
├── PPPAssessment
├── NexusAssessment
├── BankabilityAssessment
├── Stakeholder
└── DevelopmentStage

Site
│
├── OceanObservation
├── BathymetryCell
├── ClimateHazard
├── Port
├── Shipyard
├── GridAsset
└── CableLandingStation
```

---

# Core Project Domain

## OceanInfrastructureProject

Represents a candidate, planned, active, or operational infrastructure project.

Examples:

* OTEC Plant
* SWAC System
* Desalination Facility
* Deep Ocean Water Facility
* Offshore AI Datacenter
* Hybrid Blue Economy Project

### Attributes

```text
project_id (UUID)
name
project_type
country_code
region
status
description
created_at
updated_at
```

### Relationships

```text
Project 1 → 1 Site
Project 1 → N Assessments
Project N ↔ N Stakeholders
Project 1 → 1 DevelopmentStage
```

---

## Site

Represents a geographic location evaluated by OIIP.

### Attributes

```text
site_id (UUID)
latitude
longitude
distance_to_shore_km
water_depth_m
exclusive_economic_zone
country_code
geometry
```

### Relationships

```text
Site 1 → N OceanObservation
Site 1 → N ClimateHazard
Site N ↔ N InfrastructureAsset
```

---

# Ocean Domain

## OceanObservation

Stores oceanographic measurements and derived values.

### Attributes

```text
observation_id
site_id
observation_date

sea_surface_temperature
temperature_200m
temperature_500m
temperature_1000m

salinity
current_velocity

data_source
```

### Derived Metrics

```text
thermal_gradient
cooling_potential
otec_resource_score
```

---

## BathymetryCell

Represents seabed characteristics.

### Attributes

```text
cell_id
geometry
depth_m
slope
distance_to_1000m_depth
source
```

### Purpose

Supports:

* OTEC
* SWAC
* Deep-water intake analysis
* Pipeline routing

---

# Infrastructure Domain

## InfrastructureAsset

Abstract parent entity.

### Types

```text
PORT
SHIPYARD
GRID_ASSET
SUBSTATION
POWER_PLANT
CABLE_LANDING_STATION
LOGISTICS_HUB
```

---

## Port

### Attributes

```text
port_id
name
country
capacity
draft_depth
coordinates
```

---

## Shipyard

### Attributes

```text
shipyard_id
name
country
fabrication_capabilities
heavy_lift_capacity
coordinates
```

---

## GridAsset

### Attributes

```text
grid_asset_id
asset_type
capacity_mw
operator
coordinates
```

---

## CableLandingStation

### Attributes

```text
landing_station_id
name
operator
connected_cables
coordinates
```

### Purpose

Critical for:

* AI Datacenter projects
* Offshore digital infrastructure

---

# Climate & Risk Domain

## ClimateHazard

Stores natural hazard data.

### Types

```text
CYCLONE
TSUNAMI
SEISMIC
EXTREME_WAVE
FLOODING
```

### Attributes

```text
hazard_id
hazard_type
severity
frequency
return_period
geometry
```

---

## ClimateAssessment

Evaluates survivability of infrastructure.

### Attributes

```text
assessment_id
project_id

cyclone_risk_score
wave_risk_score
tsunami_risk_score
seismic_risk_score

resilience_score
assessment_date
```

---

# Economic Domain

## EconomicAssessment

Evaluates project economics.

### Attributes

```text
assessment_id
project_id

capex_usd
opex_usd_year

lcoe
npv
irr
payback_period_years

economic_score
assessment_date
```

---

## BankabilityAssessment

Evaluates financing readiness.

### Attributes

```text
assessment_id
project_id

investment_score
funding_readiness_score
climate_impact_score

bankability_score

assessment_date
```

### Purpose

Primary output for:

* Investors
* Infrastructure Funds
* Development Banks

---

# Policy & PPP Domain

## PPPAssessment

Evaluates institutional readiness.

### Attributes

```text
assessment_id
project_id

regulatory_score
policy_alignment_score
utility_readiness_score
financing_availability_score

ppp_score
assessment_date
```

---

# Blue Economy Domain

## NexusAssessment

Evaluates secondary value opportunities.

### Attributes

```text
assessment_id
project_id

desalination_score
aquaculture_score
cooling_score
hydrogen_score

nexus_score
assessment_date
```

### Purpose

Identifies additional revenue streams and economic benefits.

---

# Stakeholder Domain

## Stakeholder

Represents organizations involved in a project.

### Types

```text
GOVERNMENT
DEVELOPER
INVESTOR
UTILITY
DEVELOPMENT_BANK
RESEARCH_INSTITUTION
TECHNOLOGY_PROVIDER
NGO
```

### Attributes

```text
stakeholder_id
name
stakeholder_type
country
website
```

---

## ProjectStakeholder

Many-to-many relationship.

### Attributes

```text
project_id
stakeholder_id
role
```

### Roles

```text
PROJECT_OWNER
INVESTOR
OFFTAKER
REGULATOR
TECHNICAL_PARTNER
FINANCIAL_PARTNER
```

---

# Development Lifecycle Domain

## DevelopmentStage

Tracks project maturity.

### Stages

```text
IDEA
PRE_SCREENING
PRE_FEASIBILITY
FEASIBILITY
PPP_DEVELOPMENT
FINANCING
ENGINEERING
CONSTRUCTION
OPERATION
DECOMMISSIONING
```

### Attributes

```text
project_id
current_stage
stage_started_at
updated_at
```

---

# Assessment Framework

All project intelligence assessments follow a common structure.

## Assessment Base Model

```text
assessment_id
project_id
assessment_date
data_version
methodology_version
score
```

Specialized assessments inherit this structure:

* ResourceAssessment
* InfrastructureAssessment
* ClimateAssessment
* EconomicAssessment
* PPPAssessment
* NexusAssessment
* BankabilityAssessment

---

# Project Intelligence Score

The primary analytical output of OIIP.

```text
Project Intelligence Score =
Resource Score
+ Infrastructure Score
+ Climate Resilience Score
+ Economic Score
+ PPP Score
+ Nexus Score
+ Bankability Score
```

Produces:

```text
Ocean Infrastructure Project Intelligence Report
```

---

# Architectural Principle

The platform is project-centric.

A Site is a location.

A Project is an investment opportunity.

Therefore:

```text
OceanInfrastructureProject
    owns
        Site
```

rather than:

```text
Site
    owns
        Project
```

This principle guides the entire data model and future platform evolution.
