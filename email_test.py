# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:22:55 2016

@author: Mohammad
"""

#==============================================================================
#   The function get unprocessed email text, removes the header and returns 
#   only the body of the email for further processing.
#==============================================================================
#import numpy as np 
#import itertools

def get_email_text(filename):
# Import the email modules we'll need
    from email.parser import Parser
    import email
    parser = Parser()
    
    
    file = open(filename, 'r', encoding='ISO-8859-1')
    
    emailText =  file.read()
    
    email = parser.parsestr(emailText)
    
    
#    Getting the fields of email. Commented out.
    #print(email.get('From'))
    #print(email.get('To'))
    #print(email.get('Subject'))
    
#   Getting the body of the email
    textlist = []
    if email.is_multipart():
        for part in email.get_payload():
            textlist.extend(email.get_payload())
            text = [items.as_string() for items in textlist]
            email_text = '\n'.join(text)
            
    else:
        email_text = email.get_payload()
    
    file.close()    
    return email_text
    
    
    
    
    
    
#==============================================================================
#   The function below takes an email file and looks for matches in a spam
#    vocabulary and returns a feature vector of the matches. The vocabulary
#    file can be changed foe later use.
#==============================================================================    
    
def process_email(filename):
        
    import re
    import numpy as np
    import pandas as pd
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer() 
    #==============================================================================
    #   Process email function
    #==============================================================================
    email_pattern = r'[A-Z0-9._%+-]+@[A-Z0-9._%+-]+\.[A-Z]{2,4}'
    email_regex = re.compile(email_pattern, flags = re.IGNORECASE)
    #url_pattern = r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?'
    url_pattern = r'(http|https)://[^\s]*'
    url_regex = re.compile(url_pattern, flags = re.IGNORECASE)
    
    number_pattern = r'[0-9]+'
    number_regex = re.compile(number_pattern)
    
    dollar_pattern = r'[$]+'
    dollar_regex = re.compile(dollar_pattern)
    
    http_pattern = r'<[^<>]+>'
    http_regex = re.compile(http_pattern)
    
    nonword_pattern = r'[^a-zA-Z0-9]'
    nonword_regex = re.compile(nonword_pattern)
    
    email_list = []
    
    # Get the body of the email
    line = get_email_text(filename)
    
    # process the body of the email.
    line = line.lower()
    line = http_regex.sub(' ',line)
    line = email_regex.sub('emailaddr',line)
    line = url_regex.sub('httpaddr',line)
    line = number_regex.sub('number',line)
    line = dollar_regex.sub('dollar',line)
    line = nonword_regex.sub(' ',line)
    listline = line.split()    
    newline = []
    for word in listline:
        word = word.strip()
        word = stemmer.stem(word)
        newline.append(word)

#   print(line)    
    email_list.extend(newline)
#   print(email_list)    
    vocab_filename = '../vocab.txt' 
    b = pd.read_table(vocab_filename, header = None)
    vocab = pd.DataFrame(b) 
    vocab = pd.Series(vocab[1])
    
    invocab = np.array(vocab[vocab.isin(email_list)].index)
#   print(invocab)
    x = np.zeros(len(vocab))
    x[invocab] = 1
    
    # Sanity checks
#    print(invocab.shape)
#    print(x.shape)
#    print(x[x==1].shape)
    return x    