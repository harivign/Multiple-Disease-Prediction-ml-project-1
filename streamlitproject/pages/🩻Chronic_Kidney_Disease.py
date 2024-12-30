import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("kidney_disease (1).pkl", "rb"))

# Map categorical values to numeric representations
categorical_mapping = {
    "rbc": {"normal": 1, "abnormal": 0},
    "pc": {"normal": 1, "abnormal": 0},
    "pcc": {"notpresent": 0, "present": 1},
    "ba": {"notpresent": 0, "present": 1},
    "htn": {"yes": 1, "no": 0},
    "dm": {"yes": 1, "no": 0},
    "cad": {"yes": 1, "no": 0},
    "appet": {"good": 1, "poor": 0},
    "pe": {"yes": 1, "no": 0},
    "ane": {"yes": 1, "no": 0},
}

# Function to handle missing or invalid values
def handle_missing_values(value):
    if value is None or value == "":
        return 0.0  # Replace with a default value, e.g., 0.0
    try:
        return float(value)
    except ValueError:
        return 0.0  # Replace invalid values with 0.0

# Prediction function
def predict_kidney_disease(features):
    prediction = model.predict(features)
    return prediction

# Streamlit app
st.title("🩺 Kidney Disease Prediction Dashboard")

# Input fields with default values
age = st.number_input("Age", min_value=0, max_value=300, step=1, value=0)
bp = st.number_input("Blood Pressure (BP)", min_value=0, max_value=500, step=1, value=0)
sg = st.number_input("Specific Gravity (SG)", min_value=1.000, max_value=2.030, step=0.001, format="%.3f", value=1.000)
al = st.number_input("Albumin (AL)", min_value=0, max_value=10, step=1, value=0)
su = st.number_input("Sugar (SU)", min_value=0, max_value=10, step=1, value=0)
rbc = st.selectbox("Red Blood Cells (RBC)", ["", "normal", "abnormal"])
pc = st.selectbox("Pus Cell (PC)", ["", "normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps (PCC)", ["", "notpresent", "present"])
ba = st.selectbox("Bacteria (BA)", ["", "notpresent", "present"])
bgr = st.number_input("Blood Glucose Random (BGR)", min_value=0, max_value=700, step=1, value=0)
bu = st.number_input("Blood Urea (BU)", min_value=0, max_value=500, step=1, value=0)
sc = st.number_input("Serum Creatinine (SC)", min_value=0.0, max_value=50.0, step=0.1, value=0.0)
sod = st.number_input("Sodium (SOD)", min_value=0, max_value=500, step=1, value=0)
pot = st.number_input("Potassium (POT)", min_value=0.0, max_value=30.0, step=0.1, value=0.0)
hemo = st.number_input("Hemoglobin (HEMO)", min_value=0.0, max_value=50.0, step=0.1, value=0.0)
pcv = st.text_input("Packed Cell Volume (PCV)", value="0")
wc = st.text_input("White Blood Cell Count (WC)", value="0")
rc = st.text_input("Red Blood Cell Count (RC)", value="0")
htn = st.selectbox("Hypertension (HTN)", ["", "yes", "no"])
dm = st.selectbox("Diabetes Mellitus (DM)", ["", "yes", "no"])
cad = st.selectbox("Coronary Artery Disease (CAD)", ["", "yes", "no"])
appet = st.selectbox("Appetite", ["", "good", "poor"])
pe = st.selectbox("Pedal Edema (PE)", ["", "yes", "no"])
ane = st.selectbox("Anemia (ANE)", ["", "yes", "no"])

if st.button("Predict"):
    try:
        # Handle missing values and map categorical inputs
        pcv = handle_missing_values(pcv)
        wc = handle_missing_values(wc)
        rc = handle_missing_values(rc)

        # Validate inputs
        if "" in [rbc, pc, pcc, ba, htn, dm, cad, appet, pe, ane]:
            st.error("Please fill in all the fields.")
        else:
            # Prepare the feature array for prediction
            features = np.array([[ 
                age, bp, sg, al, su, 
                categorical_mapping["rbc"].get(rbc, 0), 
                categorical_mapping["pc"].get(pc, 0), 
                categorical_mapping["pcc"].get(pcc, 0), 
                categorical_mapping["ba"].get(ba, 0), 
                bgr, bu, sc, sod, pot, hemo, 
                pcv, wc, rc,
                categorical_mapping["htn"].get(htn, 0), 
                categorical_mapping["dm"].get(dm, 0), 
                categorical_mapping["cad"].get(cad, 0), 
                categorical_mapping["appet"].get(appet, 0), 
                categorical_mapping["pe"].get(pe, 0), 
                categorical_mapping["ane"].get(ane, 0)
            ]])

            # Reshape the features for prediction
            features = features.reshape(1, -1)

            # Make prediction
            prediction = predict_kidney_disease(features)

            # Display result
            if prediction == 0:
                st.success("The model predicts that the patient has Chronic Kidney Disease (CKD).")
            else:
                st.success("The model predicts that the patient does not have Chronic Kidney Disease (CKD).")

    except ValueError as ve:
        st.error(f"ValueError encountered: {ve}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
