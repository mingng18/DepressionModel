import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="Depression Model", page_icon=":snowflake:")

result = "haha"

#===================================title====================================================
st.markdown("<h1>Depression Model</h1>", unsafe_allow_html=True)
st.markdown("<h3>By group 13</h3>", unsafe_allow_html=True)
st.markdown("<h4>Group members:</h4>", unsafe_allow_html=True)
st.write("Ng Gih Ming U2102856:snowflake:")
st.write("Ng Gih Ming U2102856:snowflake:")
st.write("Ng Gih Ming U2102856:snowflake:")
st.write("Ng Gih Ming U2102856:snowflake:")
st.write("Ng Gih Ming U2102856:snowflake:")
st.write("---")

st.markdown("<h3Personal Information</h3>", unsafe_allow_html=True)
gender = st.radio('Gender',("Male", "Demale"))
ethics = st.radio('Ethics',("Malay", "Chinese", "India", "Lain-lain"))
ages = st.text_input('Ages')
df = pd.DataFrame({'status': ["Single", "Married", "Divorced", "Widow"],})
status = st.selectbox('Status',df['status'])
noOfDependents = st.radio('Number of dependents',("0", "1-2", "3-4", "5+"))
eduLevel = st.radio('Educational level',("Secondary school", "Diploma", "Degree", "Master/Prof/Doctor"))
workStatus = st.radio('Occupation',("Full Time", "Part Time", "Student", "Housewife", "Doesn't work"))
Health = st.slider('Rate Your Health', 1, 3, 1)
st.write("---")

st.markdown("<h3>BDI-II Test</h3>", unsafe_allow_html=True)
st.write("1 = Rarely think of, 2 = Sometimes, 3 = Always think of")
sadness = st.slider('Rate Your Sadness Level', 1, 3, 1)
pessimistic = st.slider('Rate Your Pessimistic Level', 1, 3, 1)
pastFailure = st.slider('Rate Your Past Failure Level', 1, 3, 1)
lostOfSatis = st.slider('Loss of Satisfaction', 1, 3, 1)
wrongFeel = st.slider('Always feel wrong?', 1, 3, 1)
punishFeel = st.slider('Always feel being punished?', 1, 3, 1)
dislikeSelf = st.slider('Dislike yourself?', 1, 3, 1)
critiqueSelf = st.slider('Critique yourself?', 1, 3, 1)
suicide = st.slider('Thought of suicide?', 1, 3, 1)
cry = st.slider('Want to cry?', 1, 3, 1)
heartBroke = st.slider('Heart Broken?', 1, 3, 1)
lossOfInterest = st.slider('Loss of interest?', 1, 3, 1)
hardDecide = st.slider('Hard to make decision?', 1, 3, 1)
feelUseless = st.slider('Feel useless?', 1, 3, 1)
lossPower = st.slider('Loss Power?', 1, 3, 1)
sleepQuality = st.slider('Sleep quality Drop?', 1, 3, 1)
annoyed = st.slider('Easily being annoyed?', 1, 3, 1)
lossOfAppetite = st.slider('Loss of appetite?', 1, 3, 1)
bodyWeight = st.slider('Body weight drop drastically?', 1, 3, 1)
worryPhyAppearance = st.slider('Worry about physical appearance?', 1, 3, 1)
st.write("---")
if st.button('Check Me!'):
  # Add a placeholder
  latest_iteration = st.empty()
  bar = st.progress(0)

  for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Checking {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

  '...the result is out now!'
  'You are ' + result
else:
  st.write("Press the button to check!")

st.write("---")
st.markdown("<h3>Background of our study</h3>", unsafe_allow_html=True)
st.markdown("<h3>Data set preview</h3>", unsafe_allow_html=True)
st.write("The dataset is about data concerning depressive symptoms using the Bahasa Malaysia version of the Beck Depression Inventory-II (Malay-BDI II) questionnaire with the associated acoustic features of speech and demographic information. The data was gathered from a population on social media of Bahasa Malaysia Speaker. ")
st.write("[Link to dataset >](https://data.mendeley.com/datasets/mm4nm7ndp2/2/files/52af697a-6e3a-4763-898b-3e1db23c212f)")
data = pd.read_csv("dataset.csv")
st.write(data)
st.write("---")