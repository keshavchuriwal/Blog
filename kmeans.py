# Sample dataset
X = [[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]]

# Initial data points for K-Means clustering
init_points = [[2, 2], [3, 2], [2, 3]]

# Number of clusters
k = 3

# Calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return sum([(a - b) ** 2 for a, b in zip(x1, x2)]) ** 0.5

# Initialize centroids with initial data points
centroids = init_points.copy()

# Loop until convergence
while True:
    # Assign each data point to the nearest centroid
    clusters = [[] for _ in range(k)]
    for x in X:
        distances = [euclidean_distance(x, c) for c in centroids]
        nearest_cluster_idx = distances.index(min(distances))
        clusters[nearest_cluster_idx].append(x)

    # Calculate new centroids as the mean of each cluster
    new_centroids = []
    for i in range(k):
       cluster_mean = [sum(col)/len(col) for col in zip(*clusters[i])]
       new_centroids.append(cluster_mean)

    # Check for convergence
    if new_centroids == centroids:
        break
    else:
        centroids = new_centroids.copy()

# Assign final labels to each data point
labels = []
for x in X:
    distances = [euclidean_distance(x, c) for c in centroids]
    nearest_cluster_idx = distances.index(min(distances))
    labels.append(nearest_cluster_idx)

# Print the centroids and labels
print("Final centroids:")
print(centroids)
print("\nLabels:")
print(labels)