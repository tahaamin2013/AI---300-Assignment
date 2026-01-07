---
name: summary-creation
description: Read long content such as documentation, assignments, specs, or articles and convert it into a short, clear summary. Extracts key points, decisions, and actions while removing unnecessary details. Makes information easy to understand and reuse later.
---

# Summary Creation

This skill helps create concise, clear summaries of long content while preserving the most important information.

## What This Skill Does

1. **Remove unnecessary details** - Filter out redundant information and examples
2. **Extract key points** - Identify main ideas, decisions, and actionable items
3. **Create short, readable summaries** - Produce summaries that are 10-20% of original length
4. **Save mental effort** - Make complex information quickly digestible

## When to Use This Skill

Use this skill when you need to:
- Summarize long documents, articles, or reports
- Create executive summaries of detailed content
- Extract key points from technical documentation
- Condense meeting notes or assignment requirements
- Create quick reference guides from comprehensive materials

## Summary Structure

### Basic Summary Format
- **Purpose**: What is the main goal or topic?
- **Key Points**: 3-5 most important ideas or findings
- **Decisions/Actions**: Any conclusions or next steps
- **Impact**: Why this information matters

### Technical Document Format
- **Problem Statement**: What issue is being addressed?
- **Solution**: Main approach or methodology
- **Results**: Key findings or outcomes
- **Implications**: What this means for the reader

### Article/Report Format
- **Context**: Background information
- **Main Argument**: Central thesis or finding
- **Evidence**: Key supporting points
- **Conclusion**: Final takeaways or recommendations

## Summary Guidelines

### Length Guidelines
- **Original content**: 1-5 pages → **Summary**: 3-5 bullet points
- **Original content**: 5-20 pages → **Summary**: 1 paragraph
- **Original content**: 20+ pages → **Summary**: 2-3 paragraphs

### Quality Standards
- **Clarity**: Use simple, direct language
- **Accuracy**: Preserve original meaning without distortion
- **Completeness**: Include all essential information
- **Relevance**: Focus on information most important to the reader

### What to Remove
- Repetitive examples and explanations
- Detailed background not essential to understanding
- Minor details and tangential information
- Technical jargon that doesn't add value
- Long quotes and citations (summarize instead)

### What to Keep
- Main ideas and central arguments
- Key statistics and findings
- Important definitions and concepts
- Action items and decisions
- Cause-and-effect relationships

## Examples

### Example 1: Technical Documentation
**Original**: 15-page API documentation with detailed examples
**Summary**: 1 paragraph describing the API's purpose, key endpoints, and usage patterns

### Example 2: Meeting Notes
**Original**: 3 pages of discussion notes with multiple viewpoints
**Summary**: 3-5 bullet points covering decisions made, action items, and next steps

### Example 3: Research Article
**Original**: 25-page academic paper with methodology, results, and analysis
**Summary**: 2 paragraphs covering the research question, methodology, key findings, and implications

## Tools and Scripts

### summarize.py
Python script for automated text summarization using extractive methods.

Usage:
```bash
python scripts/summarize.py input.txt --length 3 --output summary.txt
```

Parameters:
- `--length`: Number of sentences in summary (default: 3)
- `--output`: Output file path
- `--method`: Summarization method (extractive/abstractive)

### text-analysis.py
Script for analyzing text structure and identifying key sections.

Usage:
```bash
python scripts/text-analysis.py document.txt
```

Outputs:
- Key topics and themes
- Sentence importance scoring
- Section analysis
- Vocabulary complexity assessment

## References

- [Summary Writing Best Practices](references/writing-guidelines.md)
- [Technical Documentation Summary Templates](references/templates.md)
- [Executive Summary Examples](references/examples.md)
- [Content Analysis Methods](references/analysis-methods.md)

## Tips for Effective Summaries

1. **Read completely first** - Understand the full context before summarizing
2. **Identify the audience** - Tailor summary complexity to the reader's knowledge level
3. **Use active voice** - Make summaries more engaging and direct
4. **Maintain logical flow** - Preserve the original structure's logic
5. **Check for completeness** - Ensure no critical information is omitted
6. **Test readability** - Read summary without original text to verify clarity