# 🌾 Crop Recommendation System using Machine Learning

This project recommends the most suitable crop to grow based on environmental and soil conditions using machine learning models. It was developed as part of a practical application of ML in agriculture, aiming to support farmers and agriculturists with data-driven decisions.

---

## 📌 Project Motivation

In agriculture, choosing the right crop based on the soil's nutrient content and climate conditions can significantly improve yield and sustainability. This project leverages machine learning algorithms to analyze features such as:

- Nitrogen, Phosphorus, and Potassium (NPK) levels in the soil
- Temperature and humidity of the region
- Soil pH and expected rainfall

Using these parameters, the system predicts the most suitable crop to grow, helping optimize agricultural productivity.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **scikit-learn** – ML model training
- **pandas, numpy** – Data handling
- **matplotlib, seaborn** – Data visualization
- **joblib** – Model serialization
- **Streamlit** – Web-based user interface

---

## 📂 Dataset Used

- **Crop Recommendation Dataset** from [Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- It contains 2200+ rows with the following features:
  - `N`, `P`, `K`: Nutrient values
  - `temperature`: in °C
  - `humidity`: in %
  - `ph`: pH level of soil
  - `rainfall`: in mm
  - `label`: Recommended crop (target variable)

---

## 🧠 Machine Learning Models Applied

The following models were trained and compared:
- **Decision Tree Classifier**
- **Random Forest Classifier** ✅ (Best performing with ~93% accuracy)
- **K-Nearest Neighbors (KNN)**

Evaluation Metrics:
- Accuracy
- Confusion Matrix
- Classification Report

The **Random Forest** model was selected as the final model due to its robustness and high accuracy.

---

## 🔍 Project Workflow

### Step 1: Data Loading & Preprocessing
- Load the dataset using pandas
- Check for missing values and class balance
- Perform feature scaling with `StandardScaler`

### Step 2: Model Training
- Train ML models using training data
- Evaluate each model on the test set
- Perform hyperparameter tuning using `GridSearchCV`

### Step 3: Save Final Model
- Save the best model (Random Forest) using `joblib`
- Save the fitted scaler as well

### Step 4: Deploy Using Streamlit
- Build a UI using Streamlit for users to input values
- Load model + scaler and display predictions
- Use sliders and number inputs for a user-friendly experience

---

## ▶️ How to Run This Project

### ⚙️ Step 1: Install Dependencies
```bash
pip install -r requirements.txt

##⚙️ Step 2: Run Streamlit app
```bash
streamlit run crop_app.py

