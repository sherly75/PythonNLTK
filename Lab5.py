def total(tp,fp,fn,tn):
    return tp+fp+fn+tn

def acc(tp,fp,fn,tn):
    return (tp+tn)/(tp+fp+fn+tn)

def pres(tp,fp,fn,tn):
    return tp/(tp+fp)

def rec(tp,fp,fn,tn):
    return tp/(tp+fn)


def f1(tp,fp,fn,tn):
    pre = tp / (tp + fp)
    re = tp / (tp + fn)
    return (2*(pre*re)/(re+pre))

#asking to tp,fp,fn,tn
tp=int(input('What is the True Positive (TP) of the System?'))
fp=int(input('What is the False Positive (FP) of the System?'))
fn=int(input('What is the False Negative (FN) of the System?'))
tn=int(input('What is the True Negative (TN) of the System?'))


print('The Accuracy of System A = ',acc(tp,fp,fn,tn))
print('The Precision of System A = ',pres(tp,fp,fn,tn))
print('The Recall of System A = ',rec(tp,fp,fn,tn))
print('The F1-Measure of System A = ',f1(tp,fp,fn,tn))