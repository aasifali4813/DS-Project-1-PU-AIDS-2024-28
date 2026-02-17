import streamlit as st
import requests

def compute_probability(payload):

    r = requests.post(url="http://127.0.0.1:8080/compute-probability",json=payload)
    return r.json()

st.set_page_config(page_title="A Web App",layout="centered")
st.title("Determine Placement Probability")
st.caption("Frontend:Streamlit | Backend: REST API")
st.subheader(body="Please enter your details below",text_alignment="center")

iq = st.number_input("Enter your IQ here",min_value=40,max_value=160,
                     value="min",step=1)
previous_semester_result = st.number_input("Enter your Previous Semester Result",
                                           min_value=0.0,max_value=10.0,value="min",
                                           step=0.01)
cgpa = st.number_input("Enter your CGPA",min_value=0.0,max_value=10.0,value="min",
                                           step=0.01)
communication_skills = st.number_input("Enter your Communication Skills",
                                       min_value=0,max_value=10,
                                       value="min",step=1)
projects_completed = st.number_input("Enter your Number of Completed Projects",
                                       min_value=0,max_value=10,
                                       value="min",step=1)

payload = {"iq":iq, "previous_semester_result":previous_semester_result,
           "cgpa":cgpa,"communication_skills":communication_skills,
           "projects_completed":projects_completed}

text_area_placeholder = st.empty()

if st.button("Calculate Probability"):
    response = compute_probability(payload)
    text_area_placeholder.text_area(label="Your Placement Probability",
                                    value=response["result"])