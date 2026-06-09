# Use Cases

## Purpose

This document defines the primary business use cases supported by OIIP.

---

# UC-001 Coordinate Screening

## Actor

Developer

## Goal

Determine whether a location is suitable for an ocean infrastructure project.

## Workflow

```text
Coordinates
      ↓
Screening Request
      ↓
Assessments
      ↓
Project Intelligence Score
      ↓
Report
```

## Result

Project Screening Report

---

# UC-002 Project Comparison

## Actor

Developer

## Goal

Compare multiple candidate locations.

## Workflow

```text
Project A
Project B
Project C
      ↓
Ranking
      ↓
Comparison Report
```

## Result

Ranked opportunity list.

---

# UC-003 Government Planning

## Actor

Government Agency

## Goal

Identify infrastructure opportunities at national scale.

## Workflow

```text
Country
      ↓
Regional Analysis
      ↓
Project Portfolio
```

## Result

National Opportunity Map.

---

# UC-004 Investment Screening

## Actor

Investor

## Goal

Prioritize projects for due diligence.

## Workflow

```text
Projects
      ↓
Investment Scoring
      ↓
Shortlist
```

## Result

Investment Pipeline.

---

# UC-005 AI Datacenter Screening

## Actor

Datacenter Operator

## Goal

Identify locations suitable for AI infrastructure.

## Workflow

```text
Coordinates
      ↓
Cooling Assessment
      ↓
Connectivity Assessment
      ↓
Energy Assessment
      ↓
Suitability Score
```

## Result

AI Datacenter Opportunity Report.

---

# UC-006 OTEC Development Pipeline

## Actor

Developer

## Goal

Manage project progression through lifecycle stages.

## Workflow

```text
Project
      ↓
Assessments
      ↓
Stage Advancement
```

## Result

Project Development Dashboard.

---

# UC-007 Climate Resilience Screening

## Actor

Engineer

## Goal

Evaluate survivability of ocean infrastructure.

## Workflow

```text
Location
      ↓
Hazard Assessment
      ↓
Resilience Score
```

## Result

Climate Risk Report.

---

# MVP Scope

OIIP v1 implements only:

```text
UC-001 Coordinate Screening
```

Everything else builds on top of this capability.

---

# Guiding Principle

Every feature must support at least one clearly defined stakeholder use case.
