
#import seaborn as sns
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # importing matplotlib modules to plot

# load the boston housing csv file
df = pd.read_csv('Boston_Housing.csv')
# print(df)
df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.8

# split 80-20 train and test data
train = df[msk]
# print(train.shape)
test = df[~msk]
# print(test.shape)

a = []

# sampling the dataframe
# generate 50 random samples assign random_state with different number
for x in range(50):
    sampleSet = train.sample(n=100, replace=True)
    # print(sample)
    # feature matrix for each sample
    X_train = sampleSet.iloc[:, :3].values
    # response vector of train data for each sample
    Y = sampleSet.iloc[:, 3].values
    # x transpose
    X_traint = np.transpose(X_train)
    A = np.dot(X_traint, X_train)
    B = np.linalg.inv(A)
    C = np.dot(X_traint, Y)
    Bbar = np.dot(B, C)
    Ybar = np.dot(X_train, Bbar)
    # print(Bbar.shape)

    # print(Ybar.shape)#this is to check each iteration gives prediction array of size 100
    # test data
    Xtest = test.iloc[:, :3].values
    #print("Xtest size")

    # response vector of test data
    Ytest = test.iloc[:, 3].values
    # print(Xtest.shape)
    YbarTest = np.dot(Xtest, Bbar)
    # append the Y hat values to an array
    a.append(YbarTest)

# take it to a np array
a = np.asarray(a)
# take the average of all size=50 arrays using mean command
averageYbar = np.mean(a, axis=0)
# print(averageYbar.shape)

# plotting
testScatter = plt.scatter(averageYbar, Ytest, color="r", marker="*", s=60)
plt.plot(Y, Y, color="black")  # plotting the stright line
plt.xlabel('Real value')  # adding axis labels
plt.ylabel('Predicated Value')
plt.show()  # displaying the plot
