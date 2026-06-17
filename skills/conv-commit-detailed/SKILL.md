---
name: conv-commit-detailed
description: Use this skill ONLY when the user explicitly requests a detailed, thorough, or comprehensive conventional commit with a body and context. Do not use this for standard, concise, or sarcastic commits.
---

Skill instructions for the agent to follow:

When generating a commit message, you must follow the Conventional Commits v1.0.0 specification and strictly enforce a highly detailed output. Analyze the staged changes deeply to provide extensive context, reasoning, and implications.

## Message Format

```
<type>[optional scope]: <description>

<body>

[optional footer(s)]
```

## Types
The `<type>` must be one of the following: `feat`, `fix`, `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`, `revert`.

## Rules
1. **Scope**: Always include a precise scope if applicable.
2. **Description**: A short summary of the code changes. Use the imperative, present tense.
3. **Body (MANDATORY)**: You MUST include a detailed body separated from the description by a single blank line. Your body must comprehensively address:
   - **Context**: What was the previous behavior or the motivation for the change?
   - **Implementation**: How does this commit solve the problem or implement the feature?
   - **Impact/Side-effects**: Are there any performance, security, or architectural considerations?
4. **Footer**: Include a footer separated from the body by a blank line if there are related issue numbers or breaking changes.
5. **Breaking Changes**: Must be explained thoroughly using a `BREAKING CHANGE: ` footer with an extensive description and migration path.

## Output
Produce ONLY the raw, detailed commit message text. Do not wrap the output in markdown code blocks and do not add any conversational text.