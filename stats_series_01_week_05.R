# Snippet 1: Introduction to Sampling
population <- 1:10000
sample_random <- sample(population, 100) # Random Sampling

library(caret)

# Stratified Sampling
y <- ifelse(population <= 5000, 0, 1)
stratified_sample <- createDataPartition(y, times = 1, p = 0.1, list = FALSE)

# Snippet 2: Sampling Distribution & Central Limit Theorem
means <- replicate(1000, mean(sample(population, 30))) # Sampling Distribution
hist(means, breaks=30)

# Snippet 3: Estimation: Point and Interval
confidence_level <- 0.95
mean <- mean(sample_random)
standard_error <- sd(sample_random) / sqrt(length(sample_random))
confidence_interval <- qt(confidence_level, df=length(sample_random)-1) * standard_error
CI_lower <- mean - confidence_interval
CI_upper <- mean + confidence_interval
