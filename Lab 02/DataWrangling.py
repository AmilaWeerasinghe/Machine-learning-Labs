

from pandas.plotting import scatter_matrix
import pandas as pd  # import pandas module as pd
import matplotlib.pyplot as plt

# ............................................................................................................................
# part 1
df = pd.read_csv("lab02Exercise01.csv", names=[
                 "Chanel1", "Chanel2", "Chanel3", "Chanel4", "Chanel5"])
# print(df)
# ..........................................................................................................................
# part 2
# calculate mean value

mean_value1 = df["Chanel1"].mean()
mean_value2 = df["Chanel2"].mean()
mean_value3 = df["Chanel3"].mean()
mean_value4 = df["Chanel4"].mean()
mean_value5 = df["Chanel5"].mean()

# replace mean values
df["Chanel1"] = df["Chanel1"].fillna(mean_value1)
df["Chanel2"] = df["Chanel2"].fillna(mean_value2)
df["Chanel3"] = df["Chanel3"].fillna(mean_value3)
df["Chanel4"] = df["Chanel4"].fillna(mean_value4)
df["Chanel5"] = df["Chanel5"].fillna(mean_value5)
# ..........................................................................................................................
# Part3
#pd.plotting.scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
# print(df)
# plt.show()
# ..........................................................................................................................
# part 4
# define a function to decide the value of the new column


def AddVal(row):
    if ((row["Chanel1"]+row["Chanel5"])/2) < ((row["Chanel2"]+row["Chanel3"]+row["Chanel4"])/3):
        return 1

    else:
        return 0


# send row by row into AddVal funtion as add the new value to a seperate column
df["new_column"] = df.apply(AddVal, axis=1)
print(df)
