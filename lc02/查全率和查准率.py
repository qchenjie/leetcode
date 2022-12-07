from sklearn import metrics

y = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
y_hat = [0, 0, 0, 0, 1, 1, 0, 0, 1, 1]

print('accuracy=', metrics.accuracy_score(y, y_hat))
print('precision=', metrics.precision_score(y, y_hat))
print('recall=', metrics.recall_score(y, y_hat))
print('f1_score=', metrics.f1_score(y, y_hat))
