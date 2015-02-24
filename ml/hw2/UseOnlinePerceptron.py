
class classifier:
    
    def __init__(self):
        self.train_features = 'files/rcv1.train.features'
        self.train_labels = 'files/rcv1.train.labels'
        self.test_features = 'files/rcv1.test.features'
        self.test_labels = 'files/rcv1.test.labels'
        self.order = 'files/training.orders'
        self.data = []
        self.labels = []
        self.t_data = []
        self.t_labels = []
        self.orders = []
        self.terms = 47236
        # initialize w and b
        self.w = [0 for x in xrange(self.terms)]
        self.b = 0
    
    def load_data(self, fname, dest):
        prev = '1'
        row = []
        with open(fname) as f:
            for line in f:
                items = line.strip().split(' ')
                rid = items[0]
                feature = [int(items[1]), float(items[2])]
                if rid != prev:
                    dest.append(row)
                    row = []
                    prev = rid
                    continue
                row.append(feature)
            dest.append(row)

    def load_labels(self, fname, dest):
        with open(fname) as f:
            for line in f:
                dest.append(int(line.strip()))

    def load_order(self):
        with open(self.order) as f:
            for line in f:
                self.orders.append([int(x) for x in line.strip().split(',')])
        
    
    def train(self, order):
        result = []
        index = 0
        for one in order:
            x = self.data[one-1]
            y = self.labels[one-1]
            if y * (self.dot_product(x, self.w) + self.b) <= 0:
                self.improve_w(self.w, y, x)
                self.b += y
            if index != 0 and index % 100 == 0:
                # do current result on training data and testing data
                result.append([float(self.test_train(self.w, self.b))/float(19242), float(self.test(self.w, self.b))/float(1000)])
            index += 1
        result.append([float(self.test_train(self.w, self.b))/float(19242), float(self.test(self.w, self.b))/float(1000)])
        print 'done'
        return result

    def test_train(self, w, b):
        error = 0
        for i, x in enumerate(self.data):
            y = int(self.labels[i])
            if y * (self.dot_product(x, w) + b) <= 0:
                error += 1
        return error

    
    def test(self, w, b):
        error = 0
        for i, x in enumerate(self.t_data):
            y = int(self.t_labels[i])
            if y * (self.dot_product(x, w) + b) <= 0:
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

    def start(self):
        result = []
        # load train data
        self.load_data(self.train_features, self.data)
        self.load_labels(self.train_labels, self.labels)
        # load testing data
        self.load_data(self.test_features, self.t_data)
        self.load_labels(self.test_labels, self.t_labels)
        # load orders
        self.load_order()
        for x in self.orders:
            result.append(self.train(x))
            self.w = [0 for x in xrange(self.terms)]
            self.b = 0
        print result

print '---- start ----'
c = classifier()
c.start()
#print c.test(c.w, c.b)
#print c.test_train(c.w, c.b)
#print len(c.train_data), len(c.labels_data)
#print c.train_data[1]
#print c.train_data[-1]
#
