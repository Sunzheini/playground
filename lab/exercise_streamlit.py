import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import time


# Page configuration
st.set_page_config(
    page_title="Advanced Streamlit Demo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and header
st.title("🚀 Advanced Streamlit Dashboard")
st.markdown("---")

# Sidebar
st.sidebar.header("Controls")
st.sidebar.markdown("Customize your dashboard using the controls below.")


# Data generation function
@st.cache_data
def generate_sample_data(n_points, noise_level):
    """Generate sample data for demonstration"""
    np.random.seed(42)  # For reproducible results
    dates = pd.date_range(start='2023-01-01', periods=n_points, freq='D')

    # Generate different types of data
    trend = np.linspace(10, 50, n_points)
    seasonal = 10 * np.sin(2 * np.pi * np.arange(n_points) / 365.25)
    noise = np.random.normal(0, noise_level, n_points)

    sales = trend + seasonal + noise + np.random.exponential(5, n_points)
    profit = sales * 0.2 + np.random.normal(0, 2, n_points)
    customers = np.random.poisson(sales * 2, n_points)

    return pd.DataFrame({
        'Date': dates,
        'Sales': np.maximum(sales, 0),  # Ensure non-negative
        'Profit': profit,
        'Customers': customers,
        'Region': np.random.choice(['North', 'South', 'East', 'West'], n_points),
        'Product': np.random.choice(['Product A', 'Product B', 'Product C'], n_points)
    })


# Sidebar controls
n_points = st.sidebar.slider("Number of data points", 50, 1000, 365)
noise_level = st.sidebar.slider("Noise level", 0.1, 5.0, 1.0)
selected_region = st.sidebar.multiselect(
    "Select regions",
    ['North', 'South', 'East', 'West'],
    default=['North', 'South', 'East', 'West']
)

# Date range picker
date_range = st.sidebar.date_input(
    "Select date range",
    value=(date(2023, 1, 1), date(2023, 12, 31)),
    min_value=date(2023, 1, 1),
    max_value=date(2023, 12, 31)
)

# Generate and filter data
df = generate_sample_data(n_points, noise_level)
if selected_region:
    df = df[df['Region'].isin(selected_region)]

if len(date_range) == 2:
    start_date, end_date = date_range
    df = df[(df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)]

# Main content area with columns
col1, col2, col3, col4 = st.columns(4)

# Key metrics
with col1:
    st.metric(
        label="Total Sales",
        value=f"${df['Sales'].sum():,.0f}",
        delta=f"{df['Sales'].tail(30).mean() - df['Sales'].head(30).mean():+,.0f}"
    )

with col2:
    st.metric(
        label="Avg Daily Profit",
        value=f"${df['Profit'].mean():,.0f}",
        delta=f"{df['Profit'].std():+,.0f}"
    )

with col3:
    st.metric(
        label="Total Customers",
        value=f"{df['Customers'].sum():,}",
        delta=f"{df['Customers'].tail(7).mean() - df['Customers'].head(7).mean():+,.0f}"
    )

with col4:
    st.metric(
        label="Profit Margin",
        value=f"{(df['Profit'].sum() / df['Sales'].sum() * 100):.1f}%",
        delta="2.3%"
    )

st.markdown("---")

# Chart section with tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Time Series", "📊 Distribution", "🗺️ Regional Analysis", "🔍 Data Explorer"])

with tab1:
    st.subheader("Sales and Profit Trends Over Time")

    # Plotly time series chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Sales'], name='Sales', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Profit'], name='Profit', yaxis='y2', line=dict(color='green')))

    fig.update_layout(
        title='Sales vs Profit Over Time',
        xaxis_title='Date',
        yaxis=dict(title='Sales ($)', side='left'),
        yaxis2=dict(title='Profit ($)', side='right', overlaying='y'),
        hovermode='x unified',
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    # Native streamlit charts for comparison
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sales Line Chart (Native)")
        st.line_chart(df.set_index('Date')['Sales'])

    with col2:
        st.subheader("Customer Bar Chart (Native)")
        st.bar_chart(df.groupby('Region')['Customers'].sum())

with tab2:
    st.subheader("Data Distributions")

    col1, col2 = st.columns(2)

    with col1:
        # Histogram with matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(df['Sales'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
        ax.set_title('Sales Distribution')
        ax.set_xlabel('Sales ($)')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

    with col2:
        # Box plot with plotly
        fig = px.box(df, x='Region', y='Profit', title='Profit by Region')
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Regional Performance Analysis")

    # Regional summary
    regional_summary = df.groupby('Region').agg({
        'Sales': ['sum', 'mean'],
        'Profit': ['sum', 'mean'],
        'Customers': 'sum'
    }).round(2)

    st.dataframe(regional_summary, use_container_width=True)

    # Pie chart for sales by region
    region_sales = df.groupby('Region')['Sales'].sum()
    fig = px.pie(values=region_sales.values, names=region_sales.index,
                 title='Sales Distribution by Region')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Data Explorer")

    # Interactive filtering
    col1, col2 = st.columns(2)
    with col1:
        product_filter = st.selectbox("Filter by Product", ['All'] + list(df['Product'].unique()))
    with col2:
        min_sales = st.number_input("Minimum Sales", value=float(df['Sales'].min()),
                                    max_value=float(df['Sales'].max()))

    # Apply filters
    filtered_df = df.copy()
    if product_filter != 'All':
        filtered_df = filtered_df[filtered_df['Product'] == product_filter]
    filtered_df = filtered_df[filtered_df['Sales'] >= min_sales]

    # Display filtered data
    st.write(f"Showing {len(filtered_df)} rows out of {len(df)} total rows")
    st.dataframe(filtered_df, use_container_width=True)

    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name=f'filtered_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
        mime='text/csv'
    )

# Advanced features section
st.markdown("---")
st.header("🎛️ Advanced Interactive Elements")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("File Upload")
    uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])
    if uploaded_file is not None:
        user_df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:")
        st.dataframe(user_df.head())

with col2:
    st.subheader("Text Input & Analysis")
    user_text = st.text_area("Enter some text to analyze", "Streamlit is awesome!")
    if user_text:
        word_count = len(user_text.split())
        char_count = len(user_text)
        st.write(f"Words: {word_count} | Characters: {char_count}")

with col3:
    st.subheader("Progress Demo")
    if st.button("Run Progress Demo"):
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.text(f'Progress: {i + 1}%')
            time.sleep(0.01)

        st.success("Demo completed!")

# Session state example
st.markdown("---")
st.header("💾 Session State Example")

if 'counter' not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Increment'):
        st.session_state.counter += 1

with col2:
    if st.button('Decrement'):
        st.session_state.counter -= 1

with col3:
    if st.button('Reset'):
        st.session_state.counter = 0

st.write(f'Counter value: {st.session_state.counter}')

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ using Streamlit | Data refreshed every time you interact with controls</p>
</div>
""", unsafe_allow_html=True)

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.info("""
This demo showcases various Streamlit features:
- Interactive widgets
- Multiple chart types
- Tabs and columns
- Caching
- Session state
- File upload/download
- And much more!
""")

st.sidebar.success("✅ Demo loaded successfully!")


# run with:
# streamlit run D:\Study\Projects\PycharmProjects\playground\lab\exercise_streamlit.py
