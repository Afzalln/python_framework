import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

st.title("Advanced Data to Graph Application")
st.write("Upload a CSV file to visualize the data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    columns = st.multiselect("Select columns", list(df.columns))

    chart_type = st.selectbox("Select chart type", ["Line Chart", "Bar Chart", "Scatter Plot"])

    if chart_type == "Line Chart":
        st.subheader("Line Chart")
        hue_column = st.selectbox("Select hue column (optional)", ["None"] + list(df.columns))
        if hue_column != "None":
            line_chart = sns.lineplot(data=df, x=columns[0], y=columns[1], hue=hue_column)
        else:
            line_chart = sns.lineplot(data=df[columns])
        st.pyplot()

    elif chart_type == "Bar Chart":
        st.subheader("Bar Chart")
        hue_column = st.selectbox("Select hue column (optional)", ["None"] + list(df.columns))
        if hue_column != "None":
            bar_chart = sns.barplot(data=df, x=columns[0], y=columns[1], hue=hue_column)
        else:
            bar_chart = sns.barplot(data=df[columns])
        st.pyplot()

    elif chart_type == "Scatter Plot":
        st.subheader("Scatter Plot")
        size_column = st.selectbox("Select size column (optional)", ["None"] + list(df.columns))
        if size_column != "None":
            scatter_plot = sns.scatterplot(data=df, x=columns[0], y=columns[1], size=df[size_column])
        else:
            scatter_plot = sns.scatterplot(data=df, x=columns[0], y=columns[1])
        st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.sidebar.subheader("Additional Options")

    if st.sidebar.checkbox("Histogram"):
        st.subheader("Histogram")
        hist_plot = sns.histplot(data=df[columns])
        st.pyplot()

    if st.sidebar.checkbox("Heatmap"):
        st.subheader("Heatmap")
        corr = df[columns].corr()
        heatmap = sns.heatmap(corr, annot=True)
        st.pyplot()

    if st.sidebar.checkbox("Descriptive Statistics"):
        st.subheader("Descriptive Statistics")
        stats = df[columns].describe()
        st.dataframe(stats)

     
    if st.sidebar.checkbox("Correlation"):
        st.subheader("Correlation")
        corr_matrix = df[columns].corr()
        st.dataframe(corr_matrix)

    if st.sidebar.checkbox("Pairplot"):
        st.subheader("Pairplot")
        pairplot = sns.pairplot(df[columns])
        st.pyplot()