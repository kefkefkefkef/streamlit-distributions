import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
x = np.linspace(-10,10,100)
 
def normal_dist(x , mean , sd):
    prob_density = np.exp(-0.5*((x-mean)/sd)**2) / np.sqrt(np.pi * sd**2)
    return prob_density
 
mean1 = st.slider(label='input mean', min_value=-5., max_value=5., value=4.)
sd1 = st.slider(label='input std dev', min_value=0.1, max_value=5., value=4.)
 
pdf1 = normal_dist(x,mean1,sd1)

fig1, ax1 = plt.subplots()
plt.plot(x, pdf1 , color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
st.pyplot(fig1)

#x = np.linspace(-10,10,100)
 
mean2 = st.slider(label='input mean', min_value=-5., max_value=5., value=4.)
sd2 = st.slider(label='input std dev', min_value=0.1, max_value=5., value=4.)
 
pdf2 = normal_dist(x,mean2,sd2)

fig2, ax2 = plt.subplots()
plt.plot(x, pdf2, color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
st.pyplot(fig2)

#x = np.linspace(-10,10,100)
  
mean3 = st.slider(label='input mean', min_value=-5., max_value=5., value=4.)
sd3 = st.slider(label='input std dev', min_value=0.1, max_value=5., value=4.)
 
pdf3 = normal_dist(x,mean3,sd3)

fig3, ax3 = plt.subplots()
plt.plot(x, pdf3, color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
st.pyplot(fig3)