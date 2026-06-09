# API Architecture

## Ocean Infrastructure Intelligence Platform (OIIP)

---

# Purpose

This document defines the API architecture of the Ocean Infrastructure Intelligence Platform (OIIP).

The API provides programmatic access to project screening, assessment, scoring, and reporting capabilities.

The API is designed around infrastructure projects rather than datasets.

---

# API Philosophy

Traditional GIS APIs answer:

> What data exists at this location?

OIIP APIs answer:

> What infrastructure opportunity exists at this location?

The API is project-centric and decision-oriented.

---

# Architectural Style

The platform exposes a REST API.

Future versions may additionally provide:

* GraphQL
* gRPC
* Agent-to-Agent (A2A) interfaces
* MCP-compatible tools

REST remains the primary integration interface for OIIP v1.

---

# API Versioning

Versioning is URL-based.

Example:

```text
/api/v1
```

Future:

```text
/api/v2
```

---

# Core Workflow

```text
Coordinates
      ↓
Project Screening
      ↓
Assessments
      ↓
Project Intelligence Score
      ↓
Project Intelligence Report
```

---

# Primary Resources

## Screening

Represents a project screening request.

Endpoint:

```http
POST /api/v1/screening
```

Request:

```json
{
  "latitude": 13.10,
  "longitude": 100.92
}
```

Response:

```json
{
  "screening_id": "uuid",
  "status": "completed",
  "project_intelligence_score": 78
}
```

---

## Projects

Represents an evaluated infrastructure opportunity.

Endpoint:

```http
GET /api/v1/projects/{project_id}
```

Response:

```json
{
  "project_id": "uuid",
  "name": "Candidate OTEC Project",
  "status": "screened"
}
```

---

## Assessments

Represents analytical results.

Endpoint:

```http
GET /api/v1/projects/{project_id}/assessments
```

Returns:

* Resource Assessment
* Climate Assessment
* Economic Assessment
* Infrastructure Assessment
* PPP Assessment
* Nexus Assessment
* Bankability Assessment

---

## Reports

Represents generated project reports.

Endpoint:

```http
GET /api/v1/projects/{project_id}/report
```

Response:

```json
{
  "report_url": "...",
  "generated_at": "..."
}
```

---

# Assessment Model

All assessments follow a common structure.

```json
{
  "assessment_id": "uuid",
  "assessment_type": "resource",
  "score": 82,
  "created_at": "..."
}
```

---

# Scoring

OIIP produces multiple scores.

Examples:

* Resource Score
* Climate Score
* Infrastructure Score
* Economic Score
* PPP Score
* Nexus Score
* Bankability Score
* Project Intelligence Score

All scores use a normalized range:

```text
0 - 100
```

---

# Report Generation

Supported formats:

* JSON
* Markdown
* HTML
* PDF

Example:

```http
GET /api/v1/projects/{project_id}/report?format=pdf
```

---

# Future APIs

Future versions may include:

## Investor API

Provides investment-oriented screening.

Example:

```http
GET /api/v1/investor/opportunities
```

---

## Government API

Supports national planning workflows.

Example:

```http
GET /api/v1/government/projects
```

---

## AI Datacenter API

Supports AI infrastructure planning.

Example:

```http
POST /api/v1/ai-datacenter/screening
```

---

# Security

Authentication:

* API Keys
* OAuth2
* Service Accounts

Future:

* OIDC
* Enterprise SSO

---

# Guiding Principle

Every API endpoint must help answer one question:

> Should this infrastructure project move forward?
