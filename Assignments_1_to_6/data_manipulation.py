
import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV File",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Summary Of Data")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select the column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox("Select Unique Values",unique_values)

    filter_df = df[df[selected_column] == selected_values]
    st.write(filter_df)

    st.write("Plot Data")
    x_columns = st.selectbox("Select x-axis columns",columns)
    y_columns = st.selectbox("Select y-axis columns",columns)

    if st.button("Generate Plot"):
        st.line_chart(df.set_index(x_columns)[y_columns])
else:
    st.write("Waiting on file upload....")





