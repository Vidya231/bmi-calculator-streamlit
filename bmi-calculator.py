import streamlit as st
# Title and description
st.title("BMI Calculator 🧮")
st.write("Enter your height and weight to calculate your Body Mass Index (BMI).")

# Input fields
weight = st.number_input("Weight (in kg)", min_value=1.0, max_value=300.0, step=0.5)
height = st.number_input("Height (in cm)", min_value=50.0, max_value=250.0, step=0.5)

# Calculate BMI
if height > 0 and weight > 0:
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.markdown(f"### Your BMI is: `{bmi:.2f}`")

    # Interpret BMI
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
