## Data Analysis Steps

## 1. Define the questions.

# 1. What are the yearly sales trend?
# 2. Which product sild the most in 2016?
# 3. Among the three product categories which one had the lowest sale in 2018?
# 4. What is the yearly sales trend of the 3 customer group
# 5. Are we getting more corporate customers 

## Collect data
import pandas as pd

train = pd.read_csv('train.csv')
train.head()

train.info()

train.isnull().sum()

train[train['Postal Code'].isna()]

## fill in null values with non-null values
train['Postal Code'] = train['Postal Code'].fillna('05401')
train.info()
train.isnull().sum()

train.head()

# deleting a column
del train['Row ID']

train.head(2)

train.info()

# converting object to datetime
train['Order Date'] = pd.to_datetime(train['Order Date'], format='%d/%m/%Y')
train['Ship Date'] = pd.to_datetime(train['Ship Date'], format='%d/%m/%Y')

# Converting float to object
train['Postal Code'] = train['Postal Code'].astype(str)

train.info()
