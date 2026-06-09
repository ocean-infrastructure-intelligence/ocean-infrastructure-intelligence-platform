# Project Intelligence Model

## Ocean Infrastructure Intelligence Platform (OIIP)

---

# Purpose

This document defines the primary business object of OIIP.

The platform is no longer centered around geographic locations.

The platform is centered around infrastructure projects.

The objective of OIIP is to transform ocean data into investment-ready project intelligence.

---

# Core Business Entity

```text
OceanInfrastructureProject
```

Everything in the platform exists to support the evaluation, development, financing, and operation of a project.

---

# Conceptual Model

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
├── Stakeholders
└── DevelopmentStage
```

---

# OceanInfrastructureProject

Represents a candidate or active infrastructure development opportunity.

Examples:

* OTEC Plant
* SWAC System
* Desalination Facility
* Deep Ocean Water Facility
* Offshore AI Datacenter
* Hybrid Blue Economy Project

---

## Core Attributes

```text
project_id
name
country
region
project_type
status
created_at
updated_at
```

---

## Project Types

```text
OTEC
SWAC
DESALINATION
AI_DATACENTER
BLUE_ECONOMY_HUB
HYBRID
```

---

# Site

Represents the physical location.

```text
site_id
latitude
longitude
bathymetry
distance_to_shore
exclusive_economic_zone
```

Relationship:

```text
Project 1 → 1 Site
```

---

# Resource Assessment

Evaluates natural resources.

```text
resource_assessment
├── thermal_gradient
├── cooling_potential
├── ocean_depth
├── resource_score
└── assessment_date
```

Relationship:

```text
Project 1 → N ResourceAssessment
```

---

# Infrastructure Assessment

Evaluates buildability.

```text
infrastructure_assessment
├── nearest_port
├── nearest_shipyard
├── nearest_grid
├── nearest_cable
├── logistics_score
└── infrastructure_score
```

Relationship:

```text
Project 1 → N InfrastructureAssessment
```

---

# Climate Assessment

Evaluates survivability.

```text
climate_assessment
├── cyclone_risk
├── wave_risk
├── tsunami_risk
├── seismic_risk
└── resilience_score
```

Relationship:

```text
Project 1 → N ClimateAssessment
```

---

# Economic Assessment

Evaluates commercial viability.

```text
economic_assessment
├── capex
├── opex
├── lcoe
├── npv
├── irr
├── payback_period
└── economic_score
```

Relationship:

```text
Project 1 → N EconomicAssessment
```

---

# PPP Assessment

Evaluates institutional readiness.

```text
ppp_assessment
├── regulatory_score
├── climate_policy_score
├── utility_readiness
├── financing_availability
└── ppp_score
```

Relationship:

```text
Project 1 → N PPPAssessment
```

---

# Nexus Assessment

Evaluates secondary opportunities.

```text
nexus_assessment
├── desalination_score
├── aquaculture_score
├── cooling_score
├── hydrogen_score
└── nexus_score
```

Relationship:

```text
Project 1 → N NexusAssessment
```

---

# Bankability Assessment

Primary output for investors.

```text
bankability_assessment
├── risk_adjusted_irr
├── funding_readiness
├── climate_impact
├── investment_score
└── bankability_score
```

Relationship:

```text
Project 1 → N BankabilityAssessment
```

---

# Stakeholders

Represents project participants.

```text
Stakeholder
├── id
├── name
├── type
└── role
```

Types:

```text
Government
Developer
Investor
Utility
DevelopmentBank
ResearchInstitution
TechnologyProvider
```

Relationship:

```text
Project N ↔ N Stakeholder
```

---

# Development Stage

Tracks project maturity.

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
```

---

# Project Intelligence Score

The platform's primary KPI.

```text
Project Intelligence Score =
Resource
+
Infrastructure
+
Climate
+
Economics
+
PPP
+
Nexus
+
Bankability
```

Produces:

```text
Project Intelligence Report
```

---

# Architectural Principle

A Site is a location.

A Project is an opportunity.

OIIP is designed to evaluate opportunities, not locations.

Therefore:

```text
Project
    owns
        Site
```

not

```text
Site
    owns
        Project
```
