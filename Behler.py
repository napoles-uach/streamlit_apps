import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
st.sidebar.write("Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces")
st.sidebar.write("Jörg Behler and Michele Parrinello")
st.sidebar.write(" Phys. Rev. Lett. 98, 146401 – Published 2 April 2007")
st.sidebar.markdown("DOI: [10.1103/PhysRevLett.98.146401](10.1103/PhysRevLett.98.146401)")


st.title("Review of 'Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces'")

st.write('The main idea is to represent the total energy $E$ of the system as a sum of atomic contributions $E_i$, (typically used in empirical potentials)')

st.latex(r'''E=\sum_i E_i''')


st.write('The general structure of this network topology is shown schematically below:')

st.image('https://pubs.rsc.org/image/article/2017/SC/c7sc02267k/c7sc02267k-f1_hi-res.gif',use_column_width=True)
st.write('The $$R_i$$ represent the Cartesian coordinates of atom $i$. In a first step these coordinates are transformed into a set of \
symmetry function values $\{G_i^{\mu}\}$ for each atom $i$. These symmetry function values describe the energetically relevant local \
environment of each atom and are subsequently used as input for the NN. They depend on the positions of all atoms in the system, as \
indicated by the dotted arrows.')

st.write('**Radial symmetry functions** are constructed as a sum of Gaussians with the parameters $\eta$ and $R_s$')
st.latex(r'''G_i^1=\sum_{j\ne i}^{all} e^{-\eta (R_{ij}-R_s)^2}f_c(R_{ij}) ''')

st.latex(r'''f_c(R_{ij})=0.5\cos(\pi R_{ij}/R_c)+1 \text{ for } R_{ij}\le R_c  ''')
st.write('and $0$ for $R_{ij}>R_c$:')




st.write('$\eta$')
eta = st.selectbox('$\eta$',(1,2,3,4,5))
Rc = st.slider('Rc',1,20,11)

#st.write(x, 'squared is', x * x)
fig = plt.figure(figsize=(4,3.5))
#Rc=x
x = np.arange(0,Rc+0.2,0.2)
y = 0.5*(np.cos(np.pi*x/Rc)+1)
#plt.legend(['Rc=11'])


plt.xlabel(r'$R_{ij}$')
plt.ylabel(r'$f_c$')
plt.hlines(y=0.0-0.0002, xmin=Rc, xmax=20, linewidth=1.5)
plt.ylim(-.05, 1.05)
plt.plot(x,y)
#st.pyplot(fig)

#---------------
fig2 = plt.figure(figsize=(4,3.5))
#Rc=11.3
x = np.arange(0,Rc+0.05,0.05)
plt.hlines(y=0.0-0.002, xmin=Rc, xmax=20, linewidth=1.5)
y1 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-2)**2)
y2 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-3)**2)
y3 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-4)**2)
y4 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-5)**2)
y5 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-6)**2)
y6 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-7)**2)
y7 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-8)**2)
y8 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-9)**2)
plt.legend(['Rc=11.3'])
y9 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-eta*(x-10)**2)

plt.plot(x,y1,x,y2,x,y3,x,y4,x,y5,x,y6,x,y7,x,y8,x,y9)

plt.legend(['Rc=11.3'])
plt.ylim(-.05, 1.05)
plt.xlabel(r'$R_{ij}$')
plt.ylabel(r'$G^1$')
col1, col2 = st.beta_columns((1,1))
col1.pyplot(fig,use_column_width=True)
col2.pyplot(fig2,use_column_width=True)

st.write('Radial symmetry functions for an atom with one neighbor only')




st.write('At interatomic separations larger than the cutoff $R_c$ this function yields zero value and slope. The cutoff has to be sufficiently large to include several nearest neighbors, and in the present Letter a cutoff of 6 Angstroms has been used.')
st.write('*Function $G^1$is a sum of Gaussians multiplied by cutoff functions. The width of the Gaussians is defined by a parameter $\eta$,\
and the center of the Gaussians can be shifted to a certain radial distance by the parameter $R_s$. These "shifted" $G^1$ functions then are \
suitable to describe a spherical shell around the reference atom*.')

