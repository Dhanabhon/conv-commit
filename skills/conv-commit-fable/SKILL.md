---
name: conv-commit-fable
description: Use this skill ONLY when the user explicitly requests a fable, fairy-tale, folklore, mythical, epic, tale, storybook, or Aesop-style conventional commit. Do not use this for standard, concise, detailed, sarcastic, or gitmoji commits.
---

Skill instructions for the agent to follow:

When generating a commit message, you must follow the Conventional Commits v1.0.0 specification while turning the change into a short fable, myth, or storybook tale. The message must remain technically accurate even when the wording is playful.

## Message Format

```
<type>[optional scope]: <description>

<body>

[optional footer(s)]
```

## Types
The `<type>` must be one of the following: `feat`, `fix`, `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`, `revert`.

## Rules
1. **Scope**: Include a scope when the changed area is clear.
2. **Description**: Use a short, imperative, present-tense summary with fable flavor while still naming the real change (for example, `fix(memory): slay the dreadful memory leak dragon`).
3. **Body (MANDATORY)**: Include a body separated from the description by one blank line. Write 1-2 compact paragraphs as a fable, tale, myth, or storybook scene. Use fantasy metaphors such as kingdoms, dragons, curses, quests, scrolls, or sages only when they map to the actual diff.
4. **Technical Truth**: Preserve the real behavior, files, feature, bug, or documentation change. Do not invent unrelated systems, fake issue numbers, fake benchmarks, or fake line numbers.
5. **Moral**: Optionally end the body with a short `Moral:` sentence when it adds charm without obscuring the technical meaning.
6. **Footer**: Include footers only for related issues or breaking changes.
7. **Breaking Changes**: Use a valid `BREAKING CHANGE: ` footer and keep the migration impact clear, even if the wording stays mythical.

## Output
Produce ONLY the raw commit message text. Do not wrap the output in markdown code blocks and do not add conversational text.
