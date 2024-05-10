import numpy as np
import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")

#=======================================================================================
st.set_page_config(page_title="Admission Predicto", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")
#=======================================================================================

# st.title("Diabetes Predictor")
st.markdown("<h1 style='text-align: center;'>Diabetes Predictor</h1>", unsafe_allow_html=True)

#=======================================================================================

model=pickle.load(open("diabetes.pkl","rb"))

#=======================================================================================


def user_input():
    col1,col2,col3=st.columns(3)

    with col1:
        Pregnancies=st.number_input("How many Pregnancies experience do you have: ")
    with col2:
        Glucose=st.number_input("What is your Glucose Level(out of 300): ")
    with col3:
        Insulin=st.number_input("What is your Insulin Level(out of 400): ")
    col4,col5,col6=st.columns(3)
    with col4:
        BMI=st.number_input("What is your Body Mass Index(BMI)(out of 100): ") #weight/(Height)**2
    with col5:
        DiabetesPedigreeFunction=st.number_input("What is your GeneticDiabetesScore(out of 1.5): ")
    with col6:
        Age=st.number_input("What is your Age(out of 150): ")

    outcome=np.array([[Pregnancies,Glucose,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    if st.button("Submit"):
        result=model.predict(outcome)
        if result==1:
            st.write("**Regrettably, it appears that you are experiencing symptoms consistent with diabetes.**", unsafe_allow_html=True)

        else:
            st.write("**Congratulations, you exhibit no symptoms indicative of diabetes**", unsafe_allow_html=True)

user_input()
            


