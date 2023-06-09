import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import scipy.stats as sct
 
x = np.linspace(-10,10,100)
 
def normal_dist(x , mean , sd):
    prob_density = np.exp(-0.5*((x-mean)/sd)**2) / np.sqrt(np.pi * sd**2)
    return prob_density
st.write("""

### Нормальное распределение
""")

mean1 = st.slider(label='Введите среднее значение', min_value=-5., max_value=5., value=4.)
sd1 = st.slider(label='Введите стандартное отклонение', min_value=0.1, max_value=5., value=4.)
 
pdf1 = normal_dist(x,mean1,sd1)

fig1, ax1 = plt.subplots()
plt.plot(x, pdf1 , color = 'blue')
plt.xlabel('Величина')
plt.ylabel('Частота')
st.pyplot(fig1)

st.write("""

### Распределение Пуассона 
""")

#x = np.linspace(-10,10,100)
k = np.arange(st.slider(label='Промасштабируйте ось Х', min_value=5, max_value=100, value=10))
lam = st.slider(label='Введите количество людей, заходящих в минуту', min_value=0, max_value=15, value=1)
mass_poi = sct.poisson(lam).pmf(k)
cumul_poi = sct.poisson(lam).cdf(k)
fig2, ax2 = plt.subplots()
plt.vlines(k, [0]*len(mass_poi), mass_poi)#, label='Probability mass function of Poi')
plt.title('Количество людей заходящих в магазин в минуту')
plt.xlabel('Количество людей')
plt.ylabel('Вероятность')
st.pyplot(fig2)

st.write("""

### Экспоненциальное распределение
Известно, что в среднем телевизор ломается  через 1 год.
""")


fig3, ax3 = plt.subplots(2, 1)
lam2 = st.slider(label='Введите начало', min_value=0, max_value=3, value=1)
lam3 = st.slider(label='Введите конец', min_value=2, max_value=5, value=3)
x1 = np.linspace(lam2, lam3, 100)

ax3[0].plot(x1, sct.expon.pdf(x1), 'r-', lw=5, alpha=0.6)
ax3[0].set_ylabel('Вероятность поломки')
ax3[0].set_title('Вероятность поломки')
ax3[1].plot(x1, sct.expon.cdf(x1), 'r-', lw=5, alpha=0.6)
#dens_exp = st.expon(lam2).pdf(x1)
#cumul_exp = st.expon(lam2).cdf(x1)
ax3[1].set_title('Накопленная вероятность')
plt.xlabel('Количество лет')
plt.ylabel('Вероятность поломки')
#plot_dens_cumul(dens_exp, cumul_exp, 'expon', x1)  



#plt.plot(x, pdf3, color = 'blue')

#plt.ylabel('Probability Density')
plt.tight_layout()
st.pyplot(fig3)