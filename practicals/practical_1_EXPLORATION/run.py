import pandas as pd
import os

#directory name of the output file
dirname = 'specs/output'

#read the csv file
data = pd.read_csv('./specs/AutoMpg_question1.csv')

#perform operations
data['horsepower'] = data['horsepower'].fillna(data['horsepower'].mean())
data['origin'] = data['origin'].fillna(data['origin'].min())

#check if the output folder is present, if not create output folder
if not os.path.exists(dirname):
    os.mkdir(dirname)

#write the output to output file
data.to_csv("./specs/output/question1_out.csv",index=False,)


#Read two files for question 2
file_a = pd.read_csv('./specs/AutoMpg_question2_a.csv')
file_b = pd.read_csv('./specs/AutoMpg_question2_b.csv')

#perform operations
file_b = file_b.rename(columns={"name":"car name"})
file_a['other'] = 1

#concat the data in one single dataframe
single_file = pd.concat([file_a,file_b])

#check if the output folder is present, if not create output folder
if not os.path.exists(dirname):
    os.mkdir(dirname)

#write the output to output file
single_file.to_csv('./specs/output/question2_out.csv',index=False)
