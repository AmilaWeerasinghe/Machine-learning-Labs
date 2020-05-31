import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # importing matplotlib modules to plot

# load the boston housing csv file
df = pd.read_csv('Boston_Housing.csv')
# print(df)#for testing purpose
df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.8

# split 80-20 train and test data
train = df[msk]
test = df[~msk]

# print(train)#for testing purpose
# print(test)

# feature matirx of train data
X_train = train.iloc[:, :3].values
# print(X_train.shape)

# response vector of train data
Y = train.iloc[:, 3].values
# print(Y.shape)

# ........Noe calculate the given equation
# transpose for X
X_traint = np.transpose(X_train)
# print(X_traint.shape)

A = np.dot(X_traint, X_train)
# print(A.shape)

B = np.linalg.inv(A)
# print(B.shape)

C = np.dot(X_traint, Y)
# print(C.shape)

# find the values of b hat
Bbar = np.dot(B, C)
print(Bbar)
print("B bar size....")
print(Bbar.shape)

Ybar = np.dot(X_train, Bbar)
print("y hat for train data")
print(Ybar)

print("train data completed...........")

# test data
print("....train data.....process")
Xtest = test.iloc[:, :3].values
# print(X)


# response vector of test data
Ytest = test.iloc[:, 3].values

print("Y bar for test data")
YbarTest = np.dot(Xtest, Bbar)
print(YbarTest)


# plottting
trainScatter = plt.scatter(Ybar, Y, color="b", marker="*", s=60)
testScatter = plt.scatter(YbarTest, Ytest, color="r", marker="*", s=60)
plt.legend((trainScatter, testScatter),
           ('train data', 'test data'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)

plt.plot(Y, Y, color="black")  # plotting the stright line
plt.xlabel('Real value')  # adding axis labels
plt.ylabel('Predicated Value')
plt.show()  # displaying the plot
