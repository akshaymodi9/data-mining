import pandas as pd
import numpy as np
import os

from sklearn.decomposition import PCA

#directory name of the output file
dirname = 'output'

""" Answer to Question 1 """
 
#read the csv file
#By passing float precision as high the precsion is not lost.
data = pd.read_csv('./specs/SensorData_question1.csv',index_col = False,float_precision='high')

#added new colums of original data
data['Original Input3'] = data['Input3']
data['Original Input12'] = data['Input12']

#Normalize the Input3 column using the z-score normalization 
"""
    Formula for z = (x – μ) / σ
        where z: normailzed data
              x: The data point which has to be normalized 
              μ: Mean of the data  
              σ: Standard deviation of the data   
"""

data['Input3']=(data['Input3']-data['Input3'].mean())/data['Input3'].std()



#Normallize the Input12 in the range [0.0,1.0]
"""
    Formula 
        𝑧 = 𝑥𝑖−min(𝑥) / (max(𝑥)−min(𝑥))
        where z: normailzed data
              𝑥𝑖: The data point which has to be normalized 
         min(𝑥): Minimum value in the data set
         max(𝑥): Maximum value in the data set

"""

data['Input12'] = (data['Input12']-data['Input12'].min())/(data['Input12'].max()-data['Input12'].min())

#create a new variable that doesnt hava the columns required for mean
data1 = data.drop(['Original Input3','Original Input12'],axis=1)

#mean of inputs
data['Average Input'] = data1.mean(axis=1)

# check if the output folder is present, if not create output folder
if not os.path.exists(dirname):
    os.mkdir(dirname)

#write the output to output file
data.to_csv('./output/question1_out.csv',index=False)



""" Answer to Question 2 """

#read the csv file
df = pd.read_csv('./specs/DNAData_question2.csv',index_col = False,float_precision='high')


#Apply PCA for 95% variance
pca = PCA(n_components=0.95)

#Reduction of attributes
pca.fit(df)
pca_generated_data = pca.transform(df)

#make a copy of dataframe
new_df = df.copy(deep=True)

#transpose the pca generated output as the bin has to be created accross rows
pca_transpose = pca_generated_data.T

#generate the new columns for width and assign the bin.
for i in range(pca.n_components_):
    new_col = 'pca'+str(i)+'_width'
    new_df[new_col] = pd.cut(pca_transpose[i],10)

#generate the new columns for frequency and assign the bin
for i in range(pca.n_components_):
    new_col = 'pca'+str(i)+'_freq'
    new_df[new_col] = pd.qcut(pca_transpose[i],10)


# check if the output folder is present, if not create output folder
if not os.path.exists(dirname):
    os.mkdir(dirname)

#write the output to output file
new_df.to_csv('./output/question2_out.csv',index=False)