import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("/home/ubuntu/Multiple-Disease-Prediction-project-1/kidney_disease (1).pkl", "rb"))

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
    try:
        return float(value)
    except ValueError:
        return np.nan
    
# Prediction function
def predict_kidney_disease(features):
    prediction = model.predict(features)
    return prediction

# Streamlit app
st.title("🩺 Kidney Disease Prediction Dashboard")

# Input fields with initial empty values
age = st.number_input("Age", min_value=0, max_value=300, step=1, value=None)
bp = st.number_input("Blood Pressure (BP)", min_value=0, max_value=500, step=1, value=None)
sg = st.number_input("Specific Gravity (SG)", min_value=1.000, max_value=2.030, step=0.001, format="%.3f", value=None)
al = st.number_input("Albumin (AL)", min_value=0, max_value=10, step=1, value=None)
su = st.number_input("Sugar (SU)", min_value=0, max_value=10, step=1, value=None)
rbc = st.selectbox("Red Blood Cells (RBC)", ["", "normal", "abnormal"])
pc = st.selectbox("Pus Cell (PC)", ["", "normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps (PCC)", ["", "notpresent", "present"])
ba = st.selectbox("Bacteria (BA)", ["", "notpresent", "present"])
bgr = st.number_input("Blood Glucose Random (BGR)", min_value=0, max_value=700, step=1, value=None)
bu = st.number_input("Blood Urea (BU)", min_value=0, max_value=500, step=1, value=None)
sc = st.number_input("Serum Creatinine (SC)", min_value=0.0, max_value=50.0, step=0.1, value=None)
sod = st.number_input("Sodium (SOD)", min_value=0, max_value=500, step=1, value=None)
pot = st.number_input("Potassium (POT)", min_value=0.0, max_value=30.0, step=0.1, value=None)
hemo = st.number_input("Hemoglobin (HEMO)", min_value=0.0, max_value=50.0, step=0.1, value=None)
pcv = st.text_input("Packed Cell Volume (PCV)", value=None)
wc = st.text_input("White Blood Cell Count (WC)", value=None)
rc = st.text_input("Red Blood Cell Count (RC)", value=None)
htn = st.selectbox("Hypertension (HTN)", ["", "yes", "no"])
dm = st.selectbox("Diabetes Mellitus (DM)", ["", "yes", "no"])
cad = st.selectbox("Coronary Artery Disease (CAD)", ["", "yes", "no"])
appet = st.selectbox("Appetite", ["", "good", "poor"])
pe = st.selectbox("Pedal Edema (PE)", ["", "yes", "no"])
ane = st.selectbox("Anemia (ANE)", ["", "yes", "no"])

if st.button("Predict"):
    # Handle missing values and map categorical inputs
    pcv = handle_missing_values(pcv)
    wc = handle_missing_values(wc)
    rc = handle_missing_values(rc)

    # Check if all required fields are filled in
    if None in [age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane] or "" in [rbc, pc, pcc, ba, htn, dm, cad, appet, pe, ane]:
        st.error("Please fill in all the fields.")
    else:
        # Prepare the feature array for prediction
        features = np.array([[ 
            age, bp, sg, al, su, 
            categorical_mapping["rbc"][rbc], 
            categorical_mapping["pc"][pc], 
            categorical_mapping["pcc"][pcc], 
            categorical_mapping["ba"][ba], 
            bgr, bu, sc, sod, pot, hemo, 
            pcv, wc, rc,
            categorical_mapping["htn"][htn], 
            categorical_mapping["dm"][dm], 
            categorical_mapping["cad"][cad], 
            categorical_mapping["appet"][appet], 
            categorical_mapping["pe"][pe], 
            categorical_mapping["ane"][ane]
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
