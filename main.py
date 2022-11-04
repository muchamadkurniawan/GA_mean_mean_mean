#ini adalah program GA kmean, GAmean kmean
import pandas as pd
import numpy as np
from kmeans import class_kmeans
from my_kmeans import myKmeans
from DatasetPublic import class_dataset
from GAfile import GA
from objectiveFile import step
from GA_Polygamy import GAPoly
#
# def readDataExcel():
#     file = pd.read_excel(open('borneo.xlsx', 'rb'))
#     dframe = pd.DataFrame(file, columns=(['x', 'y']))
#     return np.array(dframe)

if __name__ == '__main__':
    # # dataset iris
    # dataset = class_dataset()
    # dataset.irisDataset()
    # baris,dim =dataset.X.shape
    # nCluster = 3

    # # dataset wine
    # dataset = class_dataset()
    # dataset.wineDataset()
    # baris, dim = dataset.X.shape
    # nCluster = 2

    # # dataset wine
    # dataset = class_dataset()
    # dataset.breast_cancerDataset()
    # baris, dim = dataset.X.shape
    # nCluster = 2

    # dataset diabetes
    # - irisDataset
    # - wineDataset
    # - breast_cancerDataset
    # - diabetesDataset
    # - artificialDataset
    # - artificialDataset3D
    # - dataset_MobilePhone

    dataset = class_dataset()
    dataset.artificialDataset()
    baris, dim = dataset.X.shape
    nCluster = len(set(dataset.y))
    print("n cluster: ", nCluster)

    #GA
    nPop = 30
    Cr = 0.7
    maxloop = 100
    Mr = 0.2
    objektif = step()

    # print("tes 2 dimension ", arr_2d)

    # TESTING MY K-MEANS
    # objCluster = myKmeans(dataset.X, nCluster, bestGA)
    # objCluster.printout()

    print("===================")
    print("GA INIT - KEANS")
    sse = []
    sil = []
    davies = []
    v = []
    lope = []
    for i in range(5):
        obj = GA(nPop, nCluster, dim, maxloop, Cr, Mr, dataset.X, dataset.y, objektif)
        bestGA = obj.bestInd
        arr = np.array(bestGA)
        arr_2d = np.reshape(arr, (nCluster, len(dataset.X[0])))
        obj_kmeans = class_kmeans(dataset.X,dataset.y, nCluster, initCentroid=arr_2d)
        sse.append(obj_kmeans.get_SSE())
        sil.append(obj_kmeans.get_silhouette())
        davies.append(obj_kmeans.get_davies_bouldin())
        v.append(obj_kmeans.get_V_measure())
        lope.append(obj_kmeans.maxloop)
        # obj_kmeans.get_centroids()
    print("SSE          : ", sse)
    print("Silhoutte    : ", sil)
    print("davies       : ", davies)
    print("V measure    : ", v)
    print("maxloop      : ",lope)
    print("===================")

    print()
    print("K- means")
    sse = []
    sil = []
    davies = []
    v = []
    lope = []
    for i in range(5):
        initCentroids = []
        obj_kmeans1 = class_kmeans(dataset.X,dataset.y, nCluster, initCentroid=initCentroids)
        sse.append(obj_kmeans1.get_SSE())
        sil.append(obj_kmeans1.get_silhouette())
        davies.append(obj_kmeans1.get_davies_bouldin())
        v.append(obj_kmeans1.get_V_measure())
        lope.append(obj_kmeans1.maxloop)
        # obj_kmeans1.get_centroids()
    print("SSE          : ", sse)
    print("Silhoutte    : ", sil)
    print("davies       : ", davies)
    print("V measure    : ", v)
    print("maxloop      : ", lope)
    print()
    print("===================")
    print("GA Poly INIT KMEANS")
    sse = []
    sil = []
    davies = []
    v = []
    lope = []
    for i in range(5):
        nmate = 4
        obj1 = GAPoly(
            nmate,nPop, nCluster, dim, maxloop, Cr, Mr, dataset.X, dataset.y , objektif)
        bestGApoly = obj1.bestInd
        arr1 = np.array(bestGApoly)
        arr_2d1 = np.reshape(arr1, (nCluster, len(dataset.X[0])))
        obj_kmeans2 = class_kmeans(dataset.X, dataset.y, nCluster, initCentroid=arr_2d1)
        sse.append(obj_kmeans2.get_SSE())
        sil.append(obj_kmeans2.get_silhouette())
        davies.append(obj_kmeans2.get_davies_bouldin())
        v.append(obj_kmeans2.get_V_measure())
        lope.append(obj_kmeans2.maxloop)
    print("SSE          : ", sse)
    print("Silhoutte    : ", sil)
    print("davies       : ", davies)
    print("V measure    : ", v)
    print("maxloop      : ", lope)
    print("===================")
