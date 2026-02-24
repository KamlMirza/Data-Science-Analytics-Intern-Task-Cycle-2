# Project: Term Deposit Subscription Prediction
This project focuses on predicting customer behavior in response to bank marketing campaigns using Machine Learning and Explainable AI.

## Task Objective
The primary goal of this project is to develop a classification model that predicts whether a customer will **subscribe to a term deposit** based on their demographic profile and past interaction history.
By accurately identifying potential subscribers, the bank can:
- Optimize marketing strategies  
- Improve campaign conversion rates  
- Reduce operational costs  
- Target high-value customers more effectively  

## Approach
The project followed a structured data science workflow, moving from raw data to interpretable business insights.
 
### Exploratory Data Analysis (EDA)
- Checked for missing values (none found)  
- Analyzed the distribution of the target variable  
- Identified significant class imbalance between "no" and "yes" responses  
- Visualized relationships between categorical features (e.g., job title) and subscription rates  
- Explored patterns across economic indicators and campaign-related variables  

### Data Preprocessing
- Converted the target variable to numerical format using Label Encoding  
- Applied One-Hot Encoding to categorical features to avoid artificial hierarchy assumptions  
- Split the dataset into training and testing sets  
- Applied StandardScaler (Feature Scaling) for Logistic Regression  

### Model Building
- Trained a Logistic Regression model as a baseline classifier  
- Trained a Random Forest Classifier to improve predictive performance and handle non-linear relationships  

### Explainable AI (XAI)
- Implemented SHAP (SHapley Additive Explanations) for model interpretability  
- Generated global feature importance summary plots  
- Generated individual waterfall plots for specific customer predictions  
- Identified the most influential features driving subscription outcomes  

### Model Performance
The Random Forest model demonstrated strong predictive capability:
- Overall Accuracy: 91%  
- ROC AUC: 0.95 (indicating high discriminative power)  
- Confusion Matrix Results:
  - 7,088 correctly predicted non-subscribers  
  - 452 correctly predicted subscribers  

## Conclusion and Insights
Based on the analysis and the SHAP values:
- **Duration:** The length of the last phone call is the most significant predictor. However, this information is only available after the call, making it less useful for predictive targeting before a campaign begins.  
- **Economic Indicators:** Variables such as `euribor3m` (Euro Interbank Offered Rate) and `nr.employed` significantly impact the likelihood of subscription.  
- **Recommendation:** The bank should prioritize customers who have been contacted fewer times in previous campaigns to reduce the risk of marketing fatigue and improve campaign effectiveness.
