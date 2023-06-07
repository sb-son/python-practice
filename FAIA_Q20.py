import numpy as np

# Sample Test Case:
# import numpy as np
# X = np.array([ 9, 15, 25, 14, 10, 18,  0, 16,  5, 19, 16, 20])
# Y = np.array([39, 56, 93, 61, 50, 75, 32, 85, 42, 70, 66, 80])
# covariance(X, Y)  returns ~122.9470

def covariance(X, Y):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    total = 0

    for i in range(len(X)):
        total += (X[i] - mean_X) * (Y[i] - mean_Y)
    covariance_value = total / (len(X) - 1)
    return round(covariance_value, 3)

X = np.array([9, 15, 25, 14, 10, 18, 0, 16, 5, 19, 16, 20])
Y = np.array([39, 56, 93, 61, 50, 75, 32, 85, 42, 70, 66, 80])

print(covariance(X, Y))  # Output: ~122.9470