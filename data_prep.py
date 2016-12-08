# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:27:40 2016

"""
import numpy as np

X_spam = np.load('features_spam.npy')
y_spam = np.ones_like(X_spam[:,1])
y_spam.resize(len(y_spam),1)
z_spam = np.hstack((y_spam,X_spam))
np.random.shuffle(z_spam)

para1 = int(z_spam.shape[0]/3)
 
 
X_easy = np.load('features_easy_ham.npy')
y_easy = np.zeros_like(X_easy[:,1])
y_easy.resize(len(y_easy),1)
z_easy = np.hstack((y_easy,X_easy)) 


X_hard = np.load('features_hard_ham.npy')
y_hard = np.zeros_like(X_hard[:,1])
y_hard.resize(len(y_hard),1)
z_hard = np.hstack((y_hard,X_hard))

z_neg = np.vstack((z_easy,z_hard))
np.random.shuffle(z_neg)
para2 = para1*2
para3 = para1*6
z_test = np.vstack((z_spam[:para1,:], z_neg[:para2,:]))
z_train = np.vstack((z_spam[para1:,:],z_neg[para2:para3,:]))
np.random.shuffle(z_test)
np.random.shuffle(z_train)

np.save('z_test',z_test)
np.save('z_train',z_train)
