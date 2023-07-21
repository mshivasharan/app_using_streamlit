import streamlit as st
import plotly.express as px
from backend import get_data

st.header('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forcastdays', min_value=1, max_value=5,
                 help='select the number of forcasting days')

options = st.selectbox('select data to view', 
                       ('Temperature', 'Sky'))

st.subheader(f'{options} for the next {days} days in {place}')

d, t = get_data(place, days, options)

figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)