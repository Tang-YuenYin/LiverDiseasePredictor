import streamlit as st
import pandas as pd

st.set_page_config(page_title="Liver Predictor",page_icon="🧑‍⚕️")
#Function to display the content in the Home Page
st.title("ABOUT US")
st.sidebar.success("Select a page above")
st.text("")
st.subheader("Problem Statement")
st.write(
 """
Overall, about 1 in 10 Americans (30 million in total) have some type of liver disease. About 5.5 million people in the U.S. have chronic liver disease or cirrhosis.

Some types of liver disease are becoming more common in the U.S. because they are related to rising rates of obesity. An estimated 20% to 30% of adults have excess fat in their liver, a condition called non-alcohol rekated fatty liver disease (NAFD). This may be renamed metabolic-associated fatty liver disease (MAFLD) to reflect its relationship to metabolic syndrome and conditions like diabetes, high blood pressure, high cholesterol and obesity.
 """   
)
st.text("")
st.write("---")
st.text("")
st.subheader("Objective")
st.write(
 """
 *Help in prediction of liver disease

 *Act as a guidance for professionals
 """   
)
st.text("")
st.write("---")
st.text("")
st.subheader("Our Team")
st.write(
 """
 * Adeline Kong Earn Ning

 * Lee Zia Qian

 * Low Hui Yi

 * Tang Yuen Yin

 * Yoong Jing Yi 
 """   
)
