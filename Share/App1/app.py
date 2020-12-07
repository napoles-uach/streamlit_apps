import streamlit as st
import os
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import imageio
from scipy.spatial.distance import cdist
import random
#st.title('Empty app :rocket:')

# Put your Python+Streamlit code here ...
# you can modify it by double cliking on the folder icon at the left

text=st.sidebar.text_input('enter the text (line break with backslash+n)','Text\n as a Graph')
pnt_sz=st.sidebar.number_input('Enter the point size',100)
var1= '"{0}"'.format(text)


cmd="convert -size 800x200 xc:White -gravity Center   -weight 700 -pointsize {1}  -annotate 0 {0}   image.png".format(var1,pnt_sz)

os.system(cmd)

st.image('./image.png')

im = imageio.imread('./image.png')


sam = st.sidebar.selectbox('Number of nodes',(500,1000,1500,2000),3)
nodsize = st.sidebar.selectbox('Node size',(0,1,2,3,4,5))

#st.write((im[0]))
G = nx.Graph()

@st.cache
def readim():

	lista=[]
	for i in range(im.shape[0]):
	  for j in range(im.shape[1]):
	    bit=im[i][j]#np.sum(im[i][j][:2])
	    if bit!=255:
	      lista.append([i,j])
	return(lista)
#lista=[]
lista=readim()
#st.write(lista)
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
#-------------------------------------------------------
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
Rc = st.slider('Cutoff radius',1,30,10)
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
 


st.balloons()
