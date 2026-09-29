# **📊 Employee Attrition Analysis & Prediction**

An end-to-end Employee Attrition Analysis and Machine Learning project that explores the factors associated with employee turnover and uses a Random Forest classification model to predict whether an employee is likely to leave the organization.

The project combines Exploratory Data Analysis (EDA), data visualization, machine learning, and an interactive Streamlit application to turn HR data into actionable insights.

# **🚀 Project Overview**

Employee attrition can have a significant impact on organizations through recruitment costs, loss of experienced employees, productivity disruption, and additional training requirements.

This project analyzes employee data to:

- Understand patterns in employee attrition

- Explore factors associated with employees leaving an organization

- Visualize important HR metrics and relationships

- Build a machine learning model for attrition prediction

- Provide an interactive interface for making predictions

The analysis is based on an HR Employee Attrition dataset containing demographic, professional, compensation, satisfaction, and work-related information.

# **🎯 Objectives**

The main objectives of this project are:

- Perform exploratory data analysis on employee HR data.

- Identify patterns and relationships associated with employee attrition.

- Prepare and transform the data for machine learning.

- Train a Random Forest classification model.

- Save the trained model for later predictions.

- Build an interactive Streamlit application.

- Provide a simple interface for predicting employee attrition.

# **🛠️ Technologies Used**

- **Python**

- **Pandas** – Data manipulation and analysis

- **NumPy** – Numerical computing

- **Matplotlib** – Data visualization

- **Seaborn** – Statistical visualization

- **Scikit-learn** – Machine learning

- **Jupyter Notebook** – Data analysis and experimentation

- **Streamlit** – Interactive web application

- **Pickle** – Model and feature serialization

- **Power BI** - Data visualization and interactive HR dashboard

# **📁 Project Structure**

```text
employee-attrition/
│
├── Attrition.ipynb
│   └── Exploratory data analysis and machine learning workflow
│
├── HR-Employee-Attrition.csv
│   └── Employee HR dataset
│
├── app.py
│   └── Streamlit application for attrition prediction
│
├── random_forest_model.pkl
│   └── Trained Random Forest classification model
│
├── feature_names.pkl
│   └── Feature names used by the trained model
│
├── Attrition Dashboard.pdf
│   └── Power BI attrition analysis dashboard
│
├── Attrition Dashboard Screenshot.png
│   └── Dashboard preview
│
└── README.md
    └── Project documentation
```

# **🔍 Exploratory Data Analysis**

The project performs exploratory analysis to understand employee characteristics and their relationship with attrition.

The analysis covers areas such as:

- Employee demographics

- Department and job role

- Monthly income

- Job satisfaction

- Work-life balance

- Overtime

- Business travel

- Years at the company

- Years in current role

- Job level

- Distance from home

Visualizations are used to make patterns and relationships in the data easier to understand.

# **🤖 Machine Learning**

A Random Forest Classifier is used to predict employee attrition.

The general machine learning workflow includes:

```
Raw HR Data
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Preparation
     ↓
Train/Test Split
     ↓
Random Forest Model
     ↓
Model Evaluation
     ↓
Model Serialization
     ↓
Streamlit Prediction App

```


The trained model is stored in:
```
random_forest_model.pkl
```

The corresponding feature names are stored in:
```
feature_names.pkl
```

This allows the trained model to be reused by the Streamlit application without retraining every time the application starts.

# **🌐 Streamlit Application**

The project includes an interactive Streamlit application located in:
```
app.py
```

The application provides a user-friendly interface where employee information can be entered and the trained machine learning model can be used to generate an attrition prediction.

Run the application

First, clone the repository:
```
git clone https://github.com/m4h3k/employee-attrition.git
cd employee-attrition
```

Create a virtual environment:
```
python -m venv venv
```

Activate it on Windows:
```
venv\Scripts\activate
```

Or on macOS/Linux:
```
source venv/bin/activate
```

Install the required libraries:
```
pip install pandas numpy matplotlib seaborn scikit-learn streamlit jupyter
```

Run the Streamlit application:
```
streamlit run app.py
```

The application will open in your browser.

# **📓 Jupyter Notebook**

The complete analysis and modeling workflow is available in:
```
Attrition.ipynb
```

The notebook can be opened using Jupyter:
```
jupyter notebook
```

Then open:
```
Attrition.ipynb
```
# **📊 Dashboard**

The project also contains an employee attrition dashboard created using Microsoft Power BI:
```
Attrition Dashboard.pdf
```

A screenshot of the dashboard is provided in:
```
Attrition Dashboard Screenshot.png
```

The Power BI dashboard provides a visual overview of employee attrition and relevant HR metrics.

# **💡 Key Takeaways**

This project demonstrates how HR data can be combined with machine learning to investigate employee attrition.

The analysis focuses on factors such as:

- Compensation

- Job satisfaction

- Work-life balance

- Overtime

- Job role

- Career progression

- Work experience

- Business travel

- Demographic characteristics

These variables can be explored to understand patterns within the dataset and develop predictive models for employee attrition.

# **🔮 Future Improvements**

Potential improvements to the project include:

- Compare Random Forest with K-Nearest Neighbors (KNN), XGBoost and other classifiers

- Add cross-validation and systematic hyperparameter tuning

- Add feature importance visualizations

- Deploy the Streamlit application online

- Add automated data preprocessing pipelines

- Improve the dashboard with additional interactive filters

# **📚 Dataset**

The project uses an HR Employee Attrition dataset containing employee-level information such as demographics, job characteristics, compensation, satisfaction, and attrition status.

The dataset is included in the repository as:
```
HR-Employee-Attrition.csv
```
# **⚠️ Disclaimer**

This project is intended for educational and analytical purposes. Predictions generated by the model should not be used as the sole basis for employment-related decisions. Model outputs can reflect limitations or biases present in the underlying historical dataset.


## 👤 Author

**m4h3k**

[GitHub Repository](https://github.com/m4h3k/employee-attrition)


**⭐ Support**

If you find this project useful, consider giving the repository a ⭐ on GitHub.
