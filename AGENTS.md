# Agent entrypoint

This repository is the canonical source for the OKF-COCCE v0.1 specification.

Before making changes, agents MUST read, in order:

1. [README.md](README.md)
2. [spec/index.md](spec/index.md)
3. [okf/index.md](okf/index.md)
4. [okf/cocce.md](okf/cocce.md)

Agents MUST validate before finalizing changes:

```sh
python3 tools/validate-okf-cocce.py .
```

Agents MUST NOT invent new normative requirements without updating the relevant files in `spec/` and at least one example where applicable.

Agents MUST NOT store secret values in OKF-COCCE connection files. Connection documents MAY contain secret references, environment variable names, vault paths, or approval paths, but never tokens, passwords, private keys, or credential material.
