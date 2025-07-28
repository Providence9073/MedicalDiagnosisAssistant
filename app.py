import streamlit as st
from modules.data_loader import load_data
from modules.trainer import train_model
from modules.predictor import predict_disease
from modules.remedies import suggest_remedy

# Load and train
@st.cache_resource
def setup():
    df = load_data("Training.csv")
    model, le, symptoms, acc = train_model(df)
    return model, le, symptoms, acc

model, le, symptoms, acc = setup()

st.title("🩺 AI Medical Diagnosis Assistant")
st.markdown(f"**Model Accuracy:** {acc*100:.2f}%")

# UI
selected = st.multiselect("Select Symptoms", symptoms)

if st.button("Predict"):
    if not selected:
        st.warning("Please select at least one symptom.")
    else:
        disease = predict_disease(selected, model, le, symptoms)
        remedy = suggest_remedy(disease)
        st.success(f"🤒 Likely Disease: **{disease}**")
        st.info(f"🩹 Suggested Remedy: {remedy}")