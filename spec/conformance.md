# Conformance

## Required

An OKF-COCCE v0.1 repository MUST:

- Include `README.md`, `LICENSE`, `AGENTS.md`, and `spec/index.md`.
- Define OKF as the base format and COCCE as a layer on top of OKF.
- Keep concept documents as Markdown with YAML frontmatter.
- Include a non-empty `type` field in every concept document.
- Never store secret values in connection documents.

A COCCE-aware agent MUST:

- Parse frontmatter for concepts it uses.
- Tolerate unknown fields and unknown type values.
- Treat capabilities as descriptions, not authorization grants.
- Check connection and policy context before mutating external systems.

## Recommended

Repositories SHOULD:

- Store the primary OKF bundle in `okf/`.
- Include `okf/index.md`, `okf/log.md`, and `okf/cocce.md`.
- Use directories for categories, objects, capabilities, integrations, connections, events, policies, playbooks, and references.
- Provide examples and validation tooling.
- Log material agent or automation activity as events.

## Optional

Repositories MAY:

- Use additional COCCE-compatible concept types.
- Generate indexes from concepts.
- Mirror external references under `okf/references/`.
- Use stricter local validation than the base OKF conformance model.
