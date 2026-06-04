# Security Policy

## Supported Versions

The Ocean Infrastructure Intelligence Platform (OIIP) is currently under active development.

Security updates are provided for the latest development branch and official releases.

| Version        | Supported |
| -------------- | --------- |
| main           | Yes       |
| Latest Release | Yes       |
| Older Releases | No        |

---

# Reporting a Vulnerability

We take security issues seriously and appreciate responsible disclosure.

If you discover a security vulnerability, please do not open a public GitHub issue.

Instead, contact the project maintainers privately.

When reporting a vulnerability, please include:

* Description of the issue
* Steps to reproduce
* Potential impact
* Affected components
* Suggested remediation (if available)

We will acknowledge receipt of the report as soon as possible and investigate the issue.

---

# Responsible Disclosure

We ask security researchers to:

* Give maintainers reasonable time to investigate and fix issues
* Avoid public disclosure before remediation
* Avoid accessing data beyond what is necessary to demonstrate the issue
* Avoid actions that could disrupt services or infrastructure

We value responsible security research and will work collaboratively to address legitimate concerns.

---

# Security Scope

The project includes multiple layers that may have different security considerations:

* Web APIs
* Geospatial services
* Background processing pipelines
* External data providers
* Database infrastructure
* AI agents and automation systems
* Containerized deployments

Security reviews should consider all relevant layers.

---

# Sensitive Information

The following information must never be committed to the repository:

* API keys
* Access tokens
* Passwords
* Database credentials
* Private certificates
* Cloud credentials
* SSH private keys
* Production secrets

Examples:

```text
.env
.env.production
secrets.yaml
credentials.json
private.key
```

Use environment variables or dedicated secret management systems instead.

---

# Dependency Security

Contributors should:

* Keep dependencies up to date
* Review security advisories
* Avoid unnecessary dependencies
* Remove unused packages

The project may use:

* Dependabot
* GitHub Security Advisories
* CodeQL
* Automated dependency scanning

to identify potential vulnerabilities.

---

# Data Security

OIIP integrates data from multiple external providers.

Examples include:

* Copernicus Marine Service
* NOAA
* GEBCO
* OpenStreetMap
* AIS providers
* Infrastructure datasets

Contributors must:

* Respect provider terms of use
* Preserve attribution requirements
* Avoid unauthorized redistribution of restricted datasets
* Protect any non-public credentials used to access data services

---

# Infrastructure Security

Recommended production practices include:

* HTTPS everywhere
* Principle of least privilege
* Role-based access control
* Network segmentation
* Secret management
* Regular backups
* Security monitoring
* Vulnerability scanning

---

# Database Security

Recommended practices for PostgreSQL and PostGIS:

* Disable default credentials
* Restrict administrative access
* Use encrypted connections
* Regularly update database software
* Limit database exposure to public networks

Production databases should never be directly exposed to the public internet.

---

# Container Security

When using Docker:

* Use minimal base images
* Keep images updated
* Run containers as non-root users
* Scan images for vulnerabilities
* Avoid embedding secrets in images

---

# API Security

API implementations should:

* Validate all inputs
* Apply authentication where required
* Implement rate limiting
* Log security-relevant events
* Protect against common web vulnerabilities

Examples include:

* Injection attacks
* Broken access control
* Server-side request forgery (SSRF)
* Cross-site scripting (XSS)
* Cross-site request forgery (CSRF)

---

# AI and Automation Security

OIIP may include AI agents and automated workflows.

Contributors should consider:

* Prompt injection risks
* Data leakage risks
* Unauthorized tool access
* Credential exposure
* Agent privilege escalation

AI agents should operate under the principle of least privilege.

---

# Geographic and Infrastructure Data

Some datasets may describe critical infrastructure.

Examples include:

* Power systems
* Telecommunications infrastructure
* Submarine cable networks
* Port facilities

Contributors should ensure that published information complies with applicable laws, regulations, licenses, and source restrictions.

---

# Security Updates

Security-related fixes may be prioritized over feature development.

Where appropriate, maintainers may:

* Issue security advisories
* Publish remediation guidance
* Release emergency patches

---

# Acknowledgements

We appreciate responsible disclosure and contributions from the security community.

Security is a shared responsibility, and we thank everyone who helps improve the safety, reliability, and resilience of the Ocean Infrastructure Intelligence Platform.

---

# Contact

For security-related concerns, please contact the project maintainers through private channels rather than public issue trackers.
