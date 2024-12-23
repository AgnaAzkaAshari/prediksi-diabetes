import streamlit as st
import pickle

with open('diabetes_svm.sav', 'rb') as file:
    diabetes_model = pickle.load(file)

st.title("Prediksi Diabetes")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.text_input('Input nilai Pregnancies (Kehamilan)')

with col1:
    glucose = st.text_input('Input nilai Glukosa (Kadar Gula Darah)')

with col2:
    bloodPressure = st.text_input('Input nilai Tekanan Darah')

with col2:
    skinThickness = st.text_input('Input nilai Ketebalan Kulit (Skin Thiickness)')

with col1:
    insulin = st.text_input('Input nilai Insulin')

with col1:
    bmi = st.text_input('Input nilai Body Mass Index (BMI)')

with col2:
    diabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')

with col2:
    age = st.text_input('Input Umur')


diabetes_diagnosis = ''

# prediksi 
if st.button('Prediksi'):
    diabetes_prediction = diabetes_model.predict([[pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]])

    if(diabetes_prediction[0] == 1):
        diabetes_diagnosis = 'Prediksi : Terkena Diabetes'
    else:
        diabetes_diagnosis = 'Prediksi : Tidak Terkena Diabetes'

    st.success(diabetes_diagnosis)


