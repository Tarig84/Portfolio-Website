import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Tarig Eltayeb')
    content = """
    Hi, I am Tarig! I am a python programmer, teacher, and founder of PythonHow. I graduated in 2013 with a Master of 
    Science in Geospatial Technologies from the University of Muenister in Germany with a focus on using Python remote 
    sensing. I have worked with companies from various countries, such as the Center for Conservation Geography, to map 
    and understand Australian ecosystem, image processing with the Swiss In-Terra, and performing data mining to gain 
    business insights with the Australian Rapid Intelligence.
    """
    st.info(content)
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)