from csv import reader
import numpy as np
import pandas as pd


# read csv file as a list of lists
with open('deceasedT.csv', 'r') as read_obj:
# pass the file object to reader() to get the reader object
 csv_reader = reader(read_obj)
# Pass reader object to list() to get a list of lists
 list_of_rows = list(csv_reader)
#print(list_of_rows)

for i in range(2, len(list_of_rows)):
    for j in range(1, len(list_of_rows[0])):
        list_of_rows[i][j] = int(list_of_rows[i][j])


res_list = []
for i in range(2, len(list_of_rows)):
    for j in range(2, len(list_of_rows[0])):
       list_of_rows[i][j] = list_of_rows[i][j] + list_of_rows[i][j-1]

'''
for i in range(0, 20):
    for j in range(0, 10):
       print(list_of_rows[i][j])
'''


df = pd.DataFrame(list_of_rows)

df.to_csv('finaldeceased.csv', index=False)
