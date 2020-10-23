import streamlit as st
import numpy as np
import matplotlib.pyplot as plt




st.header("Matplotlib chart in Plotly")


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

