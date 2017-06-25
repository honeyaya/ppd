# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 22:27:46 2017

@author: v-xixhua
"""
import sys
import pandas as pd
import numpy as np

'''
判断一只首标是否会被还
dataset split:
    cross validation

1.
'''

bid = pd.read_csv('data/LC.csv',header=None, skiprows=1)
bid.columns = ['listingId','lendmoney','lendtime','lendratio','lendsuccessdate','primaryestimate','lendtype','isfirst','age','sex','phoneidentify','hukouidentify','vedioidentify','educationidentify','Zhengxinidentify','taobaoidentify','historysuccesstimes','historysuccessaccount','totalunbackmoney','historynormalbacktimes','historyunbackovertime'];
bid_length = len(bid)
print "The length of Bid is:" + str(bid_length)  #(328553,21)


'''
user = user_total[['listingId']]
print user.shape

user.drop_duplicates(inplace=True)
print user.shape
'''

bid_specific = pd.read_csv('data/LP.csv',header=None,skiprows=1)
bid_specific.columns= ['listingId','lendtime','backstate','shoudbackmoney','shouldbackinterest','restmoney','restinterest','deadlinetime','backtime','recorddate'];
bid_specific_length = len(bid_specific)
print "The length of bid_specific is: " + str(bid_specific_length)
#print bid_total.shape #(3203276,10)

'''
bid = bid_total[['listingId']]
print bid.shape

bid = bid.drop_duplicates(inplace=True)
print bid.shape
'''

#-------------------------------------- all bid data 
'''
classify the bid
bad/all  = 1773299/3203276 = 55.36%  
'''
                 
all_bid = pd.merge(bid, bid_specific, on=['listingId'],how = "left")
all_bid_length = len(all_bid)
print "The length of the all_bid is: " + str(all_bid_length)
#print len(all_bid) #(3203276,30)


bad_bid = all_bid[(all_bid.backstate==0)|(all_bid.backstate==2)]
bad_bid_length = len(bad_bid)
print "The length of bad_bid is: " + str(bad_bid_length)
#print bad_bid.shape  #(1773299,30)

worse_bid = bad_bid[bad_bid.backstate==0]
worse_bid_length = len(worse_bid)
print "The length of the worse_bid is: " + str(worse_bid_length)
#print worse_bid.shape #(1560671,30)

good_bid = all_bid[(all_bid.backstate==1)|(all_bid.backstate==3)]
good_bid.drop_duplicates(inplace=True)
good_bid_length = len(good_bid)
print "The length of the good_bid is: " + str(good_bid_length)
#print good_bid.shape  #(1428897,30)

better_bid = good_bid[good_bid.backstate==3]
better_bid.drop_duplicates(inplace=True)
better_bid_length = len(better_bid)
print "The length of the better_bid is: " + str(better_bid_length)
#print better_bid.shape #(37805,30)

maybe_bid = all_bid[all_bid.backstate==4]
maybe_bid.drop_duplicates(inplace=True)
maybe_bid_length = len(maybe_bid)
print "The length of the maybe_bid is: " + str(maybe_bid_length)
#print maybe_bid.shape #(1080,30)


#----------------------------firstbid

all_bid_first = all_bid[all_bid.isfirst == "是"]
all_big_first_length = len(all_bid_first)
print "The length of the all_bid_first is: " + str(all_big_first_length)

bad_bid_first = all_bid_first[(all_bid_first.backstate==0)|(all_bid_first.backstate==2)]
bad_bid_first.drop_duplicates(inplace=True)
bad_bid_first_length = len(bad_bid_first)
print "The length of bad_bid_first is: " + str(bad_bid_first_length)

worse_bid_first = bad_bid_first[bad_bid_first.backstate==0]
worse_bid_first.drop_duplicates(inplace=True)
worse_bid_first_length = len(worse_bid_first)
print "The length of the worse_bid_first is: " + str(worse_bid_first_length)

good_bid_first = all_bid_first[(all_bid_first.backstate==1)|(all_bid_first.backstate==3)]
good_bid_first.drop_duplicates(inplace=True)
good_bid_first_length = len(good_bid_first)
print "The length of the good_bid is: " + str(good_bid_first_length)


better_bid_first = good_bid_first[good_bid_first.backstate==3]
better_bid_first.drop_duplicates(inplace=True)
better_bid_first_length = len(better_bid_first)
print "The length of the better_bid is: " + str(better_bid_first_length)
#print better_bid.shape #(37805,30)

maybe_bid_first = all_bid_first[all_bid_first.backstate==4]
maybe_bid_first.drop_duplicates(inplace=True)
maybe_bid_first_length = len(maybe_bid_first)
print "The length of the maybe_bid is: " + str(maybe_bid_first_length)
#print maybe_bid.shape #(1080,30)


#------------------------------restbid
all_bid_rest = all_bid[all_bid.isfirst == "是"]
all_big_rest_length = len(all_bid_first)
print "The length of the all_bid_rest is: " + str(all_big_rest_length)


#------------------------------- caculate the lost money
'''
totalmoney = bid['lendmoney'].sum()
print "totalmoney is: " + str(totalmoney)


print bad_bid['shoudbackmoney'].sum() 
print good_bid['shoudbackmoney'].sum() 
print maybe_bid['shoudbackmoney'].sum()


classtotalmoneyfirst = all_bid_first['lendmoney'].sum();
print classtotalmoneyfirst

lossmoney = bad_bid['shoudbackmoney'].sum()
print lossmoney

lossmoneyfirst = bad_bid_first['shoudbackmoney'].sum()
print lossmoneyfirst

'''
print "------------------------------------------";

#------------------------------ for bid first dataset
# all_bid
# all_bid_first
# all_bid_rest


all_id = all_bid_first[['listingId']]
all_id.drop_duplicates(inplace=True)
print len(all_id)

t3 = all_bid[all_bid.isfirst == "否"]
t4 = t3[['listingId']]
print len(t4)
t4.drop_duplicates(inplace=True)
print len(t4)


all_bid.to_csv('data/dataset.csv',index=None)


#get label
'''
def get_label(backstate):
    if backstate == 0 or backstate == 2:
        return 1
    else:
        return 0

all_bid['label'] = all_bid.backstate
all_bid.label = all_bid.label.apply(get_label)
'''


















