# import standard data sets
from sklearn import datasets
# import the Logistic regression model
from sklearn.linear_model import LogisticRegression

# split data set into a train and test set
from sklearn.model_selection import train_test_split
# importing modules to measure classification performance
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, accuracy_score
# load 'wine' data set from standard data sets
digits_dataset = datasets.load_digits()
x = digits_dataset["data"]  # defining features values
y = digits_dataset["target"]  # defining target variable values
# splitting data set into a train and test set with 80% and 20%
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)

# creating an instance of the model
# increased the default max iteration value
log_reg = LogisticRegression(max_iter=40000)

log_reg.fit(x_train, y_train)  # fitting the relationship between data
predictions = log_reg.predict(x_test)  # predict labels for test data
print("predictions.......")
print(predictions)

print("classification report for predicted values")
print(classification_report(y_test, predictions))
print("confusion matrix.....")
print(confusion_matrix(y_test, predictions))
print("accuracy score.......")
print(accuracy_score(y_test, predictions))
