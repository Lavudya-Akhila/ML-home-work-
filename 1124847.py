# Given initial code word values
codebook = [[2, 2], [4, 6], [6, 5], [8, 8]]
# Data points (you can replace this with your actual data)
data_points = [[2, 5], [3, 2], [3, 3], [3, 4], [4, 3], [4, 4], [6, 3], [6, 4], [6, 6], [7, 2], [7, 5], [7, 6], [7, 7], [8, 6], [8, 7]]

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5

# Function to assign data points to the closest code word
def assign_clusters(data, codebook):
    clusters = []
    total_distance = 0
    for point in data:
        distances = [euclidean_distance(point, code) for code in codebook]
        min_distance_index = distances.index(min(distances))
        clusters.append(min_distance_index)
        total_distance += distances[min_distance_index]
    return clusters, total_distance / len(data)


# Function to update codebook values based on assigned clusters
def update_codebook(data, clusters, k):
    new_codebook = []
    for i in range(k):
        cluster_points = [point for point, cluster in zip(data, clusters) if cluster == i]
        if cluster_points:
            new_codebook.append([sum(point[j] for point in cluster_points) / len(cluster_points) for j in range(len(cluster_points[0]))])
        else:
            # If no points assigned to the cluster, keep the same code word value
            new_codebook.append(codebook[i])
    return new_codebook

# Main loop for k-means clustering
max_iterations = 5
tolerance = 1e-6
prev_avg_distance = float('inf')

for i in range(max_iterations):
    clusters, avg_distance = assign_clusters(data_points, codebook)
    codebook = update_codebook(data_points, clusters, len(codebook))
    
    print(f"Iteration: {i+1}, Average Distance: {avg_distance}")
    
    # Check convergence
    #if abs(prev_avg_distance - avg_distance) < tolerance:
    #    break
    
    prev_avg_distance = avg_distance

print("Final Codebook:")
print(codebook)
print(f"Iteration: {i+1}, Average Distance: {avg_distance}")