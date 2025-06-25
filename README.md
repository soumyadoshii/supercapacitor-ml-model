# supercapacitor-ml-model
# Data-Driven Prediction of Electrochemical Properties of Supercapacitor Materials Using Machine Learning

This repository contains the code and dataset for a machine learning project that predicts electrochemical performance metrics of supercapacitor electrode materials, specifically Transition Metal Oxides (TMOs) and carbon-based materials.

🔬 **Objective:**
Leverage machine learning to accelerate the discovery of high-performance supercapacitor materials by predicting:
- Specific Capacitance (F/g)
- Energy Density (Wh/kg)
- Power Density (W/kg)

📁 **What's in this repo:**
- `Supercapacitor_ML_Model.ipynb`: The main Colab notebook containing the end-to-end ML workflow
- Preprocessing steps for handling missing data, unit standardization, and synthetic data generation
- Model building using Random Forest Regressors with MultiOutputRegressor
- Evaluation using R² Score, MAE, and RMSE

📊 **Key Features:**
- Multi-output regression models tailored for TMOs and carbon-based materials
- Feature inputs include Specific Surface Area, Pore Size, Voltage Window, Conductivity, and Particle Size
- Achieved ~85% prediction accuracy

📚 **Data Sources:**
- Peer-reviewed research articles
- Open-access scientific databases
- Synthetic augmentation for improved feature representation

🔗 **Open in Colab:**  
[Click here to run the notebook in Colab](https://colab.research.google.com/github/YourUsername/YourRepoName/blob/main/Supercapacitor_ML_Model.ipynb)

✍️ This work was done as part of a Summer Research Internship under the guidance of **Dr. Arti Hadap**. 

---

Feel free to explore, fork, or contribute!

