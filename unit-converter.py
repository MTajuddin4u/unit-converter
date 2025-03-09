import streamlit as st

st.title("Unit converter App")
st.markdown("### Converts Length, Weight And Time Instantly")
st.write("Welcome! Select category, enter a value and get the converted result in real-time")

category = st.selectbox("choose a category", ["Length", "Weight", "Time"])


def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
           return value * 0.621371
        elif unit == "Miles to Kilometers":
           return value / 0.621371

    elif category =="weight":
        if unit == "kilograms to pounds":
           return value * 2.20462     
    elif unit == "Pounds to Kilograms":
           return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
           return value * 60
    elif unit =="Minutes to seconds":
        return value / 60 
    elif unit == "Minutes to hours":
        return value * 60
    elif unit == "Hours to days":
        return value / 24
    elif unit == "Days to hours":
         return value * 24
    return 0

if category == "Length": 
        unit = st.selectbox("Select conversation",["Kilometer to miles","Miles to kilometers"])
elif category == "Weight":
        unit = st.selectbox("Select conversation", ["Kilograms to pounds", "Pounds to kilograms"])

elif category == "Time":
        unit = st.selectbox("Select converstion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
        result = convert_units(category, value, unit)
        st.success(f"The result is {result:.2f}")