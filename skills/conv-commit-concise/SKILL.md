---
name: conv-commit-concise
description: Use this skill ONLY when the user explicitly requests a brief, single-line, or concise conventional commit. Do not use this for standard, detailed, or sarcastic commits.
---

Skill instructions for Codex to follow:

When generating a commit message, you must follow the Conventional Commits v1.0.0 specification but keep the output as brief and concise as possible. Analyze the staged changes and produce a single-line commit message.

## Message Format

```
<type>[optional scope]: <description>
```

*(Note: Do not include a body or footer unless there is a BREAKING CHANGE that strictly requires explanation).*

## Types
The `<type>` must be one of the following: `feat`, `fix`, `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`, `revert`.

## Rules
1. **Scope**: Keep it brief (e.g., `feat(api): ...`). Omit the scope if the change is broad.
2. **Description**: A short summary of the code changes. Use the imperative, present tense. Do not capitalize the first letter and do not place a period at the end. Keep the entire line strictly under 50 characters.
3. **Body and Footer**: OMIT the body and footer entirely. The only exception is a breaking change.
4. **Breaking Changes**: Strongly prefer using the `!` notation (e.g., `feat(auth)!: remove old login`) to indicate breaking changes on the first line.

## Output
Produce ONLY the raw single-line commit message text. Do not wrap the output in markdown code blocks and do not add any conversational text.