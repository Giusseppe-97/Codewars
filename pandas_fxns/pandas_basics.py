import pandas as pd

# read_csv()
data_1 = pd.read_csv(r'C:UsersABCDesktopblog_dataset.csv')
data_2 = pd.read_csv(r'C:UsersABCDesktopblog_dataset.csv')

# head()
data_1.head(6)

# describe()
data_1.describe()

# memory_usage()
data_1.memory_usage(deep=True)

# astype()
data_1['Gender'] = data_1.Gender.astype('category')

# loc[:]
data_1.loc[0:4, ['Name', 'Age', 'State']]

# to_datetime()
data_1['DOB'] = pd.to_datetime(data_1['DOB'])

# value_counts()
data_1['State'].value_counts()

# drop_duplicates()
data_1.drop_duplicates(inplace=True)

# groupby()
data_1.groupby(by='State').Salary.mean()

# merge()
data_1.merge(data_2, on='Name', how='left')

# sort_values()
data_1.sort_values(by='Name', inplace=True)

# fillna()
data_1['City temp'].fillna(38.5, inplace=True)

