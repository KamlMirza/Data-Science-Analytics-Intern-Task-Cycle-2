import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Global Superstore Analytics Dashboard",
    layout="wide"
)

# 2. Loading Pre-Cleaned Data (with caching for performance)
@st.cache_data
def load_data():
    # Automatically find the folder this script is saved in
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Point to the pre-cleaned dataset you just generated
    csv_file_path = os.path.join(script_dir, 'cleaned_superstore.csv') 
    
    # Read the local CSV
    df = pd.read_csv(csv_file_path, encoding='latin-1')
    
    # Convert Order_Date back to datetime (CSVs save dates as text)
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Navigation & Filters")
st.sidebar.markdown("Filter the data to update the dashboard.")

region = st.sidebar.multiselect(
    "Select Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

sub_category = st.sidebar.multiselect(
    "Select Sub-Category:",
    options=df[df["Category"].isin(category)]["Sub_Category"].unique() if category else df["Sub_Category"].unique(),
    default=None
)

df_selection = df[df["Region"].isin(region) & df["Category"].isin(category)]
if sub_category:
    df_selection = df_selection[df_selection["Sub_Category"].isin(sub_category)]

# 4. Main Dashboard Header
st.title("Global Superstore Business Dashboard")
st.markdown("Analyzing Sales, Profits, and Customer Performance")
st.markdown("---")

# 5. KPI Cards Layout
col1, col2, col3 = st.columns(3)

total_sales = df_selection["Sales"].sum()
total_profit = df_selection["Profit"].sum()
total_orders = df_selection.shape[0]

with col1:
    st.subheader("Total Sales")
    st.title(f"${total_sales:,.2f}")

with col2:
    st.subheader("Total Profit")
    profit_color = "green" if total_profit > 0 else "red"
    st.markdown(f"<h1 style='color: {profit_color};'>${total_profit:,.2f}</h1>", unsafe_allow_html=True)

with col3:
    st.subheader("Total Orders")
    st.title(f"{total_orders:,}")

st.markdown("---")

# 6. Visualizations
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Top 5 Customers by Sales")
    top_customers = (
        df_selection.groupby("Customer_Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )
    
    fig_customers = px.bar(
        top_customers,
        x="Sales",
        y="Customer_Name",
        orientation="h",
        color="Sales",
        color_continuous_scale="Blues",
        template="plotly_white"
    )
    fig_customers.update_layout(yaxis={'categoryorder':'total ascending'}, plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_customers, use_container_width=True)

with right_column:
    st.subheader("Profit by Category")
    fig_category = px.pie(
        df_selection, 
        values='Profit', 
        names='Category', 
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig_category, use_container_width=True)

# 7. Data Table Section
with st.expander("View Filtered Data Table"):
    st.dataframe(df_selection.sort_values(by="Order_Date", ascending=False))

st.markdown("---")
st.caption("Developed for Developers Hub Corporation - Data Science Internship")