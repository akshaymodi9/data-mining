import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#directory name of the output file
dirname = 'output'

""" Answer to Question 1 """

data = pd.read_csv('./specs/marks_question1.csv')

plt.plot(data['midterm'],data['final'],'ro',linewidth=3,color='blue')
plt.xlabel('midterm')
plt.ylabel('final')

# check if the output folder is present, if not create output folder
if not os.path.exists(dirname):
    os.mkdir(dirname)

plt.savefig('./output/marks.png')

trained_data = np.array(data['midterm'])
target_data = np.array(data['final'])


trained_data = trained_data.reshape(-1, 1)
# target_data = target_data.reshape(-1,1)

regr = LinearRegression()
regr.fit(trained_data,target_data)
y_pred = regr.predict(trained_data)


data_to_predict = np.array([86])
data_to_predict = data_to_predict.reshape(-1,1)
predicted_data = regr.predict(data_to_predict)

plt.plot(trained_data,y_pred,color='red')
plt.show()

print(predicted_data)


""" Answer to Question 2 """

data2 = pd.read_csv('./specs/borrower_question2.csv')

data2.pop('TID')

