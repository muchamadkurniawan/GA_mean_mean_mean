import math
import numpy as np

class myKmeans:
    data = []
    nCluster = 0
    centroid = []
    jarak = []
    index = []
    error = 0

    def __init__(self, data, ncluster, centroid):
        self.data = data
        self.nCluster = ncluster
        self.centroid = centroid
        self.transform1d()
        self.Algoritma()


    def printout(self):
        print("centroid ", self.centroid)

    def Algoritma(self):
        errorLama = -1
        errorBaru = 0

        while errorLama != errorBaru:
            errorLama = errorBaru
        self.getAllJarak()
        self.getAnggota()
        print(self.index)

    def getIndexMin(self,data):
        n=len(data)
        index=0
        min=data[0]
        for i in range (1,n):
            if min>data[i]:
                index=i
                min=data[i]
        return index

    def getAnggota(self):
        n = len(self.data)
        x = self.jarak
        ind = []
        for i in range (n):
            ind.append(self.getIndexMin(x[i]))
        self.index = ind

    def transform1d(self):
        arr = np.array(self.centroid)
        baris = len(self.data[0])
        kolom = self.nCluster
        # print("baris kolom in transfor1d ",baris, kolom)
        arr_2d = np.reshape(arr, (kolom, baris))
        self.centroid = arr_2d

    def getAllJarak(self):
        n = len(self.data)
        dist = []
        for i in range(n):
            dist.append(self.getJarakSatuDataToCentroids(i))
        self.jarak = dist
        # print("getALLJARAK:Jarak:", self.jarak)

    def jarak(self,data1,data2):
        # print("def jarak: print data1", data1)
        # print("def jarak: print data2", data2)
        n = len(data1)
        total=0
        for i in range(0,n):
            total = total + math.pow(data1[i]-data2[i],2)
        return math.sqrt(total)

    def getJarakSatuDataToCentroids(self,index):
        n = self.nCluster
        # print("def getjaraksatudata:centroid:", self.centroid[0])
        # print("def getjaraksatudata:data:", self.data[index])
        dist = []
        for i in range(n):
            jarak = self.jarak(self.data[index],self.centroid[i])
            dist.append(jarak)
        return dist

