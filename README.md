# Task 08: Bias Detection in LLM Data Narratives

This repository contains the complete implementation of Research Task 08, which examines how Large Language Models (LLMs) may produce biased narratives when interpreting identical data under different prompt framings.  
The project explores narrative bias in the context of anonymized basketball statistics (Players A–E) using systematic and reproducible methods.

All work included here follows Syracuse University OPT research guidelines, including dataset anonymization, reproducible analysis, and separation of raw model outputs.

---

## 📘 Project Overview

LLMs can generate different interpretations of the same data depending on how a question is framed. In this project, I evaluate four types of potential bias:

- **Confirmation Bias**  
- **Negative Framing Bias**
- **Positive Framing Bias**
- **Demographic Bias**  

All prompts reference the same dataset, allowing the framing of the question to be the only independent variable.  
Model responses are collected manually and stored locally to comply with OPT and FERPA regulations.

The final report (`REPORT.md`) summarizes the findings, methods, and conclusions from the bias evaluation.

---

## 📂 Repository Structure

Task_08_Bias_Detection/
│
├── data/
│   └── anonymized_stats.csv         # Only dataset allowed in repo (PII removed)
│
├── prompts/                         # Prompt templates for each bias condition
│   ├── confirmation_bias.txt
│   ├── framing_positive.txt
│   ├── framing_negative.txt
│   └── demographic_bias.txt
│
├── experiments/                     # Python scripts for running experiments
│   ├── experiment_design.py         # Generates prompt JSON from dataset
│   ├── run_experiment.py            # Helps log/structure LLM responses
│   ├── analyze_bias.py              # Creates tables, plots, bias metrics
│   └── validate_claims.py           # Checks numerical accuracy of LLM outputs
│
├── results/                         # Real LLM outputs stored locally only
│   └── .keep                        # (folder tracked, contents ignored)
│
├── analysis/                        # Auto-generated analysis outputs (tables/graphs)
│
├── REPORT.md                        # Full written report for Task 08
└── README.md                        # You are here

---

## 🛠️ How to Run the Pipeline

Before running the scripts, install dependencies:

pip install -r requirements.txt

Then run the pipeline in order:

### **1️⃣ Create Prompt Variations**
Generates all prompts in JSON format based on the dataset.

python experiments/experiment_design.py

### **2️⃣ Collect LLM Responses**
This script provides structure for logging responses.  
You will manually copy and paste LLM outputs (Gemini, ChatGPT, Claude, etc.) into:

results/experiment_log.json

python experiments/run_experiment.py

### **3️⃣ Run Bias + Sentiment Analysis**
Produces CSV tables and graphs inside the analysis/ folder.

python experiments/analyze_bias.py

### **4️⃣ Validate Numerical Claims**
Checks whether LLM outputs match the ground-truth dataset.

python experiments/validate_claims.py

---

## 🧪 Experiment Design Summary

- **Data:** Five anonymized players (A–E)
- **Metrics:** Points, Rebounds, Assists, Steals
- **Bias Types Tested:** Confirmation, Positive/Negative Framing, Demographic
- **Independent Variable:** Prompt phrasing only
- **Dependent Variable:** Narrative content of LLM output
- **Models Tested:** Gemini (others optional)

All prompts reference the same dataset to isolate narrative drift caused by framing.

---

## 📄 Final Report

The full analysis—including hypotheses, results, bias catalogue, mitigation strategies, and limitations—is found in:

REPORT.md

This document serves as the primary deliverable for Research Task 08.

---

## 🔒 Compliance Notes

- No raw or identifiable datasets are included.  
- All player names are replaced with anonymous identifiers.  
- Only anonymized_stats.csv is committed.  
- The results/ folder is intentionally excluded via .gitignore.  
- The repository is fully reproducible and clean of PII.

---
