import numpy as np
from matplotlib import pyplot as plt
from fuzzy_clustering.core.fuzzy import FCM

def main():

    n_samples = 3000

    X = np.concatenate((
        np.random.normal((-2, -2), size=(n_samples, 2)),
        np.random.normal((2, 2), size=(n_samples, 2)),
        np.random.normal((9, 0), size=(n_samples, 2)),
        np.random.normal((5, -8), size=(n_samples, 2))
    ))

    n_clusters_list = [2, 3, 4, 5, 6, 7]
    models = list()

    for n_clusters in n_clusters_list:

        m,c = FCM(X,c = n_clusters)
        models.append((m.argmax(axis=1),c))


    num_clusters = len(n_clusters_list)
    rows = int(np.ceil(np.sqrt(num_clusters)))
    cols = int(np.ceil(num_clusters / rows))
    f, axes = plt.subplots(rows, cols, figsize=(11,16))
    for n_clusters, model, axe in zip(n_clusters_list, models, axes.ravel()):
        fcm_centers = model[1]
        fcm_labels = model[0]
        
        axe.scatter(X[:,0], X[:,1], c=fcm_labels, alpha=.1)
        axe.scatter(fcm_centers[:,0], fcm_centers[:,1], marker="+", s=500, c='black')
        axe.set_title(f'n_clusters = {n_clusters}')
        
    plt.show()    
    
    
if __name__ == "__main__":
    main()