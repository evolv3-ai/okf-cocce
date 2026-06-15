# OKF-COCCE

OKF-COCCE is the canonical public source for the **OKF-COCCE v0.1** combined specification.

**OKF** (Open Knowledge Format) is a portable knowledge-bundle format: Markdown files with YAML frontmatter, readable by people, parseable by agents, diffable in Git, and usable without a central registry.

**COCCE** is an operational layer on top of OKF. It gives agents a consistent model for acting safely in repositories and systems:

```text
category -> object -> capability -> connection -> event
```

Before acting, agents use COCCE to answer: what domain is this, what resource is touched, what action is allowed, what binding can perform it, and what evidence should be logged.

The canonical specification files live in [`spec/`](spec/index.md). This repository also contains examples, validation tooling, and an [`okf/`](okf/index.md) bundle that describes this repository using OKF-COCCE.

Validate the repository with:

```sh
python3 tools/validate-okf-cocce.py .
```

License: MIT.
