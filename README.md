# bank-marketing-prediction
Predicting Bank Marketing Campaign Outcomes Using Classification and Regression Models".





# Bank Marketing Prediction

This project involves predicting the outcomes of bank marketing campaigns using various classification and regression models. The dataset contains information about phone calls made by a Portuguese bank to market term deposits. The goal is to determine whether a client will subscribe to the product based on various features.

## Project Structure

- **`Regression_Final.ipynb`**: The main Jupyter notebook containing the entire workflow, including data preprocessing, feature engineering, model training, and evaluation.
  
## Models Used

1. **Logistic Regression**: For binary classification of subscription outcomes.
2. **Random Forest Classifier**: To predict whether a client will subscribe based on categorical and numerical features.
3. **Support Vector Classifier (SVC)**: Used with a tuned parameter grid for optimal classification performance.
4. **Support Vector Regression (SVR)**: Applied to predict continuous target variables (regression task).
5. **Decision Tree Regression**: Simple model for regression tasks with decision trees.
6. **Random Forest Regression**: Ensemble method for continuous predictions.

## Feature Engineering and Preprocessing

- Categorical features were one-hot encoded.
- Numerical features were scaled where needed (e.g., for SVC and Logistic Regression).
- Feature selection was applied for regression tasks to pick the most relevant variables.
![Scaled_Features](https://github.com/user-attachments/assets/4dab10ac-7562-4037-b2a2-ca7e2625b27e)

## Results and Evaluation

- Models were evaluated based on metrics such as **accuracy**, **precision**, **recall**, **F1 score** for classification, and **MSE**, **R²** for regression.
- The best performance was achieved by the **Random Forest Classifier** in classification and the **Random Forest Regressor** in regression tasks.

## Dataset

The dataset used for this project is related to direct marketing campaigns of a Portuguese banking institution. It can be found at the Kaggle website :*https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing*
### Features Used

1. **age**: Age of the client (numeric).
2. **job**: Type of job (categorical).
3. **marital**: Marital status (categorical).
4. **education**: Level of education (categorical).
5. **default**: Whether the client has credit in default (categorical).
6. **housing**: Whether the client has a housing loan (categorical).
7. **loan**: Whether the client has a personal loan (categorical).
8. **contact**: Contact communication type (categorical).
9. **month**: Month of the last contact (categorical).
10. **day_of_week**: Day of the week of the last contact (categorical).
11. **duration**: Duration of the last contact (numeric).
12. **campaign**: Number of contacts during this campaign (numeric).
13. **pdays**: Days since last contact (numeric).
14. **previous**: Number of contacts before this campaign (numeric).
15. **poutcome**: Outcome of the previous campaign (categorical).
16. **emp.var.rate**: Employment variation rate (numeric).
17. **cons.price.idx**: Consumer price index (numeric).
18. **cons.conf.idx**: Consumer confidence index (numeric).
19. **euribor3m**: Euribor 3-month rate (numeric).
20. **nr.employed**: Number of employees (numeric).

## Installation and Running

