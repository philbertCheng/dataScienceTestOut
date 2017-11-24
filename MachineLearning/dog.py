import numpy as np
import matplotlib.pyplot as plt

greyhouds = 500
labs = 500

greyheight = 28 + 4 * np.random.randn(greyhouds)
labheight = 24 + 4 * np.random.randn(labs)

plt.hist([greyheight,labheight],stacked = True,color = ['r','b'])
plt.show()