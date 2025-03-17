import streamlit as st
import joblib


def load_model(filename):
  model = joblib.load(filename)
  return model

def predict_wtih_model(model,user_input):
  prediction = model.predict([user_input])
  return prediction[0]

def main():
  st.title('Dermatology Machine Learning')
  st.info('This App Using Machine Learning!')

  #input data by user
  erythema = st.slider('Erythema' , min_value=0, max_value=3, value=2)

if __name__ == "__main__":
  main()
