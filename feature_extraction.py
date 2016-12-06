# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:56:15 2016

@author: M Hashemi
This function extracts the features from many emails and produce a feature 
matrix from them. The matrix is set to be later used by a classification
algorithm
"""

""" 
YOU CAN EMAIL TEXT FIELS FOR PARSING FROME ONLINE RESOUECES INCLUDING
http://spamassassin.apache.org, or parse you own emails! 

"""
import os
import email_test
import numpy as np

process_email = email_test.process_email
get_email_text = email_test.get_email_text

feature_vectors = []

indir = "/Users/mohammadhashemi/Documents/SVM_SpamClassification/spam"

os.chdir(indir)
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
            print(f)
            feat_vec = email_test.process_email(f)
            print(feat_vec.shape)
            feature_vectors.append(feat_vec)
            
features = np.array(feature_vectors)

os.chdir('../')

#np.save('features_spam',features)