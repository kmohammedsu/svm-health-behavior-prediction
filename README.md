# Diabetes Prediction with Support Vector Machines (SVM)

## Overview

This project explores the use of Support Vector Machines (SVM) with linear, polynomial, and radial (RBF) kernels to predict diabetes status using demographic and lifestyle variables from the National Health Interview Survey (NHIS, via IPUMS). The objective is to evaluate how health behaviors and demographic factors relate to diabetes risk, and to compare the predictive performance and clinical utility of different SVM kernels.

---
## Project Question

Can we accurately predict the presence of diabetes in adults using demographic and lifestyle variables from the NHIS, and how do different SVM kernel choices (linear, polynomial, radial) affect prediction performance and clinical utility?

---
## Data

- **Source:** [IPUMS Health Surveys: National Health Interview Survey](https://doi.org/10.18128/D070.V7.4)
- **Variables Used:**
  - Demographics: Age, BMI (BMICALC)
  - Behaviors: Sleep hours (HRSLEEP), Cigarettes per month (CIGDAYMO)
  - Engineered features: BMI × Age interaction
  - **Target:** Doctor-diagnosed diabetes (`DIABETICEV`)

---

## Technical Background

### What is an SVM?
Support Vector Machines (SVMs) are supervised machine learning models used for classification and regression. SVMs find the optimal hyperplane that separates classes by maximizing the margin between support vectors (the closest points from each class). SVMs can handle both linear and non-linear classification tasks.

### SVM Kernels
- **Linear Kernel:** Finds a straight-line (or hyperplane) separation. Best for linearly separable data and offers high interpretability.
- **Polynomial Kernel:** Projects data into a higher-dimensional space using polynomial functions, allowing for curved decision boundaries. The degree of the polynomial controls the boundary’s flexibility.
- **Radial Basis Function (RBF) Kernel:** Maps data into an infinite-dimensional space using a Gaussian function. RBF is highly flexible and can model complex, non-linear relationships.

---



## Methods

- **Preprocessing:**  
  - Cleaned missing values
  - Standardized features
  - Addressed class imbalance using SMOTE
  - Feature engineering (BMI × Age interaction)

- **Modeling:**  
  - Implemented SVM classifiers with linear, polynomial, and RBF kernels
  - Hyperparameter tuning via grid search and cross-validation for each kernel
  - Evaluation metrics: accuracy, recall, precision, F1-score, AUC, confusion matrices
  - Threshold sweep analysis to explore recall/precision tradeoffs

---

## Results

| Metric                | Linear SVM | Poly SVM (deg=5) | RBF SVM |
|-----------------------|------------|------------------|---------|
| Accuracy              | 65%        | 80%              | 84%     |
| Recall (diabetes)     | 78%        | 28%              | 33%     |
| Precision (diabetes)  | 18%        | 16%              | 24%     |
| AUC                   | 0.77       | 0.65             | 0.65    |
| False Negatives       | 4          | 13               | 12      |

- **Linear SVM:** Highest recall for diabetes (78%), making it best for screening, but with many false positives.
- **Polynomial SVM:** Higher accuracy but much lower recall for diabetes.
- **RBF SVM:** Highest overall accuracy and fewest false positives, but recall for diabetes remains low (33%).

**Key Visualizations:**  
- Confusion matrices for each kernel
- ROC curves and AUC scores
- Threshold sweep plots (precision/recall tradeoff)
- Decision boundary plots (BMI vs. Age)

---
### Interpretation: Impact of Habits, Metrics, and Demographics

### Which habits and metrics impact diabetes risk?
- **BMI × Age interaction** is the most influential predictor in all SVM models. This means older adults with higher BMI are at significantly greater risk for diabetes-a finding that matches clinical knowledge and public health research. 
- **BMI alone** is also a strong predictor, confirming that obesity is a major modifiable risk factor.
- **Smoking (CIGDAYMO)** and **Sleep (HRSLEEP)** had lower importance in this dataset. This may be due to limited detail in the NHIS survey (e.g., no pack-years or sleep quality), or because their effects on diabetes are partly mediated through BMI.

### Why do demographic and social factors make sense as predictors?
- **Age** is a critical non-modifiable risk factor. The strong interaction with BMI in your model reflects how metabolic risk increases with age.
- **Social determinants of health (SDOH)** such as income, education, and neighborhood environment are not included in this analysis but are known from the literature to significantly affect diabetes risk. Including such variables in future models could improve prediction and help address health disparities.

### Policy and Public Health Implications
- **Targeted screening:** The results support prioritizing BMI and age-based diabetes screening, especially for adults over 40.
- **Resource allocation:** Linear SVM’s high recall (78%) means it can help flag high-risk individuals for further testing, making it a useful tool in public health clinics.
- **Data modernization:** For even better prediction, future surveys should collect more detailed behavioral and social data (e.g., food access, sleep quality, smoking duration).

### Study Impact
- This project demonstrates that simple, interpretable models using basic survey data can effectively identify high-risk groups for diabetes.
- The approach can be adapted to other chronic diseases and can inform policy and prevention strategies at the community level.

### Conclusions

- **Linear SVM** is preferred for diabetes screening due to its **high recall (78%)**, minimizing missed cases.

- **BMI × Age interaction** is the most important predictor, highlighting the need for **age-specific weight management policies**.

- For screening, **sensitivity (recall)** is more critical than precision or overall accuracy.

- **Policy suggestion**:  
  Implement targeted diabetes screening and prevention programs for **older adults with high BMI**, and support **data modernization** for more granular behavioral metrics.

- **Limitations**:  
  Limited feature set and potential for high false positives.  
  Future work should include **more variables** and explore **ensemble models**.
---
## Future Work

- Explore additional health outcomes (cancer, heart disease, stroke, etc.)
- Incorporate more behavioral and socioeconomic variables
---

## How to Run

1. Clone the repository and install dependencies (see `requirements.txt`).
2. Place the cleaned NHIS data CSV in the `data/` directory.
3. Run the Jupyter notebooks in order:
    - `01_eda.ipynb`
    - `02_linear_kernel.ipynb`
    - `03_polynomial_kernel.ipynb`
    - `04_radial_kernel.ipynb`
4. Review the outputs and visualizations in each notebook.

---

## Directory Structure
```
svm_health_behavior_prediction/
├── data/
│ ├── nhis_2022_cleaned.csv
│ ├── nhis_2022_codebook.pdf
│ ├── nhis_2022.csv
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_linear_kernel.ipynb
│ ├── 03_polynomial_kernel.ipynb
│ ├── 04_radial_kernel.ipynb
├── poster/
│ ├── poster.png
├── scripts/
│ ├── data_cleaning.py
├── README.md
├── .gitignore
└── requirements.txt
```
---




