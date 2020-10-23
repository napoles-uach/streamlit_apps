import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components



st.header("Review of Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces")
st.write('The structure of a simple NN as it has hitherto been used to represent PESs is shown schematically for a 2D PES.')
#st.write('![texto alternativo](https://pubs.rsc.org/image/article/2017/SC/c7sc02267k/c7sc02267k-f1_hi-res.gif) ')
#components.html(
#    """ 
st.write('Thus, in order to represent PESs useful for all system sizes, a new NN topology has to be introduced.')

st.write('The main idea is to represent the total energy $E$ of the system as a sum of atomic contributions $E_i$, (typically used in empirical potentials)')

st.write('$$E=\sum_i E_i$$')

st.write('The general structure of this new network topology is shown schematically for a system consisting of three atoms.')

st.write('![texto alternativo](https://pubs.rsc.org/image/article/2017/SC/c7sc02267k/c7sc02267k-f1_hi-res.gif) ')
st.write('In the nodes of the input layer the two generalized coordinates $G_i^1$ and $G_i^2$ that determine the energy of configuration $i$ are provided.')
st.write('The node in the output layer yields the associated energy $E_i$, which in this case depends on the values of the two input nodes $G_i^1$ and $G_i^2$.')
#st.write('$$f_c(R_{ij})= 0.5\times[\cos(\frac{\pi R_{ij}}{R_c})+1]$$')#  \text{for }R_{ij}\le R_c\\0     \text{for }R_{ij}\gt R_c  $$')

Rc = st.slider('Rc',1,20)  #
#st.write(x, 'squared is', x * x)
fig = plt.figure(figsize=(4,2))
#Rc=x
x = np.arange(0,Rc+0.2,0.2)
y = 0.5*(np.cos(np.pi*x/Rc)+1)
#plt.legend(['Rc=11'])
plt.xlabel('R_ij')
plt.ylabel('f_c')
plt.hlines(y=0.0-0.001, xmin=Rc, xmax=20, linewidth=1.5)
plt.plot(x,y)
st.pyplot(fig)

