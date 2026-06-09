# Architecture

## Ocean Infrastructure Intelligence Platform (OIIP)

---

# Architectural Principle

OIIP is designed as a Project-Centric Decision Support System.

The primary domain entity is:

```text
OceanInfrastructureProject
```

All datasets, assessments, reports, and scores exist to evaluate projects.

---

# High-Level Architecture

```text
Frontend
      ↓
API Layer
      ↓
Application Layer
      ↓
Project Intelligence Engine
      ↓
Data Access Layer
      ↓
External Datasets
```

---

# Project Intelligence Model

```text
OceanInfrastructureProject
│
├── Resource Assessment
├── Climate Assessment
├── Economic Assessment
├── Infrastructure Assessment
├── Policy Assessment
├── Nexus Assessment
├── Bankability Assessment
│
└── Project Intelligence Score
```

---

# MVP Architecture

Version 1 implements:

```text
OceanInfrastructureProject
│
├── Resource Assessment
├── Climate Assessment
├── Economic Assessment
│
└── Project Intelligence Score
```

---

# Domain Layer

Responsibilities:

* Business rules
* Scoring logic
* Assessment models
* Project lifecycle

Core entities:

```text
Project
ResourceAssessment
ClimateAssessment
EconomicAssessment
ProjectIntelligenceScore
```

---

# Application Layer

Responsibilities:

* Orchestrate workflows
* Coordinate assessments
* Generate reports

Primary service:

```text
ProjectScreeningService
```

Workflow:

```text
Coordinates
      ↓
Resource Assessment
      ↓
Climate Assessment
      ↓
Economic Assessment
      ↓
Project Intelligence Score
      ↓
Project Intelligence Report
```

---

# Data Layer

Responsibilities:

* Dataset abstraction
* Metadata management
* Dataset orchestration

Domains:

* Ocean Data
* Climate Data
* Economic Data
* Infrastructure Data
* Policy Data

---

# Infrastructure Layer

Responsibilities:

* External API access
* Dataset ingestion
* Storage
* Caching

Examples:

* Copernicus
* NOAA
* GEBCO
* Argo
* World Bank
* IBTrACS

---

# Reporting Layer

Responsibilities:

* Report generation
* Markdown export
* HTML export
* PDF export

Outputs:

```text
Project Intelligence Report
Investment Screening Report
Government Planning Report
```

---

# Future Architecture

Future releases add:

* Infrastructure Intelligence
* Policy Intelligence
* Bankability Intelligence
* PPP Intelligence
* Portfolio Intelligence
* AI Datacenter Intelligence
* Digital Twin Intelligence

without changing the core project model.

---

# Design Principle

Every architectural component must contribute to answering:

> Should this infrastructure project move forward?
