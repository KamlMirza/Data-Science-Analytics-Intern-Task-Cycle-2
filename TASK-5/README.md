<img width="1866" height="806" alt="Screenshot 2026-02-28 204235" src="https://github.com/user-attachments/assets/90031cc9-6ba0-4be6-8df4-16a544e8575e" /># Project: Global Superstore Interactive Business Dashboard  

## 1. Task Objective  

The primary objective of this task was to build a **Business Intelligence (BI) Dashboard** that allows stakeholders to monitor and analyze the performance of a Global Superstore. Key goals included:

- **Data Refinement:** Cleaning raw dataset inconsistencies to ensure accurate reporting.  
- **Real-time Interactivity:** Enabling users to filter data by Region, Category, and Sub-Category.  
- **KPI Visualization:** Providing a high-level overview of Sales, Profits, and Customer performance through visual storytelling.  

## 2. Technical Approach  

The development process was divided into three distinct phases:

### Phase I: Data Pre-processing (`datasetclear.py`)  

Before visualization, the raw `superstore.csv` underwent a rigorous cleaning pipeline:

- **Handling Missing Values:** Rows missing critical data like `Sales`, `Profit`, or `Customer Name` were removed to maintain data integrity.  
- **Data Type Standardization:** Converted `Order Date` from strings to datetime objects and ensured `Sales` and `Profit` were numeric for calculation.  
- **Schema Optimization:** Replaced periods in column names with underscores (e.g., `Order.Date` to `Order_Date`) to ensure compatibility with Python attribute referencing.  
- **Deduplication:** Removed redundant entries to prevent the inflation of sales figures.  

### Phase II: Dashboard Development (`app1.py`)  

The dashboard was built using **Streamlit** for the frontend and **Plotly Express** for the visualizations:

- **State Management:** Utilized `@st.cache_data` to load the cleaned CSV efficiently, ensuring the dashboard remains responsive even with large datasets.  
- **Dynamic Filtering:** Implemented a sidebar with multi-select widgets. The "Sub-Category" filter is context-aware, updating its options based on the selected "Category."  
- **Responsive Layout:** Used `st.columns` to create a grid layout for Key Performance Indicators (KPIs) and charts.  

### Phase III: Visual Construction  

- **KPI Cards:** Displayed Total Sales, Total Profit, and Total Orders. A dynamic logic was applied to the Profit card to change color (Green for profit, Red for loss).  
- **Horizontal Bar Chart:** Visualized the "Top 5 Customers" to identify high-value clients.  
- **Donut Chart:** Illustrated "Profit by Category" to show which business segments contribute most to the bottom line.  

## 3. Dashboard Preview  
<img width="1866" height="806" alt="Screenshot 2026-02-28 204235" src="https://github.com/user-attachments/assets/4b0373eb-f458-4edf-9a0b-b7089a9a45c8" />












## 4. Results and Insights  

### Key Performance Indicators (Overall)

| Metric | Value |
|--------|--------|
| **Total Sales** | **$12,642,905.00** |
| **Total Profit** | **$1,467,457.29** |
| **Total Orders** | **51,290** |

### Data Insights  

- **Top Performer:** **Technology** is the most profitable category, accounting for **45.2%** of total profits, followed by Office Supplies at 35.3%.  
- **Customer Excellence:** **Tom Ashbrook** is identified as the highest-grossing customer, contributing significantly to the $40k+ sales bracket.  
- **Regional Flexibility:** The dashboard allows for granular "deep-dives" into the West, East, South, and Central regions, helping managers identify underperforming territories instantly.  
