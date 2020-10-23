import streamlit as st
import numpy as np
import matplotlib.pyplot as plt




st.header("Review of Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces")
st.write('The structure of a simple NN as it has hitherto been used to represent PESs is shown schematically for a 2D PES. ![texto alternativo](https://github.com/napoles-uach/figuras/blob/master/nn.png?raw=true?raw=true) In the nodes of the input layer the two generalized coordinates $G_i^1$ and $G_i^2$ that determine the energy of configuration $i$ are provided.
')

fig = plt.figure(figsize=(4,2))
Rc=11.0
x = np.arange(0,11,0.2)
y = 0.5*(np.cos(np.pi*x/Rc)+1)
plt.plot(x,y)
st.pyplot(fig)

