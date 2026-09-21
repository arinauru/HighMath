import numpy as np
import matplotlib.pyplot as plt

x, p = [4, 1, 3, 2, 2, 5, 7, 6], 0.75  # Выборка и вероятность: 0 < p <= 1
plt.ecdf(x)  # F_n(t) — доля наблюдений, не превосходящих t
print("Квантиль:", np.quantile(x, p, method="inverted_cdf"))  # Первый уровень x, где F_n(x) >= p
plt.show()  # Показать график