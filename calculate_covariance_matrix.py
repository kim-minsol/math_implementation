def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    """a function which calculates covariance matrix

    Args:
        vectors (list[list[float]]): a list of vectors which is an input

    Returns:
        list[list[float]]: a covariance matrix of input vectors
                           It has N x N shape. (N is num of features)
    """
    len_ = len(vectors)
    N = len(vectors[0])
    covariance_matrix = [[0]*len_ for i in range(len_)]
    for i in range(len_):
        for j in range(len_):
            # calculate mean
            mean1 = sum(vectors[i]) / N
            mean2 = sum(vectors[j]) / N
            
            # calculate cov
            residual_sum = 0
            for idx in range(N):
                residual_sum += abs(vectors[i][idx] - mean1) * abs(vectors[j][idx] - mean2)
            cov = residual_sum / (N - 1)

            # update cov
            covariance_matrix[i][j] = cov
        
    return covariance_matrix

print(calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]])) # [[1.0, 1.0], [1.0, 1.0]]
print(calculate_covariance_matrix([[1, 5, 6], [2, 3, 4], [7, 8, 9]])) # [[7.0, 2.5, 2.5], [2.5, 1.0, 1.0], [2.5, 1.0, 1.0]]
