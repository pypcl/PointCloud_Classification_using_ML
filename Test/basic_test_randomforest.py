# encoding=utf-8

##############################
# basic_test_randomforest.py #
##############################

from sklearn.externals import joblib
import numpy as np  
from sklearn import metrics

# load data for testing
feature_matrix = np.loadtxt('/media/shao/TOSHIBA EXT/data_object_velodyne/feature_matrix_with_label/test/r_0.16.txt')
data = feature_matrix[:, :-1]
target = feature_matrix[:, -1]

# load the trained model
rfc = joblib.load('/home/shao/文档/VSCodeWS/Masterarbeit_Code/PointCloud_Classification/Training/rf.pkl')

# prediction / test
y_pred = rfc.predict(data)
score = metrics.accuracy_score(target, y_pred)
print('accuracy score = ', score)
conf_matrix = metrics.confusion_matrix(target, y_pred, [0,1,2,3,4])
print('confusion matrix = ')
print(conf_matrix)
recall = metrics.recall_score(target, y_pred, average='weighted')
print('recall score = ', recall)
precision = metrics.precision_score(target, y_pred, average='weighted')
print('precision score = ', precision)
f1 = metrics.f1_score(target, y_pred, average='weighted')
print('f1 score = ', precision)