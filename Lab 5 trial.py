tp=3
fp=2
fn=1
tn=12
total=tp+tn+fp+fn
acc=(tp+tn)/total
pres=tp/(tp+fp)
rec=tp/(tp+fn)
f1=(2*(pres*rec)/(rec+pres))
print('System A: Tom and Jerry was the best cartoon on in Paris. No one watched more than Joe and Bob')
print('The Accuracy of System A = ',acc)
print('The Precision of System A = ',pres)
print('The Recall of System A = ',rec)
print('The F1-Measure of System A = ',f1)