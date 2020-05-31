# includes all ToDos in Pandass
import pandas as pd  # import pandas module as pd

# create a series with a list
# s = pd.Series([1, 4, -2, 'home'], index=['a', 'b', 'c', 'd'])
# print(type(s))
#
# print(s.dtype)
# print(s)

# create a data frame with a dictionary
# data = {'population': [1.5, 1.2, 2.0, 1.4, 0.8], 'state': ['Nevada', 'Florida', ’Ohio','Texas','Florida'],'year':[2003, 2000, 2004, 1990, 1994]}
# df = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five'], columns=['year', 'state', 'population', 'debt'])
# ..........................................................................................................................

df = pd.read_csv('sampleDataSet.csv')  # without setting names
# df = pd.read_csv("sampleDataSet.csv", names=[
#              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])  # setting names
print(df)
