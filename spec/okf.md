# Open Knowledge Format (OKF) v0.1

OKF is the base standard for OKF-COCCE.

A knowledge bundle is a directory tree of UTF-8 Markdown files. Concept documents contain YAML frontmatter followed by Markdown body content. OKF is human-readable, agent-parseable, Git-diffable, portable, and usable without a central registry.

## Goals

OKF exists to let people and agents author, exchange, and consume contextual knowledge around data, systems, processes, and software. It standardizes only enough structure for interoperability.

OKF does not replace OpenAPI, JSON Schema, Protobuf, Avro, Terraform, Kubernetes manifests, or other domain schemas. OKF MAY reference those formats.

## Bundle structure

```text
bundle/
  index.md
  log.md
  concepts.md
  group/
    index.md
    concept.md
```

A bundle MAY be a Git repository, archive, or subdirectory in a larger repository.

## Reserved files

- `index.md` lists nearby content for progressive disclosure.
- `log.md` records update history.

Other Markdown files are concept documents.

## Concept documents

Every non-reserved concept document MUST begin with YAML frontmatter delimited by `---` and MUST include a non-empty `type` field.

```yaml
---
type: Reference
title: Example concept
description: A one-line summary.
resource: urn:example:concept
tags: [example]
timestamp: 2026-06-15T00:00:00Z
---
```

Recommended fields are `title`, `description`, `resource`, `tags`, and `timestamp`. Producers MAY add fields. Consumers MUST tolerate unknown fields and unknown `type` values.

## Body

The body is Markdown. Producers SHOULD prefer headings, lists, tables, and fenced code blocks because structure helps both humans and agents.

Conventional headings include `Schema`, `Examples`, and `Citations`.

## Links

Concepts MAY link to other concepts with normal Markdown links. Bundle-relative links beginning with `/` are RECOMMENDED. Relative links are allowed. Link text and surrounding prose define relationship meaning.

OKF consumers SHOULD tolerate broken links. The OKF-COCCE repository validator is stricter for this repository and checks internal links before publication.

## Indexes and logs

`index.md` files SHOULD enumerate local contents. `log.md` files SHOULD use newest-first ISO date headings (`YYYY-MM-DD`).

## OKF conformance

A bundle conforms to OKF v0.1 when every concept document has parseable YAML frontmatter with a non-empty `type` field and reserved files follow their intended structure when present.
