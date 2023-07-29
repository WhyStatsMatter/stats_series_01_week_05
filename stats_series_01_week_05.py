# Snippet 1: Introduction to Sampling
import random

population = range(1, 10001)
sample_random = random.sample(population, 100) # Random Sampling

from sklearn.model_selection import train_test_split

# Stratified Sampling
X, y = population, [0 if i <= 5000 else 1 for i in population]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.1)

# Snippet 2: Sampling Distribution & Central Limit Theorem
import numpy as np

means = [np.mean(random.sample(population, 30)) for _ in range(1000)] # Sampling Distribution
plt.hist(means, bins=30)
plt.show()

# Snippet 3: Estimation: Point and Interval
import scipy.stats as stats

confidence_level = 0.95
degrees_freedom = len(sample_random) - 1
mean = np.mean(sample_random)
standard_error = stats.sem(sample_random)
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, mean, standard_error)
