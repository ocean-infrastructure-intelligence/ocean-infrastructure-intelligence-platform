# Entity Relationship Diagram (ERD)

## Purpose

This document defines the logical data model for the Ocean Infrastructure Intelligence Platform (OIIP).

The model is designed to support:

* Oceanographic data storage
* OTEC analysis
* Infrastructure intelligence
* Environmental risk assessment
* Economic modeling
* AI Datacenter Suitability Index (ADCSI)
* Geospatial analytics

The platform uses PostgreSQL with PostGIS as the primary operational database.

---

# Design Principles

The data model follows several principles:

* Spatial-first architecture
* Domain separation
* Time-series support
* Extensibility
* Reproducibility
* Source traceability

---

# High-Level Entity Model

```text
SITE
 │
 ├── OCEAN_PROFILE
 │
 ├── OCEAN_SURFACE
 │
 ├── OTEC_POTENTIAL
 │
 ├── SITE_INFRASTRUCTURE
 │
 ├── SITE_RISK
 │
 ├── SITE_ECONOMICS
 │
 ├── DATACENTER_SUITABILITY
 │
 └── SITE_SCORE
```

The Site entity is the central object of the platform.

---

# Core Entity: Site

Represents a candidate location for ocean infrastructure development.

## site

```text
site
├── id
├── name
├── latitude
├── longitude
├── geom
├── country_code
├── region
├── created_at
└── updated_at
```

Primary Key:

```text
id
```

Geometry:

```text
POINT (EPSG:4326)
```

Relationships:

```text
site
 ├── 1:N ocean_profile
 ├── 1:N ocean_surface
 ├── 1:1 otec_potential
 ├── 1:1 site_infrastructure
 ├── 1:1 site_risk
 ├── 1:1 site_economics
 ├── 1:1 datacenter_suitability
 └── 1:1 site_score
```

---

# Oceanography Domain

## ocean_profile

Stores vertical water column measurements.

```text
ocean_profile
├── id
├── site_id
├── observation_time
├── depth_m
├── temperature_c
├── salinity_psu
├── density_kgm3
└── source_id
```

Relationship:

```text
site 1:N ocean_profile
```

Example:

```text
Depth      Temperature
0 m        29.4 °C
100 m      24.6 °C
500 m      11.3 °C
1000 m      5.8 °C
```

---

## ocean_surface

Stores surface conditions.

```text
ocean_surface
├── id
├── site_id
├── observation_time
├── sst_c
├── wave_height_m
├── current_speed_ms
├── current_direction_deg
└── source_id
```

Relationship:

```text
site 1:N ocean_surface
```

---

## bathymetry_point

Stores bathymetric observations.

```text
bathymetry_point
├── id
├── geom
├── depth_m
├── source_id
└── observation_time
```

Geometry:

```text
POINT
```

Spatial Index:

```text
GIST
```

---

# Energy Domain

## otec_potential

Stores calculated OTEC metrics.

```text
otec_potential
├── site_id
├── surface_temp_c
├── deep_temp_c
├── delta_t
├── theoretical_power_mw
├── net_power_mw
├── efficiency
├── calculation_version
└── calculated_at
```

Relationship:

```text
site 1:1 otec_potential
```

Purpose:

Evaluate thermal energy potential.

---

# Infrastructure Domain

## power_grid_asset

Represents electrical infrastructure.

```text
power_grid_asset
├── id
├── name
├── asset_type
├── voltage_kv
├── geom
└── source_id
```

Geometry:

```text
POINT
```

---

## submarine_cable

Represents submarine communication cables.

```text
submarine_cable
├── id
├── name
├── owner
├── capacity_tbps
├── geom
└── source_id
```

Geometry:

```text
LINESTRING
```

---

## cable_landing_station

Represents cable landing stations.

```text
cable_landing_station
├── id
├── name
├── country
├── geom
└── source_id
```

Geometry:

```text
POINT
```

---

## port

Represents maritime ports.

```text
port
├── id
├── name
├── port_type
├── geom
└── source_id
```

Geometry:

```text
POINT
```

---

## site_infrastructure

Aggregated infrastructure metrics.

```text
site_infrastructure
├── site_id
├── nearest_port_km
├── nearest_grid_km
├── nearest_cable_km
├── nearest_landing_station_km
├── logistics_score
└── infrastructure_score
```

Relationship:

```text
site 1:1 site_infrastructure
```

---

# Risk Domain

## cyclone_event

Historical cyclone tracks.

```text
cyclone_event
├── id
├── event_name
├── category
├── event_time
├── geom
└── source_id
```

Geometry:

```text
LINESTRING
```

---

## site_risk

Aggregated site risks.

```text
site_risk
├── site_id
├── cyclone_score
├── tsunami_score
├── seismic_score
├── wave_score
└── overall_risk_score
```

Relationship:

```text
site 1:1 site_risk
```

---

# Economics Domain

## site_economics

Stores economic indicators.

```text
site_economics
├── site_id
├── capex_usd
├── opex_usd
├── npv_usd
├── irr
├── lcoe
├── scenario_name
└── calculated_at
```

Relationship:

```text
site 1:1 site_economics
```

---

# AI Infrastructure Domain

## datacenter_suitability

Stores AI datacenter metrics.

```text
datacenter_suitability
├── site_id
├── cooling_score
├── cable_score
├── grid_score
├── logistics_score
├── security_score
├── sustainability_score
└── adcsi
```

Relationship:

```text
site 1:1 datacenter_suitability
```

---

# Ranking Domain

## site_score

Final ranking table.

```text
site_score
├── site_id
├── otec_score
├── infrastructure_score
├── risk_score
├── economic_score
├── adcsi_score
├── total_score
├── ranking
└── calculated_at
```

Relationship:

```text
site 1:1 site_score
```

---

# Data Lineage

Every dataset should be traceable to its source.

## data_source

```text
data_source
├── id
├── provider_name
├── dataset_name
├── version
├── source_url
├── license
├── acquired_at
└── metadata
```

Examples:

* Copernicus Marine
* NOAA
* GEBCO
* OpenStreetMap
* IBTrACS

All analytical entities should reference a source whenever practical.

---

# Metadata and Auditing

All major entities should support:

```text
created_at
updated_at
created_by
updated_by
```

This improves reproducibility and governance.

---

# Spatial Indexing Strategy

The following entities require GIST indexes:

```text
site
bathymetry_point
power_grid_asset
submarine_cable
cable_landing_station
port
cyclone_event
```

Benefits:

* Fast nearest-neighbor search
* Distance calculations
* Spatial joins
* Overlay analysis

---

# Future Extensions

The data model is designed to support future domains.

Potential additions:

```text
offshore_wind
wave_energy
hydrogen_production
ocean_carbon_capture
floating_datacenters
marine_robotics
digital_ocean_twin
```

Future entities should follow the same principles:

* Spatial-first
* Source traceable
* Reproducible
* Extensible

---

# Related Documents

For system architecture:

```text
docs/architecture/system-overview.md
```

For API specifications:

```text
docs/architecture/api.md
```

For deployment architecture:

```text
docs/architecture/deployment.md
```

For event processing:

```text
docs/architecture/event-model.md
```
