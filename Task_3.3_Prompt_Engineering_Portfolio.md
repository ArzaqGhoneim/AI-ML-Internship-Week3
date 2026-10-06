# Task 3.3 — Prompt Engineering Portfolio

**Student:** Arzaq Ghoneim  
**Internship:** Skill Set Go EduTech AI/ML Internship — Week 3

## Objective
Design, improve, and evaluate prompts for four common LLM tasks:
1. Reasoning
2. Information extraction
3. Summarization
4. Coding

> Important integrity note: this portfolio provides the prompt designs, evaluation criteria, and iteration framework. The "actual output" column should only be filled with output produced by the LLM tool actually used. Do not present generated/example text as a real API result.

---

## 1. Reasoning

### Initial prompt
```text
Solve this problem and give the answer.
```

### Improved prompt
```text
Solve the following problem step by step.
1. Identify the known information.
2. State the formula or rule you use.
3. Show the main calculation/reasoning steps clearly.
4. Give the final answer on a separate line.
Do not skip important reasoning steps.

Problem:
A dataset contains 800 samples. 20% are used for testing.
How many samples are in the test set?
```

### Why it is better
The improved version defines the desired reasoning structure and makes the final answer easy to identify.

### Evaluation criteria
- Correctness
- Completeness
- Clear structure
- No irrelevant content

### Actual outcome
Run the improved prompt in the selected LLM and paste the exact output here before final submission.

---

## 2. Information Extraction

### Initial prompt
```text
Extract the important information from this text.
```

### Improved prompt
```text
Extract the following fields from the text:
- Person name
- Organization
- Role
- Date
- Location

Return ONLY valid JSON using exactly these keys:
{
  "person_name": "",
  "organization": "",
  "role": "",
  "date": "",
  "location": ""
}

Text:
"Arzaq joined the Skill Set Go EduTech AI/ML internship in September 2026.
The internship is a practical AI/ML training program."
```

### Evaluation criteria
- Correct fields
- Correct values
- Valid JSON
- No extra text

### Actual outcome
Run the prompt and record the exact model response.

---

## 3. Summarization

### Initial prompt
```text
Summarize this paragraph.
```

### Improved prompt
```text
Summarize the text in 4 bullet points.
Keep only the main ideas and important technical terms.
Do not add information that is not present in the source.
Use simple English.

Text:
"Convolutional neural networks are commonly used for image classification.
Convolution layers learn local visual patterns, pooling reduces spatial
dimensions, and dense layers combine learned features to make the final
classification."
```

### Evaluation criteria
- Main ideas preserved
- Concise
- No hallucinated facts
- Technical terms retained
- Easy to read

### Actual outcome
Run the prompt and record the exact model response.

---

## 4. Coding

### Initial prompt
```text
Write Python code to clean a dataset.
```

### Improved prompt
```text
Write a beginner-friendly Python function using pandas.

Requirements:
- Input: a pandas DataFrame
- Remove duplicate rows
- Report the number of missing values before cleaning
- Fill numeric missing values with the median
- Return the cleaned DataFrame
- Include short comments
- Do not use libraries other than pandas
```

### Evaluation criteria
- Code runs
- Requirements are all satisfied
- Correct pandas usage
- Readable code
- No unnecessary dependencies

### Actual outcome
Run the prompt, execute the returned code, and record whether it worked on a small test DataFrame.

---

## Prompt Evaluation Sheet

| Task | Initial Prompt | Improvement | Evaluation Criteria | Actual Outcome |
|---|---|---|---|---|
| Reasoning | Too vague | Structured steps + final answer | Correctness, completeness, clarity | Fill after actual LLM run |
| Extraction | Too vague | Fixed fields + JSON format | Accuracy, valid JSON | Fill after actual LLM run |
| Summarization | Too vague | Length + focus + no additions | Relevance, conciseness | Fill after actual LLM run |
| Coding | Too vague | Language, library, requirements, constraints | Correctness, execution | Fill after actual LLM run |

## General Lessons
- Specific prompts generally reduce ambiguity.
- Output format instructions make evaluation easier.
- Constraints such as library restrictions help control generated code.
- Evaluation should use explicit criteria instead of judging prompts only by appearance.
