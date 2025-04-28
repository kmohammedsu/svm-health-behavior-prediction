# Diabetes Prediction with Support Vector Machines (SVM)

## Overview

This project explores the use of Support Vector Machines (SVM) with linear, polynomial, and radial (RBF) kernels to predict diabetes status using demographic and lifestyle variables from the National Health Interview Survey (NHIS, via IPUMS). The objective is to evaluate how health behaviors and demographic factors relate to diabetes risk, and to compare the predictive performance and clinical utility of different SVM kernels.

---

## Technical Background

### What is an SVM?
Support Vector Machines (SVMs) are supervised machine learning models used for classification and regression. SVMs find the optimal hyperplane that separates classes by maximizing the margin between support vectors (the closest points from each class). SVMs can handle both linear and non-linear classification tasks.

### SVM Kernels
- **Linear Kernel:** Finds a straight-line (or hyperplane) separation. Best for linearly separable data and offers high interpretability.
- **Polynomial Kernel:** Projects data into a higher-dimensional space using polynomial functions, allowing for curved decision boundaries. The degree of the polynomial controls the boundary’s flexibility.
- **Radial Basis Function (RBF) Kernel:** Maps data into an infinite-dimensional space using a Gaussian function. RBF is highly flexible and can model complex, non-linear relationships.

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

## Conclusions

- **Linear SVM** is the best choice for diabetes screening in this dataset, as it maximizes recall and minimizes missed cases, despite more false positives.
- **Polynomial and RBF SVMs** offer higher accuracy and fewer false positives, but at the cost of missing most diabetes cases-a critical issue for screening.
- **Clinical Implication:** For public health screening, sensitivity (recall) is more important than overall accuracy or precision. The linear kernel is preferable for this application.

---

## How to Run

1. Clone the repository and install dependencies (see `requirements.txt`).
2. Place the cleaned NHIS data CSV in the `data/` directory.
3. Run the Jupyter notebooks in order:
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

## Future Work

- Explore additional health outcomes (cancer, heart disease, stroke, etc.)
- Incorporate more behavioral and socioeconomic variables


