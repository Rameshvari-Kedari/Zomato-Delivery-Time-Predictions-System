# 🚴 Zomato Delivery Time Prediction System

## 📌 Project Overview

An end-to-end **Machine Learning regression project** using the **Zomato Delivery Dataset from Kaggle** to predict food delivery time and support proactive delivery operations.

The project analyzes factors such as **traffic, weather, vehicle condition, delivery distance, multiple deliveries, festival conditions, city, and delivery partner information** to estimate the expected delivery time.

### 🎯 Business Objective

> Predict delivery time accurately enough to identify potentially delayed orders and support proactive operational decisions.

---

## 📊 Dataset

**Source:** Zomato Delivery Dataset — Kaggle

**Target Variable:** `Time_taken (min)`

Key features used include:

* Delivery person rating
* Weather conditions
* Road traffic density
* Vehicle condition
* Type of vehicle
* Multiple deliveries
* Festival
* City
* Delivery distance
* Order-to-pickup time
* Day of week

---

## 🔍 Project Workflow

```text
Business Understanding
        ↓
Data Understanding
        ↓
EDA & Data Quality Analysis
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
Preprocessing Pipeline
        ↓
Cross-Validation
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Final Model
        ↓
Streamlit Deployment
```

---

## 🛠️ Feature Engineering

Important engineered features include:

* **Distance (****`distance_km`****)** — restaurant-to-customer distance
* **Order-to-pickup time (****`order_to_pickup_min`****)**
* **Order day of week**

Categorical and numerical features were handled through a **Scikit-learn preprocessing pipeline**.

---

## 🤖 Models Evaluated

The project compares multiple regression models, including:

* Linear Regression
* Random Forest
* Extra Trees
* LightGBM

Tree-based ensemble models performed better than the linear baseline.

---

## 🏆 Model Performance

The final model achieved:LightGBM

| Metric       |           Result |
| ------------ | ---------------: |
| **MAE**      | **3.06 minutes** |
| **RMSE**     | **3.78 minutes** |
| **R² Score** |         **0.84** |

---

## 💡 Business Use

The predicted delivery time can be used by an internal operations system to:

* Estimate expected delivery time
* Identify potentially delayed orders
* Support proactive operational action
* Improve delivery-time communication
* Monitor delivery performance

---

## 🚀 Deployment

The project is being extended into a **Streamlit application** where users can enter order-related information and receive a predicted delivery time along with operational recommendations.

---

## 🧰 Tech Stack

**Python · Pandas · NumPy · Scikit-learn · LightGBM · Matplotlib · Seaborn · Joblib · Streamlit**

---

## 📁 Project Structure

```text
Food-Delivery-Time-Forecasting-Proactive-Operations-System/
│
├── data/
├── notebooks/
│   ├── 01_Data_understanding_EDA_and_Feature_Engg.ipynb
│   └── Model_Training_and_Evaluation.ipynb
│
├── models/
├── app/
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

* Real-time weather integration
* Real-time traffic information
* Improved route-distance calculation
* Delivery delay-risk classification
* Model monitoring and drift detection
* Automated model retraining

---

Live Demo : https://zomato-delivery-time-predictions-system-nqhr7szyptj8hnzk2y4q9i.streamlit.app/
