import numpy as np 


def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """ calculate SVD from 2x2 matrix using Jacobi method

    Args:
        A (np.ndarray): input 2x2 matrix

    Returns:
        tuple: SVD components (U, Sigma, Vh)
    """
    ATA = A.T @ A
    AAT = A @ A.T
    vh = np.identity(ATA.shape[0])
    u = np.identity(AAT.shape[0])
    iter = 5

    for _ in range(iter):
        theta = 0.5 * np.arctan2(2 * ATA[0,1], ATA[0,0] - ATA[1,1])
        J = np.array([[np.cos(theta), -np.sin(theta)], 
                    [np.sin(theta), np.cos(theta)]])
        ATA = J.T @ ATA @ J
        vh = J @ vh
        
        theta_u = 0.5 * np.arctan2(2 * AAT[0,1], AAT[0,0] - AAT[1,1])
        J_u = np.array([[np.cos(theta_u), -np.sin(theta_u)], 
                    [np.sin(theta_u), np.cos(theta_u)]])
        AAT = J_u.T @ AAT @ J_u
        u = J_u @ u
    
    sigma = np.sqrt(np.diag(ATA))

    for i in range(len(sigma)):
        if sigma[i] < 0:
            sigma[i] = -sigma[i]
            u[:, i] = -u[:, i]

    SVD = (u, sigma, vh)
    
    return SVD


test = svd_2x2_singular_values(np.array([[1, 2], [3, 4]]))

svd = np.linalg.svd(np.array([[1, 2], [3, 4]]))
print(svd)
print(svd.U @ [[svd.S[0], 0], [0, svd.S[1]]] @ svd.Vh)
