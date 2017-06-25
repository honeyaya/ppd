# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 22:27:46 2017

@author: v-xixhua
"""
import sys
import pandas as pd
import numpy as np


bid = pd.read_csv('data/LC.csv',header=None, skiprows=1)
bid.columns = ['listingId','lendmoney','lendtime','lendratio','lendsuccessdate','primaryestimate','lendtype','isfirst','age','sex','phoneidentify','hukouidentify','vedioidentify','educationidentify','Zhengxinidentify','taobaoidentify','historysuccesstimes','historysuccessaccount','totalunbackmoney','historynormalbacktimes','historyunbackovertime'];

bid_specific = pd.read_csv('data/LP.csv',header=None,skiprows=1)
bid_specific.columns= ['listingId','lendtime','backstate','shoudbackmoney','shouldbackinterest','restmoney','restinterest','deadlinetime','backtime','recorddate'];
             
all_bid = pd.merge(bid, bid_specific, on=['listingId'],how = "left")

#----------------------------firstbid
all_bid_first = all_bid[all_bid.isfirst == "是"]

bad_bid_first = all_bid_first[(all_bid_first.backstate==0)|(all_bid_first.backstate==2)]

worse_bid_first = bad_bid_first[bad_bid_first.backstate==0]

good_bid_first = all_bid_first[(all_bid_first.backstate==1)|(all_bid_first.backstate==3)]

better_bid_first = good_bid_first[good_bid_first.backstate==3]

maybe_bid_first = all_bid_first[all_bid_first.backstate==4]


bid_id = all_bid_first[['listingId']] #get id   921655
#print len(bid_id)
bid_id.drop_duplicates(inplace=True) # 87463
#print len(bid_id)

tmp_bid = bad_bid_first[['listingId']] # 450893
#print len(tmp_bid)
tmp_bid.drop_duplicates(inplace=True) # 69903
#print len(tmp_bid)


t1 = bad_bid_first[['listingId','shoudbackmoney']] #450893
#print len(t1)
t1 = t1.groupby(['listingId']).agg('sum').reset_index() #69903l

def get_label(shoudbackmoney):
  if shoudbackmoney > 1000:
    return 1;
  else:
    return 0;
  
t1['label']=t1.shoudbackmoney
t1.label = t1.label.apply(get_label)
t1.rename(columns={'shoudbackmoney':'lossmoney'},inplace=True)
#print t1
#print len(t1)  

#print all_bid_first.shape
st = pd.merge(bid_id, t1, on=['listingId'],how = "left")

#print dataset
#print dataset.shape

#dataset = dataset['label'].replace(0,"NaN")
st = st.fillna(0)
#print st
#print st.shape

dataset = pd.merge(st,bid,on=['listingId'],how="left")
#print dataset
#print dataset.shape


dataset = dataset.replace('未成功认证','0')
dataset = dataset.replace('成功认证','1')

dataset = dataset.replace('是','1')
dataset = dataset.replace('否','0')

dataset = dataset.replace('男','0')
dataset = dataset.replace('女','1')

dataset = dataset.replace('应收安全标','0');
dataset = dataset.replace('电商','1');
dataset = dataset.replace('APP闪电','2');
dataset = dataset.replace('普通','3');
dataset = dataset.replace('其他','4');

                         
dataset = dataset.replace('AAA','0');
dataset = dataset.replace('AA','1');
dataset = dataset.replace('A','2');
dataset = dataset.replace('B','3');
dataset = dataset.replace('C','4');
dataset = dataset.replace('D','5');
dataset = dataset.replace('E','6');
dataset = dataset.replace('F','7');

                         
dataset.to_csv('data/data.csv',columns=["listingId","lossmoney","lendmoney","lendtime","lendratio","lendsuccessdate","primaryestimate","lendtype","isfirst","age","sex","phoneidentify","hukouidentify","vedioidentify","educationidentify","Zhengxinidentify","taobaoidentify","historysuccesstimes","historysuccessaccount","totalunbackmoney","historynormalbacktimes","historyunbackovertime","label"],index=None)












