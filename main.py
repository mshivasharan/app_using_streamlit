import streamlit as st

st.header('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forcastdays', min_value=1, max_value=5,
                 help='select the number of forcasting days')

options = st.selectbox('select data to view', 
                       ('Temperature', 'Sky'))

st.subheader(f'{options} for the next {days} days in {place}')