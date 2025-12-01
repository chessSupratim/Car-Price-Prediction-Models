# 🚗📈 Auto-Insight: Car Price Prediction & Insights from Indian Listings
 
Auto-Insight is an end-to-end **Data Science project** designed to predict car prices from Indian car listings.  
It covers **data cleaning, exploratory analysis, machine learning model development**, and an **interactive Streamlit dashboard** for real-time predictions.  
Users can select multiple trained models and visually compare their predictions.

## Project Purpose

This project was developed as part of the **DA 2040: Data Science in Practice** course at **IISc Bangalore (M.Tech Online, 2025–2028)**.  
**Team Data Pack**:
- Binayak Chakraborty: binayakc@iisc.ac.in  *(13-19-02-19-52-25-1-26269)*
- Supratim Dey: supratimdey@iisc.ac.in  *(13-19-02-19-52-25-1-26238)*
- Rohit Agarwal: rohitagarwal@iisc.ac.in  *(13-19-02-19-52-25-1-26288)*
- Rituparno Chatterjee: rituparnoc@iisc.ac.in  *(13-19-02-19-52-25-1-26255)*

## Problem Statement
Pricing in the Indian used-car market lacks transparency and consistency, making it difficult for buyers and sellers to make informed decisions. This project aims to leverage data science and machine learning to predict car resale prices and uncover key factors influencing valuation.

## Brief description of the dataset(s)
- Features: Rows = 140K, Columns = 12 (String = 8, Int = 3, Bool = 1)
- Size: 11 MB
- Format: .csv
- Fields: Brand, Model name, Year, Price, KM Driven, Fuel Type, Transmission, Owner etc.
 
## 📊 Project Overview
 
This app demonstrates an **end-to-end Data Science workflow**:
 
1. Data collection & cleaning  
2. Feature engineering and preprocessing  
3. EDA
4. Model development, training, evaluation & saving (`joblib`)  
5. Interactive Dashboard deployment with **Streamlit**  

**Data Source:** [Kaggle Car Dataset](https://www.kaggle.com/datasets/milapgohil/car-dataset)
 
---
 
## 🧠 High-level approach and methods used (Models Implemented)

| **Model**           | **Description**                                                   |
|----------------------|-------------------------------------------------------------------|
| Linear Regression    | Baseline model for interpretability.                             |
| Random Forest        | Handles non-linear relationships and provides feature importance.|
| XGBoost              | Gradient boosting for high accuracy and efficiency.              |
| LightGBM             | Optimized for large datasets and faster training.                |
| AdaBoost             | Improves weak learners through boosting.                         |
| Decision Tree        | Simple and interpretable model for quick insights.               |
| Weighted Ensemble    | Combines strengths of multiple models for better performance.    |
 
---

## Conclusion
All models showed relatively low predictive power, with XGBoost performing best (R² ≈ 0.293, MAE ≈ ₹2.88L, RMSE ≈ ₹3.49L). Tree-based models like RandomForest and LightGBM were close behind, while DecisionTree severely underperformed (negative R²), indicating poor generalization. Overall, results suggest the need for better feature engineering and hyperparameter tuning to improve accuracy.

