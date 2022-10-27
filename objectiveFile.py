import math

class step:
    def fitness(self, x):
        print("xxxxxx fitness ", x)
        bar, kol = x.shape
        sod = 0
        for i in range(bar):
            for j in range(bar):
                dis = 0
                dis = dis + self.__calDistEuclid(x[i], x[j])
            #     print("dis", dis)
            # print("----")
            sod = sod + dis
        # print("sod :", sod)
        return sod

    def fitness2(self, centroid, x):
        # print("centroid :", centroid)
        # print("xxx :", x)
        n, m = x.shape
        # print(n, m)
        distMin = []
        index = []
        for i in range(n):
            dist, ind = self.calData2Centroids(
                centroid, x[i])
            distMin.append(dist)
            index.append(ind)
        # print("dissss minnnn :", distMin)
        # print("0000000 : ", sum(distMin))
        return sum(distMin)
    def calDistance(self, centroid, data):
        n = centroid.size
        dis = 0
        for i in range(n):
            dis = dis+math.pow(centroid[i]-data[i], 2)
        return math.sqrt(dis)
    def calData2Centroids(self, centroids, data):
        n, m = centroids.shape
        minimal = self.calDistance(centroids[0], data)
        indMin = 0
        for i in range(n):
            minimal1 = self.calDistance(centroids[i], data)
            if minimal1 < minimal:
                minimal = minimal1
                indMin = i
        return minimal, indMin
    def __calDistEuclid(self, x1, x2):
        # print("x1 :",x1)
        # print("x2 :",x2)
        n = len(x1)
        tot = 0
        for i in range (n):
            # euclid
            tot = tot + (math.pow((x1[i] - x2[i]),2))
        return math.sqrt(tot)
