# To download italy covid csv file(only once we have to use next 2 statements)  
# from urllib.request import urlretrieve
# urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv','italy-covid-daywise.csv')
import pandas as pd

covid_df = pd.read_csv('E:\python\jovian.ml\italy-covid-daywise.csv')
print(type(covid_df))  # Dataframe Type 
#print(covid_df.to_string())  # displayes the entire row and column




# get info and description about covid_df file
print(covid_df.info())
print(covid_df.describe())

# to know about columns
print(covid_df.columns) # o/p: Index(['date', 'new_cases', 'new_deaths', 'new_tests'], dtype='object')

# shape
# returns in tuple (rows,columns)
print(covid_df.shape)   # for this example:(248, 4)

# Here's a summary of the functions & methods we've looked at so far:

#      pd.read_csv - Read data from a CSV file into a Pandas DataFrame object
#     .info() - View basic infomation about rows, columns & data types
#     .describe() - View statistical information about numeric columns
#     .columns - Get the list of column names
#     .shape - Get the number of rows & columns as a tuple





# ****************************************************************************************************
# Retrieving data from a data frame
# Pandas format is simliar to this(as dictionary in python)
# Concept 1:
covid_data_dict = {
    'date':       ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases':  [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
}
# Concept 2:
# Pandas format is not similar to this
covid_data_list = [
    {'date': '2020-08-30', 'new_cases': 1444, 'new_deaths': 1, 'new_tests': 53541},
    {'date': '2020-08-31', 'new_cases': 1365, 'new_deaths': 4, 'new_tests': 42583},
    {'date': '2020-09-01', 'new_cases': 996, 'new_deaths': 6, 'new_tests': 54395},
    {'date': '2020-09-02', 'new_cases': 975, 'new_deaths': 8 },
    {'date': '2020-09-03', 'new_cases': 1326, 'new_deaths': 6},
]
# As both the concept are correct but storing capacity in Concept 2 is not good 
# Concept 1 is better

print(covid_data_dict["new_cases"])
print(covid_df['new_cases'])
# In the above statement, Each column is represented using a data structure called Series,
# which is essentially a numpy array with some extra methods and properties.
print(type(covid_df['new_cases']))  # Series type

print(covid_df['new_cases'][246])
print(covid_df['new_tests'][240])

print(covid_df[246]['new_cases'])
print(covid_df[240]['new_tests'])