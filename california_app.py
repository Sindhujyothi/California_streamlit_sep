import numpy as np
import joblib
import streamlit as st

# Loaded california data
obj = joblib.load('california.joblib')
model=obj['model']
col=obj['columns']


# california app
st.title('california app')
In=[]
for i in col:
    v = st.number_input(f"Enter {i} value:")
    In.append(v)
if st.button('click'):
    out=model.predict([In])
    st.success(f"The median House value is: {out}")

    