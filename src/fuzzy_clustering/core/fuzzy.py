import numpy as np

def FCM(X, c=3, m=2, epsi=0.001):
    # number of samples
    n = X.shape[0]
    # number of features per sample
    f = X.shape[1]

    # generate random membership matrix
    U0 = np.random.rand(n, c)

    # this step is to make the membership values across each cluseter equal to 1
    U0 = U0 / U0.sum(axis=1)[:, None]

    U_current, U_prev = U0, U0

    k = 0

    while (True):

        # calculate centroids
        # multiply each point x from X matrix with its membership value u from U and
        # sum the results over all points for each center

        C = (((U_prev ** m).T[:, :, None]) * X).sum(axis=1)

        # divide each centroid by the sum of membership values of points belonging to that centroid
        C = C / (((U_prev ** m).T).sum(axis=1)[:, None])

        # calculate the membership matrix

        X_C = (((X[:, None, :] - C[None, :, :]) ** 2).sum(axis=2)) ** 0.5

        U_current = X_C[:, :, None] * ((1 / X_C)[:, None, :])

        U_current = (U_current ** (2 / (m - 1))).sum(axis=2)

        U_current = 1 / U_current

        if (np.abs(U_current - U_prev)).max(axis=(0, 1)) < epsi:
            print("K number of iterations completed: {}".format(k))
            break
        U_prev = U_current
        k += 1

    return U_current, C


def GK(X, c=3, m=2, epsi=0.001):
    n = X.shape[0]
    d = X.shape[1]

    # generate random membership matrix
    U0 = np.random.rand(n, c)

    # this step is to make the membership values across each cluster equal to 1
    U0 = U0 / U0.sum(axis=1)[:, None]

    U_current, U_prev = U0, U0

    count = 0

    V = np.zeros((c, d))

    F = np.zeros((c, d, d))

    D = np.zeros((n, c))

    while (count < 100):
        U_prev = U_current.copy()

        # vectorized way for cluster centers
        V = (((U_prev ** m).T[:, :, None]) * X).sum(axis=1)
        V = V / (((U_prev ** m).T).sum(axis=1)[:, None])

        # V = gk2.next_centers(X, U_prev.T)

        # calculate the covariance matrix for each cluster
        for j in range(c):
            numerator = np.zeros((d, d))
            for i in range(n):
                numerator += U_prev[i, j] ** m * np.outer(X[i] - V[j], X[i] - V[j])

            F[j, :, :] = numerator / (U_prev[:, j] ** m).sum()

        # calculate the mannabholis distance between every center v and every datapoint x
        for i in range(n):
            for j in range(c):
                det = np.linalg.det(F[j])
                inv_F = np.linalg.inv(F[j])

                D[i, j] = (X[i] - V[j]).T @ ((det ** (1 / d) * inv_F) @ (X[i] - V[j]))

        # calculate new membership matrix
        for i in range(n):
            for j in range(c):
                temp = 0
                for k in range(c):
                    temp += (D[i, j] / D[i, k]) ** (1 / (m - 1))

                U_current[i, j] = (1 / temp)

        if (np.abs(U_current - U_prev)).max(axis=(0, 1)) < epsi:
            print("K number of iterations completed: {}".format(count))
            break

        count += 1

    return U_current, V, F

