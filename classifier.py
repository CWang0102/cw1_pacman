# classifier.py
# Lin Li/26-dec-2021
#
# Use the skeleton below for the classifier and insert your code here.

import numpy as np
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
#clf represents classifier

class Classifier:

    def __init__(self):
        pass

    def reset(self):
        pass
    
    def fit(self, data, target):
        clf.fit(data, target)

    def predict(self, data, legal=None):
        arr = np.array(data)
        states = arr.reshape(1,-1)
        p_outcone = clf.predict(states)
        print(p_outcone)
        return p_outcone
        # if legal is not None and p_outcone in legal:
        #     return p_outcone
        # elif legal is not None and p_outcone not in legal:
        #     return 1
        # else:
        #     return p_outcone
