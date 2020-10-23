import streamlit as st
import numpy as np
import matplotlib.pyplot as plt




st.header("Behler")

fig = plt.figure(figsize=(4,2))
Rc=11.0
x = np.arange(0,11,0.2)
y = 0.5*(np.cos(np.pi*x/Rc)+1)
plt.plot(x,y)
st.pyplot(fig)

