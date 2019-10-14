import os

import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth

#directory name of the output file
dirname = 'output'

""" Answer to Question 1 """
 
#read the csv file
data = pd.read_csv('./specs/gpa_question1.csv')

#Filter out the count attribute
data.pop('count')

#convert the data set into the form that is required by the apriori algorithm
dummies_out = pd.get_dummies(data)


# using apriori algorithm calculate the frequent itemset using minimum support as 15%
# use_colnames attribute in apriori will use the same columns in frequent dataset output as in input dataset.
frequent_itemset = apriori(dummies_out, min_support=0.15,use_colnames=True)


# check if the output folder is present, if not create output folder
if not os.path.exists(dirname):
    os.mkdir(dirname)

#write the output to output file
frequent_itemset.to_csv('./output/question1_out_apriori.csv',index=False)


# calculate the association rules based on confidence.
#confidence is set to 90%
rules_9 = association_rules(frequent_itemset, metric="confidence", min_threshold=0.9)

rules_9.to_csv('./output/question1_out_rules9.csv',index=False)

# confidence is set to 70%
rules_7 = association_rules(frequent_itemset, metric="confidence", min_threshold=0.7)

rules_7.to_csv('./output/question1_out_rules7.csv',index=False)



""" Answer to Question 2 """

#read the csv file
data_2 = pd.read_csv('./specs/bank_data_question2.csv')

# filter out the id attribute
data_2.pop('id')

# only get those columns that contain numeric data.
numeric_data = data_2._get_numeric_data()

# initialize a new dataframe
data_1 = pd.DataFrame()

# using pandas cut method to discretise the numeric data in equal width
for i in numeric_data:
    data_1[i] = pd.cut(numeric_data[i],3)

# update the original dataframe to contain the discretised data after binning
data_2.update(data_1,overwrite=True)

# convert the data in the form to be used by fpgrowth algorithm.
dummies_out = pd.get_dummies(data_2)

#apply the fp growth algorthm to calculate the frequent itemsets.
output = fpgrowth(dummies_out, min_support=0.2,use_colnames=True)

output.to_csv('./output/question2_out_fpgrowth.csv',index = False)

#calculate the association rules 
#79% percentage is the confidence where atleast 10 rules are genearated. 
rules = association_rules(output, metric="confidence", min_threshold=0.70)

rules.to_csv('./output/question2_out_rules.csv',index=False)
