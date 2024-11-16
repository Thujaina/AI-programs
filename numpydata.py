import numpy as np

# Sample dataset: scores of students in three subjects
data = np.array([
    [85, 90, 78],
    [88, 92, 80],
    [84, 86, 88],
    [70, 75, 65],
    [95, 89, 92]
])

# 1. Normalization: Scale the data between 0 and 1
min_vals = data.min(axis=0)
max_vals = data.max(axis=0)
normalized_data = (data - min_vals) / (max_vals - min_vals)
print("Normalized Data:\n", normalized_data)

# 2. Compute mean, median, and standard deviation for each subject
mean_values = np.mean(data, axis=0)
median_values = np.median(data, axis=0)
std_dev = np.std(data, axis=0)

print("\nMean values (per subject):", mean_values)
print("Median values (per subject):", median_values)
print("Standard Deviation (per subject):", std_dev)

# 3. Correlation Matrix: Analyze relationships between subjects
correlation_matrix = np.corrcoef(data.T)
print("\nCorrelation Matrix:\n", correlation_matrix)

# 4. Random Sampling: Generate a random sample of scores
random_sample = np.random.choice(data.flatten(), size=5, replace=False)
print("\nRandom Sample of Scores:", random_sample)


#OUTPUT

Normalized Data:
 [[ 0.6         0.88235294  0.48148148]
 [ 0.72        1.          0.55555556]
 [ 0.56        0.64705882  0.85185185]
 [ 0.          0.          0.        ]
 [ 1.          0.82352941  1.        ]]

Mean values (per subject): [ 84.4  86.4  80.6]
Median values (per subject): [ 85.  89.  80.]
Standard Deviation (per subject): [ 8.16333265  6.01996678  9.32952303]

Correlation Matrix:
 [[ 1.          0.87174181  0.88970588]
 [ 0.87174181  1.          0.68300686]
 [ 0.88970588  0.68300686  1.        ]]

Random Sample of Scores: [90 70 85 89 65]

Process finished.