# OKF-COCCE v0.1 Specification

This directory is the canonical source for OKF-COCCE v0.1.

OKF-COCCE combines:

- [OKF](okf.md), the base knowledge-bundle format.
- [COCCE](cocce.md), the operational model layered on top of OKF.
- [Conformance](conformance.md), required, recommended, and optional behavior.
- [Versioning](versioning.md), compatibility and release rules.

## Status

Version: `v0.1`

License: MIT

## Core rule

COCCE is not a replacement for OKF. Every COCCE concept is an OKF concept. OKF defines the portable document format; COCCE defines a conventional vocabulary that agents can use to plan, authorize, execute, and log work.

## Agent pre-action questions

Before acting, an agent SHOULD answer:

1. What category/domain is this task in?
2. What object/resource is being touched?
3. What capability/action is allowed or requested?
4. What connection/tool/binding/approval path can perform it?
5. What event/evidence should be logged?
