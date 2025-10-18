import pandas as pd
import numpy as np

# READING CSV FILE
# data_frame = pd.read_csv("data.csv")
# print(data_frame.head())

# READING EXCEL FILE
# df = pd.read_excel("dados.xlsx")

# READING JSON FILE
# df = pd.read_json("data.json")

# CREATING A DATAFRAME
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
# print(type(df))
# print("DataFrame: \n" + str(df))
# print(df)


# EXPLORING DATAFRAME
# print(df.info()) # STRUCTURE
# print(df.describe()) # BASICS STATS
# print(df['Age'].value_counts())
# print(df.isnull().sum())
# print(df.keys())

