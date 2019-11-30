import pandas as pd
cars=pd.read_csv('cars.csv')
o=cars.iloc[:5,[1,3,5,7,9,11]]
print('a. First five rows with odd-numbered columns')
print(o)
print("")
x=cars[cars['Model']=='Mazda RX4']
print('b. Mazda RX4')
print(x)
print("")
y=cars.loc[cars['Model']=='Camaro Z28', ['cyl']]
print('c. Number of Cylinders that Camaro Z28 has')
print(y)
print("")
z=cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']), ['Model','cyl','gear']]
print('d. The number of cylinders and the type of gear the following cars have')
print(z)
 