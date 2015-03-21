
labelFile = open("data/cover.labels","r+")
labels = labelFile.readlines()
labelFile.close()

pFile = open("svm_predictions","r+")
pText = pFile.readlines()
pFile.close()
predictions = [float(p) for p in pText]

tp = 0
fp = 0
tn = 0
fn = 0
b = 0.53

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
print acc
