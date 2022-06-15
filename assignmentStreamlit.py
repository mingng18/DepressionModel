import streamlit as st
import numpy as np
import pandas as pd
import time
import pickle
from streamlit_option_menu import option_menu

# st.set_page_config(page_title="Depression Model", page_icon=":snowflake:")

def load_model():
  loaded_model = pickle.load(open("depression_model.sav", 'rb'))
  return loaded_model

def main():
  with st.sidebar:
    st.title("Depression Indicator")
    selected = option_menu(
      menu_title=None,
      options=["Prediction","Dataset", "About Us"],
      icons=["house", "clipboard-check", "info-circle"],
      menu_icon="cast",
      default_index=0,
    )

  if selected == "Prediction":
      st.title("Prediction")
      st.text("")
      predictionResult()

  elif selected == "Dataset":
      st.title("Dataset")
      st.text("")
      datasetPage()

  elif selected == "About Us":
      st.title("About Us")
      st.text("")
      aboutUsPage()

#===================================title====================================================
def aboutUsPage():
  st.markdown("<h1>Depression Model</h1>", unsafe_allow_html=True)
  st.markdown("<h3>By group 13</h3>", unsafe_allow_html=True)
  st.markdown("<h4>Group members:</h4>", unsafe_allow_html=True)
  st.write("Ng Gih Ming U2102856:snowflake:")
  st.write("Ng Gih Ming U2102856:snowflake:")
  st.write("Ng Gih Ming U2102856:snowflake:")
  st.write("Ng Gih Ming U2102856:snowflake:")
  st.write("Ng Gih Ming U2102856:snowflake:")
  st.write("---")

def predictionResult():
  st.markdown("<h3>Personal Information</h3>", unsafe_allow_html=True)
  gender = st.radio('Gender',("Male", "Female"))
  ethics = st.radio('Ethics',("Malay", "Chinese", "India", "Lain-lain"))
  ages = st.text_input('Ages', 20)
  df = pd.DataFrame({'status': ["Single", "Married", "Divorced", "Widow"],})
  status = st.selectbox('Status',df['status'])
  noOfDependents = st.radio('Number of dependents',("0", "1-2", "3-4", "5+"))
  eduLevel = st.radio('Educational level',("Secondary school", "Diploma", "Degree", "Master/Prof/Doctor"))
  workStatus = st.radio('Occupation',("Full Time", "Part Time", "Student", "Housewife", "Doesn't work"))
  health = st.slider('Rate Your Health', 1, 3, 1)
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

  feature_list = [0 if gender == "Male" else 1, 
                  0 if ethics == "Malay" else 1 if ethics == "Chinese" else 2 if ethics == "India" else 3 , 
                  ages, 
                  0 if status == "Single" else 1 if status == "Married" else 2 if status == "Divorced" else 3, 
                  0 if noOfDependents == "0" else 1 if noOfDependents == "1-2" else 2 if noOfDependents == "3-4" else 3, 
                  0 if eduLevel == "Secondary school" else 1 if eduLevel == "Diploma" else 2 if eduLevel == "Degree" else 3,
                  0 if eduLevel == "Full Time" else 1 if eduLevel == "Part Time" else 2 if eduLevel == "Student" else 3 if eduLevel == "Housewife" else 4,
                  health,
                  sadness, pessimistic, pastFailure, lostOfSatis, wrongFeel, punishFeel, dislikeSelf,
                  critiqueSelf, suicide, cry, heartBroke, lossOfInterest, hardDecide, feelUseless, 
                  lossPower, sleepQuality, annoyed, lossOfAppetite, bodyWeight, worryPhyAppearance]
  user_input = np.array(feature_list).reshape(1, -1)


  if st.button('Check Me!'):
    loaded_model = load_model()
    prediction = loaded_model.predict(user_input)

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'Checking {i+1}')
      bar.progress(i + 1)
      time.sleep(0.01)

    '...the result is out now!'
    'You are ' + prediction
  else:
    st.write("Press the button to check!")
  
  st.write("---")


def datasetPage():
  st.markdown("<h3>Background of our study</h3>", unsafe_allow_html=True)
  st.markdown("<h3>Data set preview</h3>", unsafe_allow_html=True)
  st.write("The dataset is about data concerning depressive symptoms using the Bahasa Malaysia version of the Beck Depression Inventory-II (Malay-BDI II) questionnaire with the associated acoustic features of speech and demographic information. The data was gathered from a population on social media of Bahasa Malaysia Speaker. ")
  st.write("[Link to dataset >](https://data.mendeley.com/datasets/mm4nm7ndp2/2/files/52af697a-6e3a-4763-898b-3e1db23c212f)")
  data = pd.read_csv("dataset.csv")
  st.write(data)
  st.write("---")


if __name__ == '__main__':
    main()