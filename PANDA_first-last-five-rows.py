import pandas as pd
cars=pd.read_csv('cars.csv')
print('First five rows of the DataFrame')
print(cars.head())
print('Last five rows of the DataFrame')
print(cars.tail())