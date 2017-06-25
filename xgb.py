# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:49:48 2017

@author: v-xixhua
"""

import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler

dataset = pd.read_csv('data/dataset.csv')

print dataset.shape

X = dataset.drop(['listingId','lendsuccessdate','label'],axis=1)
y = dataset.label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dataset1 = xgb.DMatrix(X_train,label=y_train)
dataset2 = xgb.DMatrix(X_test, label=y_test)

params={'booster':'gbtree',
	    'objective': 'rank:pairwise',
	    'eval_metric':'auc',
	    'gamma':0.1,
	    'min_child_weight':1.1,
	    'max_depth':4,
	    'lambda':10,
	    'subsample':0.7,
	    'colsample_bytree':0.7,
	    'colsample_bylevel':0.7,
	    'eta': 0.01,
	    'tree_method':'exact',
	    'seed':0,
	    'nthread':12
	    }

#train the model
watchlist = [(dataset1,'train'),(dataset2,'val')]
model = xgb.train(params,dataset1,num_boost_round=3000,evals=watchlist,early_stopping_rounds=300)



