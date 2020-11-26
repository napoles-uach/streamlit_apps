import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import imageio
from scipy.spatial.distance import cdist
import random

st.title('Turkey Graphs :turkey:')
im = imageio.imread('g.png')


sam = st.sidebar.selectbox('Number of nodes',(500,1000,1500,2000))
nodsize = st.sidebar.selectbox('Node size',(0,1,2,3,4,5))

#st.write(im.shape)
G = nx.Graph()

@st.cache
def readim():

	lista=[]
	for i in range(658):
	  for j in range(592):
	    bit=np.sum(im[i][j][:2])
	    if bit!=510:
	      lista.append([i,j])
	return(lista)
#lista=[]
lista=readim()
#st.write(len(lista))
aList = lista#im[0][0][:].tolist()
#print ("choosing 3 random items from a list using random.sample() function")
sampled_list = random.sample(aList, sam)
turk=np.array(sampled_list)
x_=[]
y_=[]
for elem in turk:
  x,y=elem
  x=-1*x

  x_.append(x)
  y_.append(y)

N=len(x_)

#np.random.seed(1905829)
#N=10
#x = np.random.uniform(20,30, size=(N, ))
#y = np.random.uniform(20,30, size=(N, ))


x=x_
y=y_

xy=np.array(list(zip(x_,y_)))

distancias = cdist(xy, xy, 'euclidean')

distancias_df=pd.DataFrame(data=distancias)

diccio={}  

for i in np.arange(N):
  diccio[str(i)]=np.array([y[i],x[i]])
  


def vecinos(df,r,i):
  return df[df[i] < r][i]

#---------------------------
Rc = st.slider('Cutoff radius',1,30)
def f(radio):
  G = nx.Graph()
  pares=[]
  for i in np.arange(N):
    vec_serie=vecinos(distancias_df,radio,i)
    lista=(list(vec_serie.index.values)) 
    for p in lista:
      if (p != i):
        pares.append([i,p])
  for par in pares:
    G.add_edge(str(par[0]),str(par[1]))
  fig, ax = plt.subplots()
  pos=diccio
  #pos = nx.kamada_kawai_layout(G)
  nx.draw(G,pos=pos,with_labels=False,node_size=nodsize)
  st.pyplot(fig)
  
f(Rc)
 
#--------------------------
my_expander = st.beta_expander('So you want to see the original turkey?? ')
with my_expander:
	st.image('g.png')
	st.write('better close this :satisfied:')

st.balloons()

