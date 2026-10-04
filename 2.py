import numpy as np, matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

x = np.array([1, 2, 2.5, 3, 4, 4.2, 5])      # выборка
t = np.linspace(x.min(), x.max(), 500)         # точки для построения
plt.plot(t, gaussian_kde(x)(t)); plt.show()    # KDE и график