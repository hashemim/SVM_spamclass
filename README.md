This file provides an explanation about the purpose of the repository and the included files. The repository includes files required for an implementation of a spam classification using a linear support vector machine. 

## Feature Extraction
"data_prep.py", "email_test.py", and "feature_extraction.py" provides functions that get an email message, remove the header, and parse its text using regular expressions. Then by looking up the words in the email with a vocabulary that is provided in "vocab.txt" one can assign a vector to each email. Note that when sved on a local host some paths may need to be modified before use. "vocab.txt" is the vocabulary that was used for feature extraction.

## Extracted Data
Two files "z_test.npy" and "z_train.npy" include data extracted from different emails for classification. 

## Classification
"Spam_SVClassifier" uses a linear support vector machine model to train the data extracted from emails and make a model. The model is then used on the test set for validation.







The sample emails were obtained from spamassassin project.
