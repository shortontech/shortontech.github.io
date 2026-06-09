# Using Agentic Tooling to Build Application-Specific AppSec Controls

## Abstract

General-purpose application security tools are constrained by the assumptions they can safely make across many codebases. They can detect known vulnerability patterns, suspicious API usage, dependency exposure, and common misconfigurations. The local rules that make a particular application safe require a different kind of context. The tool needs to know which resources must be tenant-bound, which serializers are allowed to expose sensitive fields, which state transitions require audit records, which partner webhooks must verify signatures before parsing, and which dependency findings matter because the vulnerable path is actually reachable.

Many of the most important application security failures involve application-specific invariants alongside universal vulnerability classes. These invariants often exist informally in code review memory, engineering convention, wiki pages, framework helpers, and senior developer judgment. They are too local for generic scanners to enforce by default, and historically they have been too expensive to encode as custom tooling for every application.

Agentic tooling changes that cost model. A senior application security engineer, working with an AI-assisted development harness, can now inspect a codebase, identify repeated security-relevant patterns, propose local invariants, generate enforcement tools, create fixtures, test against known-good and known-bad paths, and integrate the resulting checks into CI or review workflows in days.

This paper argues that application-specific AppSec controls belong between generic scanners and human review. In this model, the agent helps build enforcement artifacts while the security decision remains with the human reviewer. The output is a repository-owned static check, code generation rule, test harness, CI gate, review bot, or analyzer plugin that encodes a narrow invariant and produces reviewable evidence when the invariant is violated. The purpose is to convert repeated AppSec judgment into readable, repeatable, reliable controls while preserving human responsibility for the judgment itself.

## 1. Introduction

Most AppSec programs use broad tools against failures that are specific to one system.

The usual tools are designed for broad portability, while the application’s most important security rules are often specific to its ownership model, data model, workflow, and history.

A scanner can know that raw SQL concatenation is dangerous, that a dependency has a published CVE, that a cookie should be `HttpOnly`, that secrets should stay out of source control, or that a route lacks an obvious authorization decorator. These checks are useful at the level of portable security knowledge.

Real AppSec work often depends on application-specific context beneath those portable checks.

An invoice should be loaded through an organization-scoped lookup. A customer-support export should omit internal notes unless the requester has a specific role. A webhook handler should verify the signature before parsing the body. A state transition from `draft` to `approved` should require a reviewer distinct from the author. A dependency finding should block release when the vulnerable symbol is reachable under the application’s runtime conditions.

These application-specific rules form the security contract of the system.

The difficulty is that this contract is usually implicit. It lives in how experienced engineers review code, how framework helpers are expected to be used, how services are organized, and how incidents have shaped local practice. When the contract is violated, the result may look like IDOR, mass assignment, sensitive data exposure, authorization bypass, audit failure, dependency exposure, or business logic abuse. The root failure is often more precise. The implementation stopped obeying a local invariant that the rest of the application quietly depends on.

General-purpose scanners are poorly positioned to enforce these invariants because they lack permission to assume them. This application may require all invoice reads to pass through `Invoice.for_actor(actor)`. `AccountPublicSerializer` may be safe while `AccountSerializer` is internal-only. `verify_partner_signature()` may need to dominate parsing for a particular webhook family. The repository has to make those expectations visible before tooling can enforce them.

Historically, custom enforcement of these rules was expensive. A team might write a few Semgrep rules, some CodeQL queries, or a custom script for the most painful recurring issue, but deep application-specific enforcement required expertise, program analysis skill, fixture design, and maintenance time. Most organizations could not justify building bespoke AppSec tooling for every local invariant.

AI-assisted engineering changes the economics by making it practical to use agents as tooling accelerators. A prompt asking an LLM to “review the application” produces an answer that is difficult to audit and easy to lose. Agentic tooling aimed at local enforcement artifacts produces something the repository can keep, test, and improve.

The agent helps read the codebase, compare sibling paths, identify repeated patterns, draft the invariant, generate the checker, produce tests, run the tool, explain false positives, and iterate. The human AppSec engineer remains responsible for judgment. The repository gets a control it can run again.

The agent session should leave versioned repository tooling behind.
