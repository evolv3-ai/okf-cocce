# Versioning

The canonical version of this specification is `v0.1`.

OKF-COCCE versions use `major.minor` identifiers.

- A minor version introduces backward-compatible additions, clarifications, examples, optional fields, or recommended conventions.
- A major version may introduce breaking changes to required fields, reserved filenames, core concepts, or conformance rules.

Bundles MAY declare their target version with frontmatter such as:

```yaml
okf_cocce_version: "0.1"
```

Consumers that do not understand a declared version SHOULD attempt best-effort reading and report unsupported features instead of failing closed unless safety policy requires otherwise.
