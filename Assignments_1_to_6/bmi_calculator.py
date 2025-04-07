
import streamlit as st
import pandas as pd

# 🎯 Title and Introduction
st.title("💪 BMI Calculator")
st.markdown("---")
st.subheader("By Syed Soaib Sherazi")
st.markdown(
    """
    <a href="https://github.com/sherazi-412002" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github&style=for-the-badge">
    </a>
    """,
    unsafe_allow_html=True
)
st.write("Welcome! This app calculates your Body Mass Index (BMI) based on your height and weight.")
st.write("It also tells you which category you fall into. Stay healthy! 🥦")

# 📏 Input Sliders in Columns
col1, col2 = st.columns(2)

with col1:
    height = st.slider("📏 Height (cm)", min_value=50, max_value=250, value=170)

with col2:
    weight = st.slider("⚖️ Weight (kg)", min_value=20, max_value=200, value=70)

# 🧮 BMI Calculation
bmi = weight / ((height / 100) ** 2)
st.markdown(f"### 📉 Your BMI is: `{bmi:.2f}`")

# 🎨 Display BMI Category with Feedback
if bmi < 18.5:
    st.error("You're underweight 🥲 Try to maintain a balanced diet!")
elif 18.5 <= bmi < 25:
    st.success("You're in the normal range 🥳 Keep it up!")
elif 25 <= bmi < 30:
    st.warning("You're overweight 😬 Consider a healthier routine.")
else:
    st.error("You're in the obesity range 🚨 Take action for your health!")

# 📊 BMI Classification Table
st.markdown("### 🗂️ BMI Classification Chart")
bmi_data = {
    "Category": ["Underweight", "Normal", "Overweight", "Obese"],
    "Min BMI": [0.0, 18.5, 25.0, 30.0],
    "Max BMI": [18.4, 24.9, 29.9, 100.0],
}

df = pd.DataFrame(bmi_data)
st.dataframe(df)

# 📝 Footer
st.markdown("---")
st.caption("Made with ❤️ by **Syed Soaib Sherazi** using Python and Streamlit")







