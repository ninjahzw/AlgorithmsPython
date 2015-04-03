#!/usr/bin/python
import os

#Vector of bias values to test:
bValues = [ -1 + .01 * x for x in range(0,201)]

labelFile = open("data/cover.labels","r+")
labels = labelFile.readlines()
labelFile.close()

pFile = open("svm_predictions","r+")
pText = pFile.readlines()
pFile.close()
predictions = [float(p) for p in pText] 

rocCurve = [[1,1]]
bestB = bValues[0];
accuracy = 0;
for b in bValues:
    pFile = open("svm_predictions","r+")
    predictions = pFile.readlines()
    pFile.close()
    
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    
    for i in range(0,len(predictions)):
        pLabel = labels[i][0] != '-';
        pPredict = float(predictions[i]) - b > 0
        if pLabel:
            if pPredict:
                tp +=1
            else:
                fn +=1
        else:
            if pPredict:
                fp +=1
            else:
                tn +=1
    acc = float(tp+tn)/(tp+tn+fp+fn)
    if acc > accuracy:
        accuracy = acc
        bestB = b
    rocCurve.append([float(fp)/(fp+tn), float(tp)/(tp+fn)])
rocCurve.append([0,0])

G = 0
lastPoint = rocCurve[0]
for point in rocCurve[1:]:
    G -= (point[0] - lastPoint[0]) * (point[1] + lastPoint[1])
    lastPoint = point

auc = G/2

print "\nMost accurate threshold: " + str(bestB)
print "Accuracy: " + str(accuracy)
print "AUC: " + str(auc) +"\n"
out = file("roc.points", "w+")
for point in rocCurve[1:-1]:
    out.write(' '.join(map(str,point)) + '\n')
out.close()
