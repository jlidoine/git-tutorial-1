import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


mu, sigma1 = 100, 15
x_gaussian = mu + sigma1 * np.random.randn(10000)

mu, sigma2 = 100, 5
x = mu + sigma2 * (np.random.randn(10,10000) ** 2).sum(0)


np.savetxt('file_data.csv', x_gaussian, delimiter=',')
np.savetxt('file2_data.csv', x, delimiter=',')