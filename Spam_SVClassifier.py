# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:23:49 2016

"""
import numpy as np
"""
#==============================================================================
#   This code is to implement of spam classification code using an LinearSVC 
#   model of the scikit-learn library. The code is similar to the code 
#   provided for the MATLAB but everything is written in Python instead.
#==============================================================================
"""
# LOADING THE TRAINING DATA AND TEST DATA
z_train = np.load('z_train.npy')
z_test = np.load('z_test.npy')

# PREPARE THE TRAINING DATA AND TEST DATA FOR THE MODEL
X = z_train[:,1:]
y = z_train[:,0]
Xtest = z_test[:,1:]
ytest = z_test[:,0]

from sklearn import svm
# SETTING THE PARAMETERS OF THE MODEL
# PLAY WITH THE PENALY COST (C) TO AVOID OVERFITTING.  
clf = svm.LinearSVC(C=0.03) 
clf.fit(X,y)     # FITTING THE MODEL
print(clf.score(X, y, sample_weight = None))
print(clf.score(Xtest, ytest, sample_weight = None))
