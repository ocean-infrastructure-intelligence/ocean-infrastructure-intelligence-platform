# ADR-0001: Adopt a Project-Centric Domain Model

Status: Accepted

Date: 2026-06-09

Authors:

* Ocean Infrastructure Intelligence Platform Team

---

# Context

The initial versions of OIIP were designed around a geospatial "Site" concept.

The platform focused on identifying locations with favorable ocean characteristics for Ocean Thermal Energy Conversion (OTEC) and related marine infrastructure.

The core workflow was:

```text
Coordinates
    ↓
Site
    ↓
Analysis
```

This approach worked well for early experimentation and geospatial exploration.

However, further research, stakeholder interviews, and analysis of the ocean infrastructure industry revealed a fundamental limitation.

Stakeholders do not make decisions about sites.

Stakeholders make decisions about projects.

Government agencies, investors, developers, engineers, utilities, development banks, and infrastructure operators evaluate opportunities in the context of projects that have objectives, risks, economics, timelines, and stakeholders.

As a result, the existing site-centric architecture no longer reflected how real-world decisions are made.

---

# Problem

The site-centric model creates several issues.

## 1. Mismatch with Industry Decision-Making

Infrastructure projects are evaluated as business and engineering initiatives.

A location is only one component of a project.

Decision makers ask:

* Should this project proceed?
* Is this project financeable?
* Is this project resilient?
* Is this project economically attractive?

They do not ask:

* Is this coordinate interesting?

---

## 2. Limited Representation of Risk

Risk assessments belong to projects.

Examples:

* Climate risk
* Engineering risk
* Regulatory risk
* Financing risk

These cannot be naturally represented as properties of a location.

---

## 3. Limited Support for Project Lifecycle Management

Ocean infrastructure projects evolve through multiple stages.

Examples:

```text
Idea
Screening
Pre-Feasibility
Feasibility
Financing
Engineering
Construction
Operation
```

A Site entity cannot represent this lifecycle.

---

## 4. Weak Alignment with Investor Workflows

Investors evaluate projects.

Banks evaluate projects.

Governments evaluate projects.

The platform must align with these workflows.

---

# Decision

OIIP adopts a Project-Centric Domain Model.

The primary domain entity becomes:

```text
OceanInfrastructureProject
```

All assessments, scores, reports, and recommendations belong to a project.

A geographic location remains important but becomes an attribute of a project rather than the central entity.

---

# New Conceptual Model

```text
OceanInfrastructureProject
│
├── Location
├── Resource Assessment
├── Climate Assessment
├── Infrastructure Assessment
├── Economic Assessment
├── Policy Assessment
├── Nexus Assessment
├── Bankability Assessment
│
└── Project Intelligence Score
```

---

# Project Lifecycle

Projects are represented as evolving entities.

Example:

```text
IDEA
    ↓
SCREENING
    ↓
PRE_FEASIBILITY
    ↓
FEASIBILITY
    ↓
PPP
    ↓
FINANCING
    ↓
ENGINEERING
    ↓
CONSTRUCTION
    ↓
OPERATION
```

The platform must support movement through these stages.

---

# Consequences

## Positive Consequences

### Better Stakeholder Alignment

The platform now reflects real-world infrastructure decision-making.

---

### Natural Risk Modeling

Project-level risk assessments become first-class concepts.

Examples:

* Climate resilience
* Economic viability
* Regulatory readiness
* Financing readiness

---

### Better Reporting

Reports become project-focused rather than location-focused.

Example:

```text
Project Intelligence Report
```

instead of:

```text
Site Analysis Report
```

---

### Support for Future Features

The project-centric model enables:

* PPP readiness assessment
* Investment screening
* Portfolio analysis
* Infrastructure planning
* Development bank workflows
* AI datacenter screening
* Desalination planning
* Blue economy analysis

---

## Negative Consequences

### Increased Complexity

Projects contain multiple assessments and lifecycle states.

The domain model becomes more sophisticated.

---

### Additional Data Requirements

Project evaluation requires more than oceanographic datasets.

Additional domains include:

* Economics
* Infrastructure
* Policy
* Finance
* Climate resilience

---

# Alternatives Considered

## Alternative 1: Continue Site-Centric Architecture

Rejected.

Reason:

Does not align with stakeholder decision-making.

---

## Alternative 2: Dual Site + Project Model

Rejected.

Reason:

Introduces ambiguity regarding the primary domain entity.

The platform requires a single clear aggregate root.

---

## Alternative 3: Project-Centric Architecture

Accepted.

Reason:

Provides the best alignment with industry workflows and long-term product vision.

---

# Future Implications

Future development should treat projects as the primary aggregate root.

All new functionality should answer the following question:

> Does this feature help stakeholders make better project decisions?

If the answer is no, the feature should be reconsidered.

---

# Guiding Principle

OIIP is not a geospatial platform that happens to contain infrastructure data.

OIIP is a Project Intelligence Platform that uses geospatial, climate, economic, and policy data to support infrastructure decisions.
