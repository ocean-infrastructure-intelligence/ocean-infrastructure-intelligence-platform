# Project Intelligence Model

## Ocean Infrastructure Intelligence Platform (OIIP)

---

# Purpose

This document defines the core analytical model of OIIP.

The objective of OIIP is not to collect datasets and not to display maps.

The objective of OIIP is to support infrastructure investment and development decisions.

OIIP evaluates potential ocean infrastructure projects and converts multidisciplinary data into actionable intelligence.

---

# Core Question

Every analysis performed by OIIP must contribute to answering a single question:

> Should this infrastructure project move forward?

---

# Conceptual Model

The platform is built around a single aggregate root:

```text
OceanInfrastructureProject
```

All datasets, assessments, reports, and scores exist to evaluate a project.

---

# Project Intelligence Workflow

```text
Coordinates
      ↓
Project Creation
      ↓
Resource Assessment
      ↓
Climate Assessment
      ↓
Economic Assessment
      ↓
Infrastructure Assessment
      ↓
Policy Assessment
      ↓
Nexus Assessment
      ↓
Bankability Assessment
      ↓
Project Intelligence Score
      ↓
Project Intelligence Report
```

---

# OceanInfrastructureProject

Represents a candidate or active infrastructure project.

A project may represent:

* OTEC Facility
* SWAC System
* Desalination Facility
* Offshore Energy Hub
* AI Datacenter
* Blue Economy Infrastructure
* Hybrid Multi-Use Development

---

# Project Structure

```text
OceanInfrastructureProject
│
├── Project Metadata
│
├── Location
│
├── Resource Assessment
│
├── Climate Assessment
│
├── Economic Assessment
│
├── Infrastructure Assessment
│
├── Policy Assessment
│
├── Nexus Assessment
│
├── Bankability Assessment
│
├── Project Intelligence Score
│
└── Reports
```

---

# Assessment Domains

## Resource Assessment

Purpose:

Determine whether the ocean resource is sufficient.

Questions:

* Is thermal energy available?
* Is deep water accessible?
* Is OTEC technically feasible?

Inputs:

* SST
* Deep Water Temperature
* Thermal Gradient
* Bathymetry
* Distance to Deep Water

Output:

```text
Resource Score
0 - 100
```

---

## Climate Assessment

Purpose:

Evaluate survivability and environmental risk.

Questions:

* Can the infrastructure survive extreme weather?
* What hazards must be considered?

Inputs:

* Cyclones
* Waves
* Currents
* Seismic Activity
* Tsunami Risk

Output:

```text
Climate Score
0 - 100
```

---

## Economic Assessment

Purpose:

Evaluate economic viability.

Questions:

* Can the project compete economically?
* Does it reduce energy costs?

Inputs:

* Diesel Prices
* Electricity Prices
* Demand
* Fuel Imports
* GDP Indicators

Output:

```text
Economic Score
0 - 100
```

---

## Infrastructure Assessment

Purpose:

Evaluate deployment readiness.

Questions:

* Can the project be built?
* Can it connect to infrastructure?

Inputs:

* Ports
* Grid
* Airports
* Shipyards
* Submarine Cables

Output:

```text
Infrastructure Score
0 - 100
```

---

## Policy Assessment

Purpose:

Evaluate regulatory readiness.

Questions:

* Can the project be permitted?
* Is government support available?

Inputs:

* Energy Policy
* Ocean Policy
* Incentives
* PPP Frameworks

Output:

```text
Policy Score
0 - 100
```

---

## Nexus Assessment

Purpose:

Evaluate co-benefits.

Questions:

* Can the project create additional value?

Inputs:

* Desalination Potential
* Aquaculture Potential
* Hydrogen Potential
* Cooling Potential

Output:

```text
Nexus Score
0 - 100
```

---

## Bankability Assessment

Purpose:

Evaluate financing readiness.

Questions:

* Can the project attract investment?

Inputs:

* Country Risk
* Market Conditions
* Policy Stability
* Project Maturity

Output:

```text
Bankability Score
0 - 100
```

---

# Project Intelligence Score

The Project Intelligence Score is the primary output of OIIP.

Purpose:

Provide a normalized indicator of project attractiveness and readiness.

Range:

```text
0 - 100
```

Interpretation:

| Score  | Meaning                |
| ------ | ---------------------- |
| 0-20   | Not Recommended        |
| 21-40  | High Risk              |
| 41-60  | Requires Further Study |
| 61-80  | Promising              |
| 81-100 | Strong Candidate       |

---

# Scoring Composition

Current target weighting:

```text
25% Resource
20% Climate
20% Economic
15% Infrastructure
10% Policy
 5% Nexus
 5% Bankability
```

Formula:

```text
Project Intelligence Score
=
(Resource × 0.25)
+
(Climate × 0.20)
+
(Economic × 0.20)
+
(Infrastructure × 0.15)
+
(Policy × 0.10)
+
(Nexus × 0.05)
+
(Bankability × 0.05)
```

---

# MVP Scope

Version 1 implements only three domains:

```text
Resource Assessment
Climate Assessment
Economic Assessment
```

The first release answers:

> If I build an OTEC project at these coordinates, is this a reasonable idea?

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

# Future Evolution

Future releases may introduce:

* Infrastructure Intelligence
* Policy Intelligence
* Bankability Intelligence
* PPP Intelligence
* Portfolio Intelligence
* National Planning Intelligence
* AI Datacenter Intelligence
* Digital Twin Intelligence

without changing the core project model.

---

# Guiding Principle

OIIP is not a mapping platform.

OIIP is not a dataset catalog.

OIIP is a Project Intelligence Platform that transforms ocean, climate, economic, infrastructure, and policy data into decisions.
