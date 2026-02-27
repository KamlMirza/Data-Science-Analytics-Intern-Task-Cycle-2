# Task 4: Loan Default Risk with Business Cost Optimization

## Objective
The primary objective of this task is to build a robust binary classification model to identify high-risk loan applicants and determine the optimal probability threshold that minimizes the total business cost to the lending institution.

## Approach

### 1. Data Cleaning and Preprocessing
* **Missing Value Handling:** Columns with more than 50% missing data were removed to reduce noise.
* **Numerical Imputation:** Missing numerical values were filled using the **median** strategy to maintain data distribution integrity.
* **Categorical Imputation:** Categorical missing values were filled with a constant 'Unknown' value.
* **Encoding:** Applied **Label Encoding** for binary categorical features and **One-Hot Encoding** for multi-category features to ensure compatibility with numerical algorithms.

### 2. Exploratory Data Analysis (EDA)
* Analyzed the target variable distribution, revealing a significant class imbalance (approx. 92% repaid vs. 8% defaulted).
* Identified key risk drivers through correlation analysis, noting that `EXT_SOURCE` scores and applicant age (`DAYS_BIRTH`) were the strongest predictors of default.

### 3. Model Building
* **Algorithm:** Utilized **Logistic Regression** due to its interpretability and ability to output probability scores necessary for threshold tuning.
* **Class Weighting:** Implemented `class_weight='balanced'` to prevent the model from being biased toward the majority class (repaid loans).
* **Feature Scaling:** Standardized numerical features using `StandardScaler` to ensure the model converges efficiently.

### 4. Business Cost Optimization
* Defined a **Cost Function** where a **False Negative** (failing to catch a default) is 20 times more expensive than a **False Positive** (wrongly flagging a good client).
* Iterated through 100 different probability thresholds to find the "Financial Sweet Spot" that minimizes total losses.

## Results and Insights

### Model Performance
* **ROC AUC Score:** **0.7377**, indicating a strong ability to distinguish between defaulters and non-defaulters.
* **Optimal Threshold:** Found to be **0.38**.

### Business Insights
1. **Cost-Benefit Trade-off:** Using a standard 0.5 threshold is financially inefficient in banking. By lowering the threshold to **0.38**, the bank can identify more potential defaults early, saving significantly on lost principal.
2. **Risk Drivers:** Applicants with lower `EXT_SOURCE_3` scores and younger age profiles generally presented a higher risk of default.
3. **Financial Impact:** The cost-based evaluation allowed us to quantify risk in dollars, moving beyond simple accuracy to provide a metric that is directly actionable for bank stakeholders.
