# COCCE v0.1

COCCE is the OKF-compatible operational layer for agents and automation.

```text
category -> object -> capability -> connection -> event
```

COCCE uses OKF documents and frontmatter. It does not grant permission by itself. Runtime authorization still belongs to tools, hosts, policy engines, approval systems, and users.

## Category

A `Category` is the domain or control-plane namespace for work. Examples: `repo`, `ci`, `infra`, `mcp`, `security`, `knowledge`.

Category identifiers SHOULD be stable lower snake case.

## Object

An `ObjectType` defines a class of thing, such as `repo_repository`, `repo_pull_request`, or `infra_deployment`. An `Object` describes a specific instance.

Object type identifiers SHOULD follow:

```text
<category>_<object>
```

## Capability

A `Capability` is an action that can be performed against an object type or object.

Capability identifiers SHOULD follow:

```text
<category>_<object>_<action>
```

A capability describes a possible action. It MUST NOT be treated as proof that an agent is authorized.

## Connection

A `Connection` is a bounded way to use an integration, tool, runtime, service account, MCP server, local shell, or human approval path.

Connection documents MUST NOT contain secret values. They MAY contain secret references such as vault paths, environment variable names, key IDs, or approval procedures.

## Event

An `Event` records an attempted, denied, completed, or observed action. Events SHOULD be append-only and SHOULD link to relevant categories, objects, capabilities, connections, policies, logs, or pull requests.

## Required COCCE concept types

COCCE-compatible bundles SHOULD use these OKF `type` values when applicable:

- `Category`
- `ObjectType`
- `Object`
- `Capability`
- `Integration`
- `Connection`
- `Event`
- `Policy`
- `Playbook`
- `Reference`

## Pre-action checklist

Before acting, agents SHOULD answer:

1. What category/domain is this task in?
2. What object/resource is being touched?
3. What capability/action is allowed or requested?
4. What connection/tool/binding/approval path can perform it?
5. What event/evidence should be logged?

## Discovery

Agents SHOULD read repository entrypoints first, then the OKF bundle index, local COCCE profile, category index, object index, capability index, connection index, policy index, and relevant playbooks.
