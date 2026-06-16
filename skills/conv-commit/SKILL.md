---
name: conv-commit
description: Use this skill when the user wants to generate a standard commit message following the Conventional Commits specification. Do not use this if the user requests a concise, detailed, or sarcastic commit.
---

Skill instructions for Codex to follow:

When generating a commit message, you must follow the Conventional Commits v1.0.0 specification precisely. Analyze the staged changes and produce a single commit message.

## Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types
The `<type>` must be one of the following:
- `feat`: A new feature for the user.
- `fix`: A bug fix for the user.
- `build`: Changes that affect the build system or external dependencies.
- `chore`: Updating grunt tasks etc; no production code change.
- `ci`: Changes to CI configuration files and scripts.
- `docs`: Documentation only changes.
- `style`: Changes that do not affect the meaning of the code.
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `perf`: A code change that improves performance.
- `test`: Adding missing tests or correcting existing tests.
- `revert`: Reverts a previous commit.

## Rules
1. **Scope**: Optional. A noun describing a section of the codebase surrounded by parentheses (e.g., `feat(parser): ...`).
2. **Description**: A short summary of the code changes. Use the imperative, present tense: "change" not "changed". Do not capitalize the first letter and do not place a period at the end.
3. **Body**: Optional. Provide additional contextual information about the code changes. Must be separated from the description by a single blank line.
4. **Footer**: Optional. Separated from the body by a blank line. Used for referencing issues or noting breaking changes.
5. **Breaking Changes**: Must be indicated by an exclamation mark `!` before the colon, or a footer beginning with `BREAKING CHANGE: `.

## Output
Produce ONLY the raw commit message text. Do not wrap the output in markdown code blocks and do not add any conversational text.