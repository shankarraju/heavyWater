# heavyWater mini-project - SHANKAR RAJU

This is a document classifier project for HeavyWater mini-project challenge. 
# Introduction
The data was provided by HeavyWater, and the goal is to use Machine Learning to classify the OCR layer data. The input csv consists of document type and OCR data which is in order.
# Machine Learning Model
<li>Since it is Document Classifer vectorizers such as CountVectorizer and HashingVectorizers were used, and ngram of n =3 was used for taking into account the order of words.</li>

<li>Tfid was tried too but had a negative effect on the accuracy so a 3-gram Count Vectorizer is used</li>

<h4>CLASSIFIERS:</h4>
1) Naive Bayes Multinomial <br>
2)Stochastic Gradient Descent Classifier

<li>SGD performed better than NB Multinomial in terms of accuracy and speed, as we had huge chunks of data. For this reason SGD is used as model in EC2.</li>

<h6>Metrics used for measurement:</h6>

<li>Confusion Matrix</li>
<li>accuracy<li>

Details about all the model metrics and Confidence Interval (95% likelihood) found in Document Classifier-SHANKAR RAJU.ipynb


# AWS

# Tools Used
<li>AWS EC2 Instance</li>
<li>Flask</li>
<li>Flask REST-ful API</li>
<li>SHA-256 password Encryption</li>
<li>HTML, CSS, JQuery, Bootstrap</li>

# Link to the model
http://18.188.167.76/

Model is successfully hosted on AWS EC2 Instance and running.

Username & password - (email)

