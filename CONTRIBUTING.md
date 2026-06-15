# Contributing

Changes to OKF-COCCE MUST preserve OKF as the base standard and COCCE as an operational layer on top of OKF.

## Requirements

- Update `spec/` for normative changes.
- Update examples when behavior changes.
- Do not store secrets in repository files or OKF-COCCE connection documents.
- Run validation before opening a pull request:

```sh
python3 tools/validate-okf-cocce.py .
```
