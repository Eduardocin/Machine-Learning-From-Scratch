import numpy as np  # Importing the NumPy library for numerical operations

class LinearRegression:

    def __init__(self, lr=0.001, n_iters=1000):
        # Initialize learning rate (lr) and the number of iterations (n_iters)
        self.lr = lr  # Learning rate for gradient descent
        self.n_iters = n_iters  # Number of iterations for the training loop
        self.weights = None  # To store weights of the model, initialized later
        self.bias = None  # To store bias term, initialized later

    def fit(self, X, y):
        # Fit the linear regression model to the data (X, y)
        n_samples, n_features = X.shape  # Get the number of samples and features from X
        self.weights = np.zeros(n_features)  # Initialize weights with zeros for each feature
        self.bias = 0  # Initialize bias as 0

        # Gradient descent loop to update weights and bias
        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias  # Predict the target using current weights and bias

            # Compute the gradients for weights and bias
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))  # Gradient of the loss w.r.t weights
            db = (1/n_samples) * np.sum(y_pred - y)  # Gradient of the loss w.r.t bias

            # Update weights and bias using the gradients and learning rate
            self.weights = self.weights - self.lr * dw  # Update weights
            self.bias = self.bias - self.lr * db  # Update bias

    def predict(self, X):
        # Predict the output for new input data X
        y_pred = np.dot(X, self.weights) + self.bias  # Calculate prediction using weights and bias
        return y_pred  # Return the predicted values
