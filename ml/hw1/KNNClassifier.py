import heapq
import math
import numpy as np
import time

class distanceCluster:
    def __init__(self, distance, cluster):
        self.distance = distance
        self.cluster = cluster
    
    def __lt__(self, other):
        # turn to Max heap
        return self.distance < other.distance

class classifier:

    def __init__(self, k, train, test):
        self.k = k
        self.train = train
        self.test  = test
        self.file_arr = self.load_file(train)
        self.result = self.knn()

    def setK(self, k):
        self.k = k
        
    def distance(self, a, b):
        a = np.array(a)
        b = np.array(b)
        return np.linalg.norm(a-b)

    def load_file(self, filename):
        file_arr = []
        with open(filename) as f:
            for line in f:
                line_arr = self.separate_line(line.strip())
                file_arr.append(line_arr)
        return file_arr
    
    def extract_top(self, src, k):
        top = []
        heapq.heapify(src)
        while k > 0:
            top.append(heapq.heappop(src))
            k -= 1
        return top

    def separate_line(self, line):
        ## NOTE split and then convert to float
        return [float(x) for x in line.split(' ')]

    def knn(self):
        result = []
        train_list = self.load_file(self.train)
        test_list  = self.load_file(self.test)
        i = 0
        for te in test_list:
            i += 1
            ds = []
            for tr in train_list:
                d = self.distance(te[1:], tr[1:])
                ds.append(distanceCluster(d, tr[0]))
            result.append([te[0], self.extract_top(ds, self.k)])
        return result


    def get(self, k):
        total = 0
        error = 0
        for one in self.result:
            total += 1
            cluster = one[0]
            knn = one[1]
            predicted = self.maximum_occur(knn[0: k])
            if predicted != cluster:
                error += 1
        print error, total
        print float(error)/float(total)

    def maximum_occur(self, src):
        maximum = 0
        result = 0
        clusters = dict()
        for x in src:
            knncluster = x.cluster
            if knncluster not in clusters:
                clusters[knncluster] = 1
            else:
                clusters[knncluster] += 1
        for k in clusters:
            if clusters[k] > maximum:
                maximum = clusters[k]
                result = k
        return result
        

# -------- run classifier ---------
current_milli_time = lambda: int(round(time.time() * 1000))
start = current_milli_time()
classifier = classifier(25, 'zip.train', 'zip.test')
for i in xrange(1, 26, 2):
    print i
    classifier.get(i)
print 'time: ', current_milli_time() - start
