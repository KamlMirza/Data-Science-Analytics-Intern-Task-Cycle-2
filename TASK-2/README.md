# Project: Mall Customer Segmentation

## Project Objective
The main goal of this project is to analyze mall customer data to identify distinct customer groups based on their annual income and spending patterns. By applying unsupervised learning techniques, mall management can gain deeper insights into customer behavior.
These insights help in:
- Understanding customer purchasing patterns  
- Identifying high-value and low-value segments  
- Designing targeted marketing strategies  
- Improving overall customer engagement and profitability  

## Approach
To achieve meaningful customer segmentation, the project followed a structured data science workflow:

### 1. Exploratory Data Analysis (EDA)
- Visualized distributions of Age, Annual Income, and Spending Score  
- Identified patterns, trends, and possible clustering behavior  
- Examined relationships between income and spending  

### 2. Data Preprocessing
- Checked for missing values (none were found)  
- Selected relevant features:
  - `Annual Income (k$)`  
  - `Spending Score (1-100)`  
- Removed unnecessary columns to focus on clustering variables  

### 3. Feature Scaling
- Applied `StandardScaler` to normalize the data  
- Ensured both income and spending score were treated equally by the algorithm  
- Prevented bias caused by differences in feature magnitude  

### 4. Determining Optimal Number of Clusters
- Used the Elbow Method  
- Plotted Within-Cluster Sum of Squares (WCSS) against different values of k  
- Determined the optimal number of clusters to be **5**  

### 5. Model Building
- Implemented the K-Means clustering algorithm  
- Used `k-means++` initialization for better centroid placement  
- Trained the model with **k = 5**  

### 6. Dimensionality Reduction
- Applied Principal Component Analysis (PCA)  
- Reduced data to two components (PCA1 and PCA2)  
- Enabled clear 2D visualization of customer segments  

## Results and Insights
The K-Means clustering model successfully segmented customers into five distinct groups:

### 1. Stars (Cluster 1)
- High annual income  
- High spending score  
- Premium and high-value customers  

### 2. Target Customers (Cluster 3)
- High income  
- Low spending behavior  
- Potential high-value customers with untapped spending capacity  

### 3. Impulsive Customers (Cluster 2)
- Lower income  
- High spending score  
- Emotion-driven or trend-driven buyers  

### 4. Frugal Customers (Cluster 4)
- Low income  
- Low spending  
- Budget-conscious shoppers  

### 5. Average Customers (Cluster 0)
- Moderate income  
- Moderate spending  
- Largest and most balanced customer segment  

## Marketing Strategies
Based on the identified segments, the following strategies are recommended:

### For Stars
- Introduce premium loyalty programs  
- Launch exclusive luxury products  
- Offer personalized concierge services  

### For Target Customers
- Provide personalized discounts on premium products  
- Offer high-value bundle deals  
- Encourage higher spending through limited-time offers  

### For Impulsive Customers
- Promote flash sales  
- Use trendy social media campaigns  
- Offer "buy now, pay later" incentives  

### For Frugal Customers
- Advertise budget-friendly value packs  
- Highlight seasonal clearance sales  
- Provide basic rewards programs  

### For Average Customers
- Maintain engagement through holiday newsletters  
- Offer moderate promotions  
- Implement cross-category marketing strategies  
