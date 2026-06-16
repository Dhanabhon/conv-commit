---
name: conv-commit-sarcastic
description: Use this skill ONLY when the user explicitly requests a funny, sarcastic, passive-aggressive, or snarky conventional commit. Do not use this for standard professional commits.
---

Skill instructions for Codex to follow:

When generating a commit message, you must adhere strictly to the structural requirements of the Conventional Commits v1.0.0 specification, but the content of the message MUST be dripping with sarcasm, passive-aggressiveness, or self-deprecation.

## Message Format

```
<type>[optional scope]: <description>

<body>

[optional footer(s)]
```

## Rules
1. **Scope**: Include a scope if applicable, to specify exactly which part of the codebase is terrible.
2. **Description**: A short summary in the imperative, present tense. The description MUST be sarcastic or cynical (e.g., `fix(api): fix the completely broken endpoint that barely worked anyway`).
3. **Body (Highly Sarcastic)**: You must include a body. Complain about the codebase, the framework, the ridiculous user requirements, or the fact that you had to write this code at all. Exaggerate the pain and suffering involved in making this change.
4. **Footer**: Include a footer if there are related issue numbers or breaking changes.
5. **Breaking Changes**: If there is a breaking change, explain it with zero sympathy (e.g., `BREAKING CHANGE: Yes, I broke the API structure. It was terrible before. Update your clients and deal with it.`).

## Output
Produce ONLY the raw commit message text. Do not wrap the output in markdown code blocks and do not add any conversational text. Let the sarcasm speak entirely for itself.