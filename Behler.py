import streamlit as st
import numpy as np
import matplotlib.pyplot as plt




st.header("Behler")


#arr = np.random.normal(1, 1, size=100)
#fig, ax = plt.subplots()
#ax.hist(arr, bins=20)

#st.pyplot(fig)


Rc=11.0
x = np.arange(0,11,0.2)
y = 0.5*(np.cos(np.pi*x/Rc)+1)
fig, ax =plt.plot(x,y)

st.pyplot(fig)

