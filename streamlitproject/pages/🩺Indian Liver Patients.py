import streamlit as st
import numpy as np
import pickle

# Load the ML model
model = pickle.load(open('/home/ubuntu/Multiple-Disease-Prediction-project-1/indian_liver_patient.pkl', 'rb'))

def predict_liver_disease(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase,
                          alamine_aminotransferase, aspartate_aminotransferase, total_proteins,
                          albumin, albumin_and_globulin_ratio):
    # Encode gender (assuming Male=1, Female=0)
    gender_encoded = 1 if gender.lower() == 'male' else 0

    # Prepare the input as a numpy array
    input_data = np.array([[age, gender_encoded, total_bilirubin, direct_bilirubin, 
                             alkaline_phosphotase, alamine_aminotransferase, 
                             aspartate_aminotransferase, total_proteins, albumin, 
                             albumin_and_globulin_ratio]])

    # Make the prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app setup
st.title("🏥 Indian Liver Disease Prediction Dashboard")
st.write("Enter the required details below to predict Indian Liver Disease.")

# Input fields with initial empty values
age = st.number_input("Age", min_value=1, max_value=120, value=None)
gender = st.selectbox("Gender", ["", "Male", "Female"])  # Initial empty value for gender
total_bilirubin = st.number_input("Total Bilirubin", value=None)
direct_bilirubin = st.number_input("Direct Bilirubin", value=None)
alkaline_phosphotase = st.number_input("Alkaline Phosphotase", value=None)
alamine_aminotransferase = st.number_input("Alamine Aminotransferase", value=None)
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", value=None)
total_proteins = st.number_input("Total Proteins", value=None)
albumin = st.number_input("Albumin", value=None)
albumin_and_globulin_ratio = st.number_input("Albumin and Globulin Ratio", value=None)

# Prediction button
if st.button("Predict"):
    # Ensure that all inputs are filled in before making a prediction
    if None in [age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, 
                alamine_aminotransferase, aspartate_aminotransferase, total_proteins, 
                albumin, albumin_and_globulin_ratio] or gender == "":
        st.error("Please fill in all the fields.")
    else:
        # Make prediction only if all fields are filled
        prediction = predict_liver_disease(age, gender, total_bilirubin, direct_bilirubin, 
                                           alkaline_phosphotase, alamine_aminotransferase, 
                                           aspartate_aminotransferase, total_proteins, 
                                           albumin, albumin_and_globulin_ratio)
        
        if prediction == 2:
            st.write("The model predicts you are likely to have Liver Disease. 😞")
        else:
            st.write("The model predicts you are not likely to have Liver Disease. 🎉")
