# Project:Energy Consumption Time Series Forecasting

## Objective
The primary goal of this project is to forecast short-term household energy usage by analyzing historical time-based patterns. Accurate energy forecasting is critical for improving grid management and developing effective energy-saving strategies for individual households.

## Approach
The project utilizes the **Individual Household Electric Power Consumption** dataset, which captures electricity metrics at a 1-minute sampling rate. The following steps were taken to build the predictive models:

### 1. Data Preprocessing & Cleaning
- **Data Integration**: Combined separate 'Date' and 'Time' columns into a single `Datetime` index for time-series analysis.  
- **Handling Missing Values**: Identified missing data (represented as '?') and applied **linear interpolation** to ensure a continuous dataset.  
- **Resampling**: To reduce computational load and minimize high-frequency noise, the data was resampled from 1-minute intervals to a **Daily frequency** (`Global_active_power` mean).  

### 2. Exploratory Data Analysis (EDA)
- Visualized daily and monthly consumption trends to identify patterns.  
- Observed significant daily and monthly fluctuations, with clear seasonal peaks likely tied to weather changes.  

### 3. Feature Engineering
For the machine learning component, specific temporal features were extracted from the datetime index to capture human behavioral patterns:
- **Time Components**: Day, month, and year.  
- **Behavioral Indicators**: Day of the week and an `is_weekend` flag (identifying Saturdays and Sundays).  

### 4. Model Selection
The performance of three distinct forecasting approaches was compared:
- **ARIMA**: A traditional auto-regressive statistical model.  
- **Exponential Smoothing**: Used as a statistical baseline proxy for seasonal patterns.  
- **Gradient Boosting Regressor**: A machine learning approach used to leverage engineered categorical features.  

## Results and Insights

### Model Performance Comparison
Models were evaluated using **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)** based on an 80/20 train-test split.
| Model | MAE | RMSE |
| --- | --- | --- |
| **Gradient Boosting** | **0.310461** | **0.397086** |
| ARIMA | 0.430105 | 0.519172 |
| Exponential Smoothing | 0.454125 | 0.537092 |

### Key Insights
- **Superiority of ML**: The **Gradient Boosting** model outperformed traditional statistical models. This is attributed to its ability to effectively utilize engineered features like weekends vs. weekdays, which directly correlate with household energy behavior.  
- **Resampling Benefits**: Resampling high-frequency, noisy 1-minute data to daily averages provides a much clearer signal for short-term forecasting.  
- **Human Behavior**: Machine learning models that incorporate categorical time features capture human patterns (e.g., higher usage on weekends) more accurately than pure auto-regressive models.  
- **Future Work**: Accuracy could be further improved by integrating external variables such as temperature, humidity, or local weather data.  

# Author & Contact

**Kaml Mirza**  
LinkedIn: www.linkedin.com/in/kaml-mirza-38223034a
