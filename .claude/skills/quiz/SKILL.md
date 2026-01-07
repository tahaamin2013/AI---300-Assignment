---
name: quiz
description: Generate assessment quizzes from study notes with structured question types (multiple choice, short answer, essay), answer keys with explanations, and personalized review recommendations. Use when the user requests: (1) quiz generation from study notes, (2) assessment tests, (3) practice questions, (4) self-evaluation tools, or (5) mentions creating quizzes to test understanding of material.
---

# Quiz

Generate comprehensive assessment quizzes from study notes with answer keys, performance analysis, and personalized review recommendations.

## Workflow

### 1. Extract Key Concepts

Analyze the study notes to identify:
- Core concepts and definitions
- Important processes or procedures
- Relationships between topics
- Application scenarios
- Higher-order thinking opportunities (synthesis, evaluation)

### 2. Generate 5 Quiz Questions

Create exactly 5 questions following this distribution:

#### 2 Multiple Choice Questions (Testing Concepts)
- Test fundamental understanding of key concepts
- Include 4 answer options (A-D)
- Ensure distractors are plausible but clearly incorrect
- Focus on recall and comprehension

**Format:**
```
Q1. [Question stem]
A) [Option]
B) [Option]
C) [Option]
D) [Option]
```

#### 2 Short Answer Questions (Testing Application)
- Test ability to apply concepts to scenarios
- Require 2-3 sentence responses
- Focus on practical problem-solving
- Include realistic contexts

**Format:**
```
Q3. [Question with scenario requiring application]
```

#### 1 Essay Question (Testing Synthesis)
- Test ability to synthesize multiple concepts
- Require integration of ideas
- Encourage critical thinking
- Ask for analysis, comparison, or evaluation

**Format:**
```
Q5. [Question requiring synthesis of multiple concepts]
```

### 3. Provide Answer Key with Explanations

For each question, provide:

#### Multiple Choice Answers
- Correct answer letter
- 2-3 sentence explanation of why it's correct
- Brief explanation of why other options are incorrect

**Format:**
```
Q1. Correct Answer: [B]
Explanation: [Why B is correct and why others are not]
```

#### Short Answer Answers
- Key points that must be included (3-4 points)
- Example of a strong answer (2-3 sentences)
- Common mistakes to avoid

**Format:**
```
Q3. Key Points:
- [Point 1]
- [Point 2]
- [Point 3]

Example Answer: [Sample response incorporating key points]
```

#### Essay Answer
- Thesis or main argument expected
- Key concepts that should be addressed (4-6 points)
- Structure guidance (introduction, body, conclusion)
- Example outline or strong response

**Format:**
```
Q5. Expected Response:
Thesis: [Main argument]

Key Concepts to Address:
- [Concept 1]
- [Concept 2]
- [Concept 3]
- [Concept 4]

Example Outline:
[Structure showing how to integrate concepts]
```

### 4. Identify Knowledge Gaps

After presenting the quiz and answer key, provide guidance on interpreting performance:

**Gap Indicators:**

Multiple Choice Performance:
- 0/2 correct: Fundamental concept gaps - requires comprehensive review
- 1/2 correct: Partial understanding - needs targeted concept reinforcement
- 2/2 correct: Strong foundational knowledge

Short Answer Performance:
- Missing >2 key points per question: Application skills need development
- Missing 1-2 key points: Partial application ability - practice needed
- All key points included: Strong application skills

Essay Performance:
- Addresses <50% of key concepts: Synthesis skills need significant development
- Addresses 50-75% of key concepts: Emerging synthesis ability
- Addresses >75% of key concepts: Strong synthesis and integration skills

### 5. Recommend Review Sections

Based on question performance, map each question back to specific study note sections:

**Format:**
```
Review Recommendations:

If you struggled with Q1 (Multiple Choice):
→ Review: [Section name/topic from study notes]
→ Focus on: [Specific concept to reinforce]

If you struggled with Q2 (Multiple Choice):
→ Review: [Section name/topic from study notes]
→ Focus on: [Specific concept to reinforce]

If you struggled with Q3 (Short Answer):
→ Review: [Section name/topic from study notes]
→ Focus on: [Application skill to practice]

If you struggled with Q4 (Short Answer):
→ Review: [Section name/topic from study notes]
→ Focus on: [Application skill to practice]

If you struggled with Q5 (Essay):
→ Review: [Multiple sections covering integrated concepts]
→ Focus on: [How concepts connect and interact]
```

## Output Structure

Present the complete quiz in this order:

1. **Quiz Title and Instructions**
2. **5 Questions** (clearly numbered Q1-Q5)
3. **Answer Key** (with explanations for all questions)
4. **Performance Interpretation Guide** (gap indicators)
5. **Review Recommendations** (section mappings)

## Example Usage

User: "Create a quiz from my study notes on photosynthesis"

1. Read and analyze the study notes
2. Identify key concepts (light reactions, Calvin cycle, etc.)
3. Generate 2 MC questions on fundamental concepts
4. Generate 2 SA questions on applying knowledge to scenarios
5. Generate 1 essay question on synthesizing the full process
6. Provide answer key with detailed explanations
7. Include performance interpretation guidance
8. Map each question back to specific sections of the study notes

## Quality Standards

- Questions must be clear, unambiguous, and aligned with learning objectives
- Multiple choice distractors should reflect common misconceptions
- Short answer scenarios should be realistic and relevant
- Essay questions should require genuine synthesis, not just summary
- Explanations should teach, not just verify answers
- Review recommendations should be specific and actionable
