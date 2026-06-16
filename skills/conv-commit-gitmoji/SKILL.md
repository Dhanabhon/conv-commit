---
name: conv-commit-gitmoji
description: Use this skill ONLY when the user explicitly requests a conventional commit formatted with Gitmoji (emoji prefixes). Do not use this for standard commits.
---

Skill instructions for Codex to follow:

When generating a commit message, you must follow the Conventional Commits v1.0.0 specification while strictly enforcing the inclusion of the appropriate Gitmoji at the very beginning of the commit message. Analyze the staged changes and produce a single commit message.

## Message Format

```
<gitmoji> <type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types and Corresponding Gitmojis
The `<type>` must be one of the standard Conventional Commits types, and it MUST be prefixed with the exact matching unicode Gitmoji:
- `✨ feat`: A new feature.
- `🐛 fix`: A bug fix.
- `📦 build`: Build system or dependency updates.
- `🧹 chore`: Minor tasks, maintenance, or tooling.
- `👷 ci`: CI configuration changes.
- `📝 docs`: Documentation updates.
- `💄 style`: Formatting, UI, or whitespace changes.
- `♻️ refactor`: Code refactoring.
- `⚡️ perf`: Performance improvements.
- `✅ test`: Adding or fixing tests.
- `⏪️ revert`: Reverting previous commits.

*(Note: For breaking changes, use the `💥` emoji: e.g., `💥 feat(api)!: rewrite system` or as a footer `💥 BREAKING CHANGE: ...`)*

## Rules
1. **Gitmoji Prefix**: Every commit message MUST start with the appropriate unicode emoji (e.g., `✨`), followed by a space, then the Conventional Commit type. Do not use the text alias (e.g., use `✨` instead of `:sparkles:`).
2. **Scope**: Optional. A noun describing a section of the codebase surrounded by parentheses (e.g., `✨ feat(parser): ...`).
3. **Description**: A short summary of the code changes. Use the imperative, present tense: "add" not "added". Do not capitalize the first letter and do not place a period at the end.
4. **Body & Footer**: Optional. If provided, they must be separated by a blank line.
5. **Breaking Changes**: Must be indicated by an exclamation mark `!` before the colon (e.g., `💥 fix(core)!: ...`) or a `BREAKING CHANGE: ` footer.

## Output
Produce ONLY the raw commit message text. Do not wrap the output in markdown code blocks and do not add any conversational text.
