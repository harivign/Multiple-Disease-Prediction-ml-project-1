import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open('parkinsons.pkl', 'rb'))

# Prediction Function
def db_pred(mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz, mdvp_jitter_pct, mdvp_jitter_abs,
            mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, 
            shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, 
            rpde, dfa, spread1, spread2, d2, ppe):
    # Convert inputs to NumPy array
    ip = np.array([[mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz, mdvp_jitter_pct, mdvp_jitter_abs,
                    mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, 
                    shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, 
                    rpde, dfa, spread1, spread2, d2, ppe]])
    # Model prediction
    result = model.predict(ip)
    return result

# Streamlit App
st.title("🛠️ Smart Parkinson's Prediction Dashboard")
st.write("Enter the required details below to predict Parkinson's disease.")

# Input Fields in a Form
with st.form("prediction_form"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        mdvp_fo_hz = st.text_input("MDVP:Fo(Hz)", value="")
    with col2:
        mdvp_fhi_hz = st.text_input("MDVP:Fhi(Hz)", value="")
    with col3:
        mdvp_flo_hz = st.text_input("MDVP:Flo(Hz)", value="")
    with col4:
        mdvp_jitter_pct = st.text_input("MDVP:Jitter(%)", value="")
    
    with col1:
        mdvp_jitter_abs = st.text_input("MDVP:Jitter(Abs)", value="")
    with col2:
        mdvp_rap = st.text_input("MDVP:RAP", value="")
    with col3:
        mdvp_ppq = st.text_input("MDVP:PPQ", value="")
    with col4:
        jitter_ddp = st.text_input("Jitter:DDP", value="")
    
    with col1:
        mdvp_shimmer = st.text_input("MDVP:Shimmer", value="")
    with col2:
        mdvp_shimmer_db = st.text_input("MDVP:Shimmer(dB)", value="")
    with col3:
        shimmer_apq3 = st.text_input("Shimmer:APQ3", value="")
    with col4:
        shimmer_apq5 = st.text_input("Shimmer:APQ5", value="")
    
    with col1:
        mdvp_apq = st.text_input("MDVP:APQ", value="")
    with col2:
        shimmer_dda = st.text_input("Shimmer:DDA", value="")
    with col3:
        nhr = st.text_input("NHR", value="")
    with col4:
        hnr = st.text_input("HNR", value="")
    
    with col1:
        rpde = st.text_input("RPDE", value="")
    with col2:
        dfa = st.text_input("DFA", value="")
    with col3:
        spread1 = st.text_input("Spread1", value="")
    with col4:
        spread2 = st.text_input("Spread2", value="")
    
    with col1:
        d2 = st.text_input("D2", value="")
    with col2:
        ppe = st.text_input("PPE", value="")

    submit_button = st.form_submit_button(label="Predict")

# Prediction Button
if submit_button:
    try:
        # Convert text inputs to float for prediction
        mdvp_fo_hz = float(mdvp_fo_hz)
        mdvp_fhi_hz = float(mdvp_fhi_hz)
        mdvp_flo_hz = float(mdvp_flo_hz)
        mdvp_jitter_pct = float(mdvp_jitter_pct)
        mdvp_jitter_abs = float(mdvp_jitter_abs)
        mdvp_rap = float(mdvp_rap)
        mdvp_ppq = float(mdvp_ppq)
        jitter_ddp = float(jitter_ddp)
        mdvp_shimmer = float(mdvp_shimmer)
        mdvp_shimmer_db = float(mdvp_shimmer_db)
        shimmer_apq3 = float(shimmer_apq3)
        shimmer_apq5 = float(shimmer_apq5)
        mdvp_apq = float(mdvp_apq)
        shimmer_dda = float(shimmer_dda)
        nhr = float(nhr)
        hnr = float(hnr)
        rpde = float(rpde)
        dfa = float(dfa)
        spread1 = float(spread1)
        spread2 = float(spread2)
        d2 = float(d2)
        ppe = float(ppe)

        # Get prediction result
        pred = db_pred(mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz, mdvp_jitter_pct, mdvp_jitter_abs,
                       mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, 
                       shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, 
                       rpde, dfa, spread1, spread2, d2, ppe)
        
        if pred == 1:
            st.write("You have Parkinson's disease 😢")
        else:
            st.write("You don't have Parkinson's disease 🎉")

    except ValueError:
        st.error("Please ensure all inputs are numeric and valid.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
