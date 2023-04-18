import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import scipy.stats as sct
 
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
k = np.arange(11)
lam = 3#st.slider(label='input lam', min_value=-5., max_value=5., value=4.)
mass_poi = sct.poisson(lam).pmf(k)
cumul_poi = sct.poisson(lam).cdf(k)
fig2, ax2 = plt.subplots()
plt.vlines(k, [0]*len(mass_poi), mass_poi)#, label='Probability mass function of Poi')
plt.title('Количество людей заходящих в магазин в минуту')
plt.xlabel('Количество людей')
plt.ylabel('Вероятность')
st.pyplot(fig2)
#mean2 = st.slider(label='input mean', min_value=-5., max_value=5., value=4.)
#sd2 = st.slider(label='input std dev', min_value=0.1, max_value=5., value=4.)
 
#pdf2 = normal_dist(x,mean2,sd2)


#plt.plot(x, pdf2, color = 'blue')
#plt.xlabel('Data points')
#plt.ylabel('Probability Density')


#x = np.linspace(-10,10,100)
  
mean3 = st.slider(label='input mean', min_value=-5., max_value=5., value=4.)
sd3 = st.slider(label='input std dev', min_value=0.1, max_value=5., value=4.)
 
pdf3 = normal_dist(x,mean3,sd3)

fig3, ax3 = plt.subplots()
plt.plot(x, pdf3, color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
st.pyplot(fig3)