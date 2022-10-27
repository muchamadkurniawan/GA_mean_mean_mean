from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics.cluster import v_measure_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score

class class_kmeans:
    X = []
    y = []
    init_centroids = []
    nCluster = 0
    y_pred = []
    centroids = []
    SSE = []

    def __init__(self, X,y, ncluster, initCentroid =None):
        self.X = X
        self.y = y
        self.nCluster = ncluster
        self.init_centroids = initCentroid
        self.clustering()

    def clustering(self):
        # print(len(self.init_centroids))
        if len(self.init_centroids) == 0:
            kmeans = KMeans(n_clusters=self.nCluster,
                            random_state=0,
                            n_init=1,
                            max_iter=50,
                            verbose=2,
                            init='random').fit(self.X)
            print("Kmeans non Init")
        else:
            print("Kmeans with init")
            kmeans = KMeans(
                n_clusters=self.nCluster,
                init=self.init_centroids,
                random_state=0,
                max_iter=50,
                n_init=1,
                verbose=2).fit(self.X)
        self.y_pred = kmeans.labels_
        self.centroids = kmeans.cluster_centers_
        # print("def clustering:centroid ",self.centroids)
        self.SSE = kmeans.inertia_
        print("loop max: ",kmeans.n_iter_)

    def get_V_measure(self):
        acc = v_measure_score(self.y, self.y_pred)
        print("V Measure score  :",acc)
        return acc

    def get_SSE(self):
        print("nilai SSE        : ",self.SSE)
        return self.SSE

    def get_silhouette(self):
        z = silhouette_score(self.X, self.y_pred)
        print("Silhoutte Score  :",z)
        return z

    def get_davies_bouldin(self):
        z = davies_bouldin_score(self.X, self.y_pred)
        print("Davies Boundies  :",z)
        return z

    def get_centroids(self):
        print("centroids :", self.centroids)

