# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:41:56 2024

@author: HP
"""

import streamlit as st


import base64

def set_background(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_background('C:/Users/HP/Desktop/Multiple disease project/city.jpg') 


# page title
st.title('Body Mass Index Calculator')


unit = st.selectbox('Measurement system :', ['Metric System', 'Imperial System'],
                    help = 'Select the measurement system you are using to give your height and weight')


height = st.number_input('Height(cm or inches) : ', step = 1, value = 1, placeholder = "Input your Height")


weight = st.number_input('Weight(kg or pounds) : ', step = 1, value = 1, placeholder = "Input your Weight")



bmi_diagnosis = ''


if st.button('Calculate BMI : '):
    
    
    if unit == 'Metric System':
        bmi = round(weight / ((height/100) **2), 2)
        
    else:
        bmi = round(((weight / (height **2)) * 703), 2)
        
        
    if bmi < 18.5:
        st.info('Your Body Mass Index is {}.'.format(bmi))
        
        st.info('Weight Category: :blue[Underweight Category]')
        
        
        
    elif bmi >= 18.5 and bmi < 25:
        
        st.success('Your Body Mass Index is {}.'.format(bmi))
        
        st.success('Weight Category: :green[Healthy Weight Category]')
        
        
    elif bmi >=25 and bmi < 30:
        
        st.warning('Your Body Mass Index is {}.'.format(bmi))
        
        st.warning('Weight Category: :yellow[Over Weight Category]')
        
        
    else:
        
        st.error('Body Mass Index is {}.'.format(bmi))
        
        st.error('Weight Category: :red[Obese Category]')



