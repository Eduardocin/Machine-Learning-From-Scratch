import numpy as np
from collections import Counter

# Function to calculate the Euclidean distance between two points
def euclidean_distance(x1, x2):
    # Calculate the squared differences, sum them, and take the square root
    distance = np.sqrt(np.sum((x1 - x2)**2))
    return distance


class KNN:
    def __init__(self, k=3):
        # Initialize KNN with the number of nearest neighbors, k
        self.k = k

    # Store the training data (X: features, y: labels)
    def fit(self, X, y):
        self.X_train = X  # Store the feature data of training samples
        self.y_train = y  # Store the corresponding labels of training samples

    # Predict the label for each sample in X (input: 2D array of samples)
    def predict(self, X):
        # For each sample in X, call the _predict method and return all predictions
        predictions = [self._predict(x) for x in X]
        return predictions

    # Predict the label for a single sample x
    def _predict(self, x):
        # Calculate the distance from x to every point in the training data
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # Sort the distances and get the indices of the k closest points
        k_indices = np.argsort(distances)[:self.k]

        # Get the labels of the k nearest points
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Perform a majority vote to find the most common label among the k nearest points
        most_common = Counter(k_nearest_labels).most_common()

        # Return the label with the highest vote (most common label)
        return most_common[0][0]
