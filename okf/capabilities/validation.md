---
type: Capability
id: repo_validation_run
title: Run repository validation
description: Validate required files, OKF frontmatter, links, COCCE fields, and connection secret hygiene.
category: specification
object: validation
object_type: validation_tool
action: run
capability: repo_validation_run
access: execute
mutates_state: false
allowed_connections: [local-shell]
required_events: [validation_event]
tags: [cocce, capability]
---

Run `python3 tools/validate-okf-cocce.py .` before finalizing changes.
