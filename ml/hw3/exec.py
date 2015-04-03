import os
for i in xrange(1, 17):
    os.system('./svm_classify data/cover.test learn.model%s predictions%s0' % (i,i))


