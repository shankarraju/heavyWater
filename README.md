# heavyWater mini-project - SHANKAR RAJU

This is a document classifier project for HeavyWater mini-project challenge. 
# Introduction
The data was provided by HeavyWater, and the goal is to use Machine Learning to classify the OCR layer data. The input csv consists of document type and OCR data which is in order.

Since it is Document Classifer vectorizers such as CountVectorizer and HashingVectorizers were used, and ngram of n =3 was used for taking into account the order of words.

Tfid was tried too but had a negative effect on the accuracy so a 3-gram Count Vectorizer is used

CLASSIFIERS:
1) Naive Bayes Multinomial
2)Stochastic Gradient Descent Classifier

SGD performed better than NB Multinomial in terms of accuracy and speed, as we had huge chunks of data. For this reason SGD is used as model in EC2.

Metrics used for measurement:

Confusion Matrix
accuracy

Confidence Interval (95% likelihood)

#Link to the model

http://18.188.95.69/ 

Model hosted on AWS EC2 Instance.

Username & password - (email)

