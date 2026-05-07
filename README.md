# AI-Driven Autism Behavioral Analytics

## Overview
This project analyzes behavioral screening data related to Autism Spectrum Disorder (ASD) using Python, Machine Learning, and Tableau.

The project combines:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Machine learning classification
- Behavioral segmentation using clustering
- Interactive Tableau dashboarding

The goal is to identify behavioral patterns associated with ASD and provide analytical insights through data visualization.

---

## Objectives

- Analyze behavioral assessment data
- Predict ASD outcomes using machine learning
- Identify behavioral clusters using K-Means clustering
- Visualize demographic and behavioral insights
- Build an interactive Tableau dashboard

---

## Dataset

Dataset includes:
- Behavioral assessment scores (A1–A10)
- Demographic attributes
- ASD classification labels

Total records:
- 704 participants

---

## Technologies Used

### Programming & Analytics
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### Visualization
- Tableau Public
- Matplotlib
- Seaborn

---

## Project Structure

```bash
AI_ASD_Analytics_Project/
│
├── data/
├── notebooks/
├── src/
├── dashboard/
├── README.md
└── requirements.txt
```

---

## Exploratory Data Analysis

Performed:
- Behavioral score distribution analysis
- Gender-based ASD analysis
- Ethnicity distribution analysis
- Correlation heatmaps
- Behavioral trend analysis

---

## Feature Engineering

Created behavioral features including:
- behavior_total_score
- communication_score
- social_interaction_score
- behavior_variability_score

---

## Machine Learning Models

Implemented:
- Logistic Regression
- Random Forest
- XGBoost

Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1-score

---

## Behavioral Segmentation

Used:
- K-Means Clustering
- PCA visualization

Goal:
- Identify behavioral risk groups
- Segment participants by behavioral patterns

---

## Tableau Dashboard



![Dashboard Screenshot](autismdashboard.png)

The Tableau dashboard includes:
- KPI metrics
- Demographic insights
- ASD behavioral analysis
- Cluster distribution analysis

---

## Key Insights

- ASD-positive participants showed significantly higher behavioral scores.
- Certain behavioral indicators strongly contributed to ASD classification.
- Clustering identified distinct behavioral groups with varying severity levels.

---

## Future Improvements

- Hyperparameter tuning
- Model deployment with Streamlit
- Real-time prediction interface
- Advanced explainable AI analysis
