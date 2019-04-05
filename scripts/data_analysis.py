# imports the neccessary modules
import pandas as pd

# reads & stores the train data in a pandas dataframe
df = pd.read_csv("/Users/nialdaly/Documents/ey_nextwave/data/data_train.csv", index_col=None)

# prints out the top 5 rows
print(df.head(5))

print(df.info())