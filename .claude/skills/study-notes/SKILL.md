# Study Notes Skill

## Description
Transforms any study topic or concept into comprehensive, structured study notes with clear sections, key points, practical examples, and flagged critical concepts for flashcard creation.

## Activation
This skill activates when:
- User asks "study [topic]" or "help me study [topic]"
- User says "help me learn [concept]"
- User requests "create study notes for [topic]"
- User asks "teach me about [subject]"

## Procedure

1. **Analyze and Section the Topic**
   - Identify the core topic or concept provided by the user
   - Break the topic into 5-7 logical key sections that cover the subject comprehensively
   - Order sections from foundational concepts to advanced applications
   - Ensure sections have clear, descriptive titles

2. **Develop Each Section with Three Components**
   - **Definition**: Provide a clear, concise definition of the section's concept
   - **Key Points**: List 3-4 essential bullet points that explain the most important aspects
   - **Practical Examples**: Include 1-2 concrete, real-world examples that illustrate the concept

3. **Create Inter-Section Connections**
   - Identify how each section relates to others
   - Add brief connection statements showing conceptual links
   - Build a narrative flow between sections

4. **Generate Integrative Summary**
   - Write a summary paragraph (3-5 sentences) that:
     - Synthesizes all sections into a cohesive whole
     - Highlights the main takeaway from the topic
     - Shows how individual sections connect to form the complete picture

5. **Flag Critical Concepts for Flashcards**
   - Identify 5-8 discrete, fundamental concepts suitable for flashcards
   - Mark each with 🔴 for high-priority or 🟡 for medium-priority
   - Ensure concepts are testable, specific, and essential to understanding

## Output Format

```
# [TOPIC TITLE]

## Section 1: [Section Name]
**Definition:** [Clear definition]

**Key Points:**
- [Point 1]
- [Point 2]
- [Point 3]
- [Point 4 if applicable]

**Examples:** [1-2 practical examples]

---

## Section 2: [Section Name]
[Same structure repeats for 5-7 sections]

---

## Summary
[3-5 sentence synthesis connecting all sections and highlighting main takeaway]

## Critical Concepts for Flashcards
🔴 **[Concept 1]** - [Brief explanation]
🔴 **[Concept 2]** - [Brief explanation]
🟡 **[Concept 3]** - [Brief explanation]
🟡 **[Concept 4]** - [Brief explanation]
[Continue for 5-8 total concepts]
```

## Quality Criteria

### Specificity
- Each section contains concrete, specific information (not vague generalizations)
- Key points are actionable and detailed
- Examples are realistic and clearly tied to the concept
- Definitions use precise terminology

### Connection Between Sections
- Clear narrative flow from one section to the next
- Explicit connection statements linking related concepts
- Summary demonstrates how sections form a unified whole
- No isolated or disconnected information

### Flashcard Readiness
- Flagged concepts are discrete and testable
- Each concept can stand alone as a study item
- Concepts represent fundamental knowledge
- Priority levels (🔴/🟡) reflect importance to overall understanding

## Example

**Input:** "Photosynthesis"

**Output:**

```
# Photosynthesis

## Section 1: Overview & Definition
**Definition:** Photosynthesis is the biological process by which plants, algae, and some bacteria convert light energy into chemical energy stored in glucose, using carbon dioxide and water as raw materials.

**Key Points:**
- Occurs primarily in chloroplasts of plant cells
- Produces glucose (C₆H₁₂O₆) and oxygen (O₂) as products
- Requires light energy, carbon dioxide (CO₂), and water (H₂O)
- Foundation of most food chains on Earth

**Examples:** A maple tree uses sunlight to convert CO₂ from air and H₂O from soil into glucose for growth, releasing O₂ that animals breathe.

---

## Section 2: Light-Dependent Reactions
**Definition:** The first stage of photosynthesis occurring in the thylakoid membranes, where light energy is captured and converted into chemical energy (ATP and NADPH).

**Key Points:**
- Takes place in thylakoid membranes of chloroplasts
- Light is absorbed by chlorophyll and other pigments
- Produces ATP through chemiosmosis and NADPH through electron transport
- Water molecules are split (photolysis), releasing oxygen as a byproduct

**Examples:** When sunlight hits a chloroplast, photosystem II absorbs photons, energizing electrons that travel through an electron transport chain, similar to how solar panels convert light to electricity.

---

## Section 3: Calvin Cycle (Light-Independent Reactions)
**Definition:** The second stage of photosynthesis occurring in the stroma, where ATP and NADPH from light reactions are used to fix carbon dioxide into glucose.

**Key Points:**
- Takes place in the stroma of chloroplasts
- Uses ATP and NADPH from light-dependent reactions
- Carbon fixation: CO₂ is incorporated into organic molecules
- Produces glucose through a series of enzyme-catalyzed reactions

**Examples:** The Calvin Cycle works like an assembly line in a factory, where CO₂ molecules are added to a 5-carbon molecule (RuBP), processed through multiple steps, and eventually assembled into glucose.

---

## Section 4: Factors Affecting Photosynthesis Rate
**Definition:** Environmental and internal variables that influence the speed and efficiency of photosynthesis.

**Key Points:**
- Light intensity: Rate increases with light until saturation point
- Carbon dioxide concentration: Higher CO₂ increases rate up to a limit
- Temperature: Optimal range (25-35°C); extremes denature enzymes
- Water availability: Essential reactant; drought reduces photosynthesis

**Examples:** Greenhouse farmers manipulate these factors by adding supplemental CO₂, controlling temperature, and optimizing lighting to maximize crop growth rates.

---

## Section 5: Importance in Ecosystems
**Definition:** The critical role photosynthesis plays in energy flow, oxygen production, and carbon cycling in biological systems.

**Key Points:**
- Primary production: Forms the base of most food webs
- Oxygen production: Generates atmospheric O₂ for aerobic respiration
- Carbon sink: Removes CO₂ from atmosphere, mitigating climate change
- Energy storage: Converts solar energy into forms usable by heterotrophs

**Examples:** Tropical rainforests and ocean phytoplankton are major photosynthetic zones, producing about 50% of Earth's oxygen and serving as critical carbon sinks.

---

## Section 6: Cellular Structures & Pigments
**Definition:** The specialized organelles and molecules within plant cells that enable photosynthesis.

**Key Points:**
- Chloroplasts: Double-membrane organelles containing thylakoids and stroma
- Chlorophyll a & b: Primary pigments that absorb red and blue light
- Accessory pigments: Carotenoids capture additional light wavelengths
- Thylakoid arrangement: Stacked into grana for maximum surface area

**Examples:** The green color of leaves comes from chlorophyll reflecting green light while absorbing red and blue wavelengths for photosynthesis.

---

## Summary
Photosynthesis is a two-stage process that converts light energy into chemical energy stored in glucose. Light-dependent reactions capture solar energy in thylakoids, producing ATP and NADPH while releasing oxygen. These energy carriers then power the Calvin Cycle in the stroma, where CO₂ is fixed into glucose. The rate of photosynthesis depends on environmental factors like light, CO₂, temperature, and water. This process is fundamental to life on Earth, providing the oxygen we breathe and forming the foundation of most food webs.

## Critical Concepts for Flashcards
🔴 **Photosynthesis Equation** - 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂
🔴 **Chloroplast Structure** - Double membrane organelle with thylakoids (light reactions) and stroma (Calvin Cycle)
🔴 **Light-Dependent Reactions** - Occur in thylakoids, produce ATP and NADPH, release O₂ from water splitting
🔴 **Calvin Cycle** - Occurs in stroma, uses ATP/NADPH to fix CO₂ into glucose
🔴 **Carbon Fixation** - Process where CO₂ is incorporated into organic molecules via enzyme RuBisCO
🟡 **Limiting Factors** - Light intensity, CO₂ concentration, temperature, and water availability affect photosynthesis rate
🟡 **Chlorophyll Function** - Pigment that absorbs red and blue light, reflects green light
🟡 **Photosystem I & II** - Protein complexes in thylakoids that capture light energy and drive electron transport
```

## Notes
- Adjust the number of sections (5-7) based on topic complexity
- For simpler topics, use 5 sections; for complex topics, use 7
- Prioritize clarity and accessibility over technical jargon
- Ensure examples are relatable to the learner's context when possible
