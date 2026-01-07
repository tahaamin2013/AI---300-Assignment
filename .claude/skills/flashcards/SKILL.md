---
name: flashcards
description: Transform study notes into spaced repetition flashcards with tiered difficulty levels (Easy, Medium, Hard), formatted for Anki or similar tools. Use when the user requests: (1) flashcards from study notes, (2) spaced repetition cards, (3) quiz cards from notes, (4) to convert notes to Anki format, or (5) mentions creating cards for memorization. Can consume output from study-notes skill or any structured notes.
---

# Flashcards Skill

## Procedure

### 1. Input Analysis

Identify the source material:
- If user references output from study-notes skill, use the "Critical Concepts for Flashcards" section and section content
- If user provides raw notes, scan for key concepts, definitions, processes, and relationships
- Extract 8-12 core concepts suitable for flashcard generation

### 2. Concept Selection and Categorization

Select exactly 5 concepts for flashcard generation:
- **2 Easy (definition-level)**: Focus on basic definitions, terminology, or simple facts
- **2 Medium (application-level)**: Focus on understanding how concepts work, comparisons, or cause-effect relationships
- **1 Hard (synthesis-level)**: Focus on combining multiple concepts, analysis, or higher-order thinking

**Selection criteria:**
- Prioritize 🔴 flagged concepts from study-notes output (if available)
- Choose concepts that are foundational to understanding the topic
- Ensure concepts are discrete and testable
- Prefer concepts that appear across multiple sections (these are critical knowledge)

### 3. Flashcard Generation

For each of the 5 selected concepts, create a flashcard with:

**Front (Question):**
- Clear, specific question that tests understanding
- Easy: "What is...?", "Define...", "What does... mean?"
- Medium: "How does... work?", "What is the difference between... and...?", "Why does...?"
- Hard: "How do... and... relate to create...?", "Analyze...", "Compare and contrast..."
- Include enough context that the question is unambiguous

**Back (Answer):**
- Concise but complete answer (2-4 sentences for Easy, 3-5 for Medium, 4-6 for Hard)
- Include key details without overwhelming
- For Medium/Hard: Include reasoning or connections
- Use precise terminology from source material

### 4. Critical Knowledge Flagging

After generating all 5 flashcards, identify which concepts appear in multiple cards or connect to multiple other concepts. Flag these with:
- 🔴 **Critical Knowledge**: Concepts that appear in 2+ flashcards or are foundational to multiple other concepts
- List flagged concepts at the end with brief explanation of why they're critical

### 5. Output Format

Format flashcards for spaced repetition import (see [references/anki-format.md](references/anki-format.md)):

```
# Flashcards: [Topic Name]

## Easy Cards (Definition-Level)

### Card 1
**Front:** [Question]

**Back:** [Answer]

**Concept:** [Concept name]

---

### Card 2
**Front:** [Question]

**Back:** [Answer]

**Concept:** [Concept name]

---

## Medium Cards (Application-Level)

### Card 3
**Front:** [Question]

**Back:** [Answer]

**Concept:** [Concept name]

---

### Card 4
**Front:** [Question]

**Back:** [Answer]

**Concept:** [Concept name]

---

## Hard Cards (Synthesis-Level)

### Card 5
**Front:** [Question]

**Back:** [Answer]

**Concept:** [Concept name]

---

## Critical Knowledge

🔴 **[Concept]** - Appears in Cards X, Y; foundational to understanding [why it's critical]
🔴 **[Concept]** - Connects [concept A] and [concept B]; essential for [reason]

---

## Anki Import Format

[Copy-paste ready format - see references/anki-format.md]
```

## Quality Criteria

### Question Clarity
- Questions are unambiguous and specific
- Difficulty level matches question type (definition vs application vs synthesis)
- Questions test understanding, not memorization of exact wording
- Context is provided when needed

### Answer Completeness
- Answers are complete but concise
- Key details are included without overwhelming
- Answers use terminology from source material
- Medium/Hard answers explain reasoning or connections

### Difficulty Calibration
- Easy: Can be answered with simple recall of definition or fact
- Medium: Requires understanding and application of concept
- Hard: Requires synthesis of multiple concepts or higher-order analysis

### Critical Knowledge Accuracy
- Correctly identifies concepts that span multiple flashcards
- Accurately explains why flagged concepts are critical
- Only flags truly foundational concepts (avoid over-flagging)

## Interdependency with Study-Notes Skill

This skill is designed to consume output from the study-notes skill:

1. **Direct handoff**: When user runs study-notes first, use the "Critical Concepts for Flashcards" section as primary source
2. **Priority concepts**: 🔴 flagged concepts should be prioritized over 🟡 concepts
3. **Section content**: Pull definitions and examples from section content for flashcard answers
4. **Cross-references**: Use section connections to identify critical knowledge that spans multiple concepts

**Workflow example:**
```
User: "Study photosynthesis"
→ study-notes skill generates structured notes
→ User: "Create flashcards from these notes"
→ flashcards skill consumes the structured output
```

## Notes

- Always generate exactly 5 cards (not more, not less)
- If source material has <5 concepts, ask user for more material
- If source material has >12 concepts, select the most fundamental 5
- Format must be compatible with Anki for spaced repetition
