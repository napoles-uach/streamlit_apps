import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


st.title("Review of Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces")

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

st.latex('''f_c(R_{ij})=0.5\cos(\pi R_{ij}/R_c)+1 \text{points in circle} ''')
st.write('for $R_{ij}\le R_c$ and $0$ for $R_{ij}>R_c$:')



#column 1

#col1.write("**Finance and Business:** they can be used to evaluate risk in different \
#options the business is looking at, such as investments")
#col1.write("**Search and Rescue:** US coast guard uses it to predict likely locations of \
#vessels in need of assistance")
#col1.write("**Design and Visuals:** such as video games and producing 3D photo-realistic \
#models and pictures")
#col1.write("**Climate Change:** the Intergovernmental Panel on Climate Change uses it \
#to help in the calculation of energy absorbed in the atmosphere due to greenhouse gasses")
#col1.write("If you want to know more checkout the [Wiki link](https://en.wikipedia.org/wiki/Monte_Carlo_method)")

# column 2: a gif
#col2.write('[Wiki for the image](https://en.wikipedia.org/wiki/Kinetic_theory_of_gases)')
# streamlit share launches from a directory above so need to account for this in the file path

#-------------------------------------------
#\times[\cos(\frac{\pi R_{ij}}{R_c})+1]
#Rc = st.sidebar.slider('Rc',1,20)  #
Rc = st.slider('Rc',1,20,11)
#st.write(x, 'squared is', x * x)
fig = plt.figure(figsize=(4,2))
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
fig2 = plt.figure(figsize=(4,2))
#Rc=11.3
x = np.arange(0,Rc+0.05,0.05)
plt.hlines(y=0.0-0.002, xmin=Rc, xmax=20, linewidth=1.5)
y1 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-2)**2)
y2 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-3)**2)
y3 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-4)**2)
y4 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-5)**2)
y5 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-6)**2)
y6 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-7)**2)
y7 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-8)**2)
y8 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-9)**2)
y9 = 0.5*(np.cos(np.pi*x/Rc)+1)*np.exp(-3*(x-10)**2)

plt.plot(x,y1,x,y2,x,y3,x,y4,x,y5,x,y6,x,y7,x,y8,x,y9)

#plt.legend(['Rc=11.3'])
plt.ylim(-.05, 1.05)
plt.xlabel(r'$R_{ij}$')
plt.ylabel(r'$G^1$')
col1, col2 = st.beta_columns((1,1))
col1.pyplot(fig,use_column_width=True)
col2.pyplot(fig2,use_column_width=True)




st.write('At interatomic separations larger than the cutoff $R_c$ this function yields zero value and slope. The cutoff has to be sufficiently large to include several nearest neighbors, and in the present Letter a cutoff of 6 Angstroms has been used.')
st.write('*Function $G^1$is a sum of Gaussians multiplied by cutoff functions. The width of the Gaussians is defined by a parameter $\eta$, and the center of the Gaussians can be shifted to a certain radial distance by the parameter $R_s$. These "shifted" $G^1$ functions then are suitable to describe a spherical shell around the reference atom*.')
