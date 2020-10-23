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

st.write('The $\{R_i^{\alpha}\}$ represent the Cartesian coordinates $\alpha$ of atom $i$. In a first step these coordinates')
st.write(' are transformed into a set of symmetry function values $\{G_i^{\mu}\}$ for each atom $i$. These symmetry function ')
st.write('values describe the energetically relevant local environment of each atom and are subsequently used as input for the NN. ')
st.write('They depend on the positions of all atoms in the system, as indicated by the dotted arrows.')

st.write('For each atom in the system there is now a NN which we call subnet $S_i$ and which after the weight optimization yields ')
st.write('the energy contribution $E_i$.')

st.write('To ensure the invariance of the total energy with respect to the interchanging of two atoms the structure of all ')
st.write('subnets and the values of the weight paramaters are constrained to be identical in each $S_i$.')

st.write('**The crucial point is the introduction of a new type of symmetry function.** While other types of symmetry functions have ')
st.write('been used before, in our approach the symmetry function values of each atom reflect the local environment that determines ')
st.write('its energy: ')
st.write('1. two structures with different energies must yield different sets of symmetry function values, ')
st.write('2. identical local environments must give rise to the same set.')

st.write('3. the symmetry function values must be invariant with respect to a rotation or translation of the system. ')
st.write('4. the number of symmetry functions must be independent of the coordination of the atom, because the coordination ')
st.write('number of an atom can change in a MD simulation, while the structure of the subnets must not be changed if the NN is ')
st.write('to remain applicable generally.')

st.write('In the nodes of the input layer the two generalized coordinates $G_i^1$ and $G_i^2$ that determine the energy of configuration $i$ are provided.')
st.write('The node in the output layer yields the associated energy $E_i$, which in this case depends on the values of the two input nodes $G_i^1$ and $G_i^2$.')
#st.write('$$f_c(R_{ij})= 0.5\times[\cos(\frac{\pi R_{ij}}{R_c})+1]$$')#  \text{for }R_{ij}\le R_c\\0     \text{for }R_{ij}\gt R_c  $$')
st.write('$$f_c(R_{ij})=0.5\cos(\pi R_{ij}/R_c)+1$$ for $R_{ij}\le R_c$')
st.write('and $0$ otherwise:')
#\times[\cos(\frac{\pi R_{ij}}{R_c})+1]
Rc = st.slider('Rc',1,20)  #
#st.write(x, 'squared is', x * x)
fig = plt.figure(figsize=(4,2))
#Rc=x
x = np.arange(0,Rc+0.2,0.2)
y = 0.5*(np.cos(np.pi*x/Rc)+1)
#plt.legend(['Rc=11'])
plt.xlabel('R_ij')
plt.ylabel('f_c')
plt.hlines(y=0.0-0.002, xmin=Rc, xmax=20, linewidth=1.5)
plt.plot(x,y)
st.pyplot(fig)

