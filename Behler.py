import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components



st.header("Review of Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces")
st.write('The structure of a simple NN as it has hitherto been used to represent PESs is shown schematically for a 2D PES.')
#st.write('![texto alternativo](https://pubs.rsc.org/image/article/2017/SC/c7sc02267k/c7sc02267k-f1_hi-res.gif) ')
components.html(
    """ 
 Thus, in order to represent PESs useful for all system sizes, a new NN topology has to be introduced.

The main idea is to represent the total energy $E$ of the system as a sum of atomic contributions $E_i$, (typically used in empirical potentials)

$$E=\sum_i E_i$$

The general structure of this new network topology is shown schematically for a system consisting of three atoms.
<figure>
<center>
<img src='https://pubs.rsc.org/image/article/2017/SC/c7sc02267k/c7sc02267k-f1_hi-res.gif' width="400"/>
<figcaption>DOI: 10.1039/C7SC02267K (Edge Article) Chem. Sci., 2017, 8, 6924-6935</figcaption></center>
</figure>
    """,
    width=620,height=600
)
#st.write('In the nodes of the input layer the two generalized coordinates $G_i^1$ and $G_i^2$ that determine the energy of configuration $i$ are provided.')
#st.write('The node in the output layer yields the associated energy $E_i$, which in this case depends on the values of the two input nodes $G_i^1$ and $G_i^2$.')
Rc = st.slider('Rc',1,20)  #
#st.write(x, 'squared is', x * x)
fig = plt.figure(figsize=(4,2))
#Rc=x
x = np.arange(0,11,0.2)
y = 0.5*(np.cos(np.pi*x/Rc)+1)
plt.plot(x,y)
st.pyplot(fig)

