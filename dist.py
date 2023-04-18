import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
x = np.linspace(-10,10,100)
 
def normal_dist(x , mean , sd):
    prob_density = np.exp(-0.5*((x-mean)/sd)**2) / np.sqrt(np.pi * sd**2)
    return prob_density
 
mean = st.slider(label='input mean', min_value=-5., max_value=5., value=4.)
sd = st.slider(label='input std dev', min_value=0.1, max_value=5., value=4.)
 
pdf = normal_dist(x,mean,sd)

fig1, ax1 = plt.subplots()
plt.plot(x, pdf , color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
st.pyplot(fig1)

x = np.linspace(-10,10,100)
 
def normal_dist(x , mean , sd):
    prob_density = np.exp(-0.5*((x-mean)/sd)**2) / np.sqrt(np.pi * sd**2)
    return prob_density
 
mean = st.slider(label='input mean', min_value=-5., max_value=5., value=4.)
sd = st.slider(label='input std dev', min_value=0.1, max_value=5., value=4.)
 
pdf = normal_dist(x,mean,sd)

fig2, ax2 = plt.subplots()
plt.plot(x, pdf , color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
st.pyplot(fig2)

x = np.linspace(-10,10,100)
 
def normal_dist(x , mean , sd):
    prob_density = np.exp(-0.5*((x-mean)/sd)**2) / np.sqrt(np.pi * sd**2)
    return prob_density
 
mean = st.slider(label='input mean', min_value=-5., max_value=5., value=4.)
sd = st.slider(label='input std dev', min_value=0.1, max_value=5., value=4.)
 
pdf = normal_dist(x,mean,sd)

fig3, ax3 = plt.subplots()
plt.plot(x, pdf , color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
st.pyplot(fig3)