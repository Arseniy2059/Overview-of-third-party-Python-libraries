import requests
import pandas
import numpy as np

response = requests.get('https://api.github.com/events')
print(response.text)
print(response.json())
print(response.status_code)


dataframe = pandas.read_csv('hisla.txt')
print(dataframe.describe())


weight = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

weight1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


print(np.dot(weight, weight1))
