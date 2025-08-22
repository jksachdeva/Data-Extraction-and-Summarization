# Data-Extraction-and-Summarization

## Overview
This project implements a professional, modular agentic pipeline for extracting key information and generating summaries from a large-scale news article dataset stored on Google Cloud Platform (GCP). The workflow leverages Google Cloud Storage, BigQuery, Natural Language API, and Vertex AI Gemini, and is designed for extensibility, reproducibility, and clarity.

## Components

### 1. Configuration (`src/config.py`)
Holds all project parameters (e.g., GCP bucket name, file name) for easy adjustment and reproducibility.

### 2. Data Loading (`src/load_data.py`)
Loads news records from a JSONL file stored in a GCP bucket into a pandas DataFrame, ready for downstream processing.

### 3. Preprocessing (`src/preprocess.py`)
Performs exploratory data analysis:
- Displays shape, sample records, and missing value counts.
- Plots the distribution of news categories.
- Analyses description length and plots distribution.
- Extracts top words per category, excluding stopwords and punctuation.

### 4. Entity and Sentiment Extraction (`src/entity_extraction.py`)
Uses Google Cloud Natural Language API to extract entities and sentiment scores from news descriptions.

### 5. Summarization (`src/summarization.py`)
Uses Vertex AI Gemini model to summarize news descriptions into concise single-sentence summaries.

---

## Pipeline Usage

1. **Update Configuration:**  
   Set GCP resource names in `src/config.py`.

2. **Load Data:**  
   Use `load_news_data()` from `src/load_data.py` to obtain a DataFrame.

3. **Preprocess:**  
   Import and apply functions from `src/preprocess.py` for EDA and basic NLP analyses.

4. **Entity & Sentiment Extraction:**  
   Use `extract_entities(text)` and `extract_sentiment(text)` from `src/entity_extraction.py` for NLP enrichment.

5. **Summarization:**  
   Use `summarize_text(text)` from `src/summarization.py` to generate summaries.

---

## Evaluation

### Qualitative Assessment
- **Entity Extraction:**  
  Output entities are relevant and accurate for most articles (e.g., people, organizations, locations). Manual spot-checks show good coverage
- **Sentiment Analysis:**  
  Sentiment scores generally align with article tone—positive for uplifting news, negative for controversies or tragedies.
- **Summarization:**  
  Summaries are concise, often correctly capturing the main point. Results are readable and informative.

### Quantitative Assessment
- No gold standard dataset is available for quantitative scoring.  
  Evaluation is based on manual review and comparison to source descriptions.

---

## Comparison with Traditional NLP Baselines

To assess the performance of the advanced GCP models, traditional NLP baselines were applied for comparison:

| Component           | GCP/Vertex AI Model                | Baseline (SpaCy, TextRank)    | Observations                 |
|---------------------|------------------------------------|-------------------------------|------------------------------|
| Entity Extraction   | GCP Natural Language API           | SpaCy NER                     | GCP detected slightly more fine-grained entities; SpaCy performed well but missed some org/location cases. |
| Summarization       | Vertex AI Gemini                   | TextRank                      | Gemini summaries were more fluent and context-aware; TextRank tended to extract sentences verbatim and sometimes missed the main point. |

