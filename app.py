import streamlit as st
import pickle

# Buka file dalam mode 'rb' (read binary)
with open('diabetes_model.sav', 'rb') as file:
    diabetes_model = pickle.load(file)

st.title("Prediksi Diabetes")


pregnancies = st.text_input('Input nilai Pregnancies (Kehamilan)')
glucose = st.text_input('Input nilai Glukosa (Kadar Gula Darah)')
bloodPressure = st.text_input('Input nilai Tekanan Darah')
skinThickness = st.text_input('Input nilai Ketebalan Kulit (Skin Thiickness)')
insulin = st.text_input('Input nilai Insulin')
bmi = st.text_input('Input nilai Body Mass Index (BMI)')
diabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')
age = st.text_input('Input Umur')

diabetes_diagnosis = ''

# prediksi 
if st.button('Prediksi'):
    diabetes_prediction = diabetes_model.predict([[pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]])

    if(diabetes_prediction[0] == 0):
        diabetes_diagnosis = 'Prediksi : Terkena Diabetes'
    else:
        diabetes_diagnosis = 'Prediksi : Tidak Terkena Diabetes'

    st.success(diabetes_diagnosis)


