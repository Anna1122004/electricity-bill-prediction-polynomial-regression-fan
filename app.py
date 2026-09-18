import streamlit as st
import joblib
import pandas as pd

model = joblib.load("polynomial_regression-fan.pkl")
poly = joblib.load("polynomial_features-fan.pkl")

st.title("Electricity Bill Prediction")

ac_unit = st.number_input(
    "Enter AC Units",
    value=30.0
)
fan_unit = st.number_input(
    "Enter Fan Units",
    value=30.0
)
if st.button("Predict"):

    if ac_unit < 1:
        st.error("AC Units cannot be less than 1")

    elif ac_unit > 150:
        st.error("AC Units cannot be greater than 150")
    elif fan_unit < 1:
        st.error("AC Units cannot be less than 1")

    elif fan_unit > 150:
        st.error("AC Units cannot be greater than 150")
    else:
        new_data = pd.DataFrame({
            "AC_Units": [ac_unit],
          "Fan_Units":[fan_unit]
        })

        new_data_poly = poly.transform(new_data)

        prediction = model.predict(new_data_poly)

        st.success(f"Predicted Electricity Bill: {prediction[0]:.2f}")
