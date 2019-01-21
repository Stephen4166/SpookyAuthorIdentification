# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 22:23:46 2017

@author: Stephen4166
"""


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics

print("\nThis is a part of training data:")
df = pd.read_csv('train.csv')
print(df.head())

word, author = df['text'], df['author']
X_train, X_test, y_train, y_test = train_test_split(word, author, test_size=0.15)


# MNB
clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                 ('tfidf', TfidfTransformer()),
                 ('clf', MultinomialNB(alpha=1.0)),
                 ])
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
print("\nThis is the report:")
print(metrics.classification_report(y_test, predicted))
print("\nThis is the accuracy:")
print(metrics.accuracy_score(y_test, predicted))
print("\nThis is the confusion_matrix:")
print(metrics.confusion_matrix(y_test, predicted))
print()


# SVM
clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(penalty='l2',alpha=1e-4,
                                      max_iter=None, learning_rate='optimal')),
                ])
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
print("\nThis is the report:")
print(metrics.classification_report(y_test, predicted))
print("\nThis is the accuracy:")
print(metrics.accuracy_score(y_test, predicted))
print("\nThis is the confusion_matrix:")
print(metrics.confusion_matrix(y_test, predicted))


# RandomForestClassifier
clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                ('tfidf', TfidfTransformer()),
                ('clf', RandomForestClassifier(criterion='entropy', 
                                               n_estimators=50,
                                               max_depth=None)),
                ])
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
print("\nThis is the report:")
print(metrics.classification_report(y_test, predicted))
print("\nThis is the accuracy:")
print(metrics.accuracy_score(y_test, predicted))
print("\nThis is the confusion_matrix:")
print(metrics.confusion_matrix(y_test, predicted))


# Neural Network
clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                ('tfidf', TfidfTransformer()),
                ('clf', MLPClassifier(hidden_layer_sizes=(10, 10, 10, 10, 10, 10))),
                ])
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
print("\nThis is the report:")
print(metrics.classification_report(y_test, predicted))
print("\nThis is the accuracy:")
print(metrics.accuracy_score(y_test, predicted))
print("\nThis is the confusion_matrix:")
print(metrics.confusion_matrix(y_test, predicted))


# We choose the MNB as the model
clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                 ('tfidf', TfidfTransformer()),
                 ('clf', MultinomialNB(alpha=1.0)),
                 ])

