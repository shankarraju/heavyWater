import pandas as pd
import numpy as np
import json
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier

vectorizerbigram= CountVectorizer(decode_error='ignore',ngram_range=(3, 3))
sgclf=SGDClassifier(loss='hinge', penalty='l2',alpha=0.001, n_iter=5, random_state=42) 
    
wordbigram=None
SG=None
Ytest=None
def intialize():
    global SG,wordbigram,vectorizerbigram,sgclf
    data = pd.read_csv("../app/test.csv", names=["Document","Words"])

    Y=data.Document
    X= data.Words

    Xtrain,Xtest,Ytrain,Ytest = train_test_split(X, Y, test_size=0.1, random_state=42)
   
    wordbigram= vectorizerbigram.fit_transform(Xtrain.values.astype('U'))
    SG = sgclf.fit(wordbigram,Ytrain) 
    #wordbigram.shape
    #test starts here
    return 

def predictionResult(testVal):
    global SG,vectorizerbigram
  
    testDat=StringIO(testVal)
    testDat2=pd.read_csv(testDat)
    wordTest_bigram =vectorizerbigram.transform(testDat2)
    
    #wordTest_bigram.shape

   
    predictedSG = SG.predict(wordTest_bigram)
    #accuracy=np.mean(predictedSG == Ytest)
    
    result=json.dumps(predictedSG.tolist())
    return result.replace('\"','')

