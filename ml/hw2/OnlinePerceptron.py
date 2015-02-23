
class classifier:
    
    def __init__(self):
        self.train_features = 'files/rcv1.train.features'
        self.train_labels = 'files/rcv1.train.labels'
        self.test_features = 'files/rcv1.test.features'
        self.test_labels = 'files/rcv1.test.labels'
        self.train_data = []
        self.labels_data = []
        self.terms = 47236
        # initialize w and b
        self.w = [0 for x in xrange(self.terms)]
        self.b = 0
    
    def load_train_data(self, fname):
        prev = '1'
        row = []
        with open(fname) as f:
            for line in f:
                items = line.strip().split(' ')
                rid = items[0]
                feature = [int(items[1]), float(items[2])]
                if rid != prev:
                    self.train_data.append(row)
                    row = []
                    prev = rid
                    continue
                row.append(feature)
            self.train_data.append(row)

    def load_train_labels(self, fname):
        with open(fname) as f:
            for line in f:
                self.labels_data.append(int(line.strip()))
    
    def train(self):
        error = 0
        # load data
        self.load_train_data(self.train_features)
        self.load_train_labels(self.train_labels)
        for i, x in enumerate(self.train_data):
            y = int(self.labels_data[i])
            dp = self.dot_product(x, self.w)
            if y * (self.dot_product(x, self.w) + self.b) <= 0:
                self.improve_w(self.w, y, x)
                self.b += y
                error += 1
        return error
    
    def test(self):
        error = 0
        # load data
        self.load_train_data(self.test_features)
        self.load_train_labels(self.test_labels)
        for i, x in enumerate(self.train_data):
            y = int(self.labels_data[i])
            dp = self.dot_product(x, self.w)
            if y * (self.dot_product(x, self.w) + self.b) <= 0:
                error += 1
        return error

    def improve_w(self, w, y, item):
        for x in item:
            index, data = x[0], x[1]
            w[index-1] += y*data

    def dot_product(self, a, b):
        result = 0
        for x in a: 
            index, data = x[0], x[1]
            result += data*b[index-1]
        return result


c = classifier()
print c.train()
print c.test()
#print len(c.train_data), len(c.labels_data)
#print c.train_data[1]
#print c.train_data[-1]
#
