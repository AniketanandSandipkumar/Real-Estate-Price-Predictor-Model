# 🏠 Real Estate Price Predictor

A machine learning-powered web application that predicts real estate property prices in India based on multiple features like area, location coordinates, BHK, dealer/owner, and readiness status. The model is trained using a Random Forest Regressor and deployed using Flask with a responsive front-end UI.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Dataset Description](#dataset-description)
- [ML Pipeline](#ml-pipeline)
- [App Features](#app-features)
- [Sample Input/Output](#sample-inputoutput)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Learnings](#learnings)
- [Contact](#contact)

---

## 🧠 Overview

This project aims to estimate house prices using various features such as square footage, number of bedrooms, longitude/latitude, and other factors like resale, RERA registration, and ownership type. It uses a Random Forest Regressor model trained on real-world data and is deployed as a Flask web application where users can input their property features and instantly get an estimated price.

---

## 🗂️ Dataset Description

- **train.csv**: Used to train the Random Forest regression model.
- **test.csv**: Used to validate the model.
- Features used include:
  - Under Construction (0/1)
  - RERA Registered (0/1)
  - BHK (Number of bedrooms)
  - Square Foot Area
  - Ready to Move (0/1)
  - Resale (0/1)
  - Longitude & Latitude
  - Dealer (0/1)
  - Owner (0/1)

---

## 🧪 ML Pipeline

1. **Data Preprocessing**: 
   - Checked for nulls
   - Converted categorical variables to binary
   - Standardized numerical inputs if required

2. **Model Selection**: 
   - Random Forest Regressor was selected due to its performance on non-linear tabular data.

3. **Model Training**: 
   - Trained on `train.csv` with 10 selected features.
   - Saved as `randomreg.pkl` using `pickle`.

4. **Deployment**: 
   - Flask is used to serve the model and HTML frontend.
   - Streamlined prediction route receives user inputs and returns price estimate.

---

## 💻 App Features

- Clean, minimal, and mobile-friendly web interface
- 10 feature input form
- Instant prediction with error handling
- Clear display of predicted price in INR Lacs
- Background image and custom UI for better UX

---

## 🔢 Sample Input/Output

| Feature             | Example Value |
|---------------------|---------------|
| Under Construction  | 1             |
| RERA                | 1             |
| BHK                 | 3             |
| Square Feet         | 1350          |
| Ready to Move       | 0             |
| Resale              | 1             |
| Longitude           | 77.5946       |
| Latitude            | 12.9716       |
| Dealer              | 1             |
| Owner               | 0             |

💡 **Predicted Price:** ₹ 85.42 Lacs

---

## 📁 Project Structure
<br>
Real-Estate-Price-Predictor/<br>
│
├── app.py # Flask backend<br>
├── randomreg.pkl # Trained ML model<br>
├── requirements.txt # Python dependencies<br>
├── Procfile # For deployment<br>
│
├── templates/<br>
│ └── index.html # Web interface<br>
│
├── static/<br>
│ └── background.jpg # Background image<br>
│
├── train.csv # Training dataset<br>
├── test.csv # Testing dataset<br>
└── housepredictor2.ipynb # Jupyter notebook (ML work)<br>


---

## 🚀 Future Enhancements

- Add location-based feature mapping using clustering or geospatial data
- Include visualizations and confidence intervals
- Host using Streamlit or Docker for scalability
- Add user authentication for saving prediction history

---

## 📘 Learnings

- Implemented an end-to-end ML pipeline
- Learned about model deployment using Flask
- Improved understanding of handling geospatial and binary features
- Gained experience in UI/UX integration with machine learning models

---

## 📫 Contact

**Aniketanand Sandipkumar**  
📧 Email: [aniketanand2712@gmail.com]  
🔗 GitHub: [github.com/AniketanandSandipkumar](https://github.com/AniketanandSandipkumar)<br>
[App link](https://real-estate-price-predictor-model.onrender.com/)
---

> Made with ❤️ using Python, Flask, and Machine Learning.
