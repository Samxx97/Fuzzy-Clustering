import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import numpy as np


def draw_contours(X, U, centers, cov, pnt_colors, center_color, title = None):
    cluster_indices = np.argmax(U, axis=1)

    cluster_groups = []
    cluster_cov = []

    x1 = np.linspace(-2, 10, 200)
    x2 = np.linspace(-2, 10, 200)

    M, N = np.meshgrid(x1, x2)

    pos = np.empty(M.shape + (2,))
    pos[:, :, 0] = M
    pos[:, :, 1] = N

    for i in range(centers.shape[0]):

        cluster_groups.append(X[cluster_indices == i, :])
        # in case no covariance matrix was given (which is the case for Fuzzy c mean)
        if cov is None:
            cluster_cov.append(np.identity(centers.shape[1]))

        else:
            cluster_cov.append(cov[i])

    plt.figure(figsize=(17, 10))
    plt.title(title)

    for i in range(centers.shape[0]):
        plt.scatter(cluster_groups[i][:, 0], cluster_groups[i][:, 1], color=pnt_colors[i], marker='o')
        plt.plot(centers[i, 0], centers[i, 1], color=center_color, marker='x', linewidth=7, markersize=19)
        plt.contour(M, N, multivariate_normal(centers[i], cluster_cov[i]).pdf(pos), colors=pnt_colors[i], alpha=0.5)

    plt.grid()
    plt.show()

def segment_image(im,labels,center,verbose):
    n = len(np.unique(labels))
    f_img = np.zeros_like(im,dtype=np.int64)
    segs = list(np.unique(labels))
    for i in range(n):
        if verbose:
            print(i)
        mask_indx = np.where((labels==segs[i]))
        mask = np.zeros_like(im[:,:,0],dtype=np.int64)
        mask[mask_indx] = 1
        f_img[:,:,0] += mask * int(center[segs[i],0] * 256)
        f_img[:,:,1] += mask * int(center[segs[i],1] * 256)
        f_img[:,:,2] += mask * int(center[segs[i],2] * 256)
    return f_img

