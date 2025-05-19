import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('best_model.joblib')


st.title("Prediksi Dropout Mahasiswa")

# Form input
st.header("Masukkan Data Mahasiswa")

curricular_2nd_approved = st.number_input("Curricular Units 2nd Sem Approved", 0, 50, step=1)
curricular_2nd_grade = st.number_input("Curricular Units 2nd Sem Grade", 0.0, 20.0, step=0.1)
curricular_1st_approved = st.number_input("Curricular Units 1st Sem Approved", 0, 50, step=1)
curricular_1st_grade = st.number_input("Curricular Units 1st Sem Grade", 0.0, 20.0, step=0.1)
tuition_fees_up_to_date = st.selectbox("Tuition Fees Up-to-date? (0=No, 1=Yes)", [1, 0])
scholarship_holder = st.selectbox("Scholarship Holder?", ["Yes", "No"])

# Buat dataframe
input_data = pd.DataFrame([{
    'Curricular_units_2nd_sem_approved': curricular_2nd_approved,
    'Curricular_units_2nd_sem_grade': curricular_2nd_grade,
    'Curricular_units_1st_sem_approved': curricular_1st_approved,
    'Curricular_units_1st_sem_grade': curricular_1st_grade,
    'Tuition_fees_up_to_date': tuition_fees_up_to_date,
    'Scholarship_holder': scholarship_holder
}])

# Prediksi
if st.button("Prediksi"):
    proba = model.predict_proba(input_data)[0]
    pred = model.predict(input_data)[0]
    
    status = "Dropout (berpotensi DO)" if pred == 1 else "Lanjut Studi (Enrolled/Graduate)"
    st.subheader(f"Hasil Prediksi: {status}")
    st.write(f"Probabilitas Dropout: {proba[1]:.2f}%")
    st.write(f"Probabilitas Tidak Dropout: {proba[0]:.2f}%")