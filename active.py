from csv import reader
import numpy as np
import pandas as pd


# read csv file as a list of lists
with open('confirmed17june.csv', 'r') as read_obj:
# pass the file object to reader() to get the reader object
 csv_reader = reader(read_obj)
# Pass reader object to list() to get a list of lists
 list_of_rows = list(csv_reader)
#print(list_of_rows)


# read csv file as a list of lists
with open('deceased17june.csv', 'r') as read_obj0:
# pass the file object to reader() to get the reader object
 csv_reader0 = reader(read_obj0)
# Pass reader object to list() to get a list of lists
 list_of_rows0 = list(csv_reader0)
#print(list_of_rows)


# read csv file as a list of lists
with open('recovered17june.csv', 'r') as read_obj1:
# pass the file object to reader() to get the reader object
 csv_reader1 = reader(read_obj1)
# Pass reader object to list() to get a list of lists
 list_of_rows1 = list(csv_reader1)
#print(list_of_rows)



for i in range(1, len(list_of_rows)):
    for j in range(4, len(list_of_rows[0])):
        list_of_rows[i][j] = int(list_of_rows[i][j])


for i in range(1, len(list_of_rows0)):
    for j in range(4, len(list_of_rows0[0])):
        list_of_rows0[i][j] = int(list_of_rows0[i][j])



for i in range(1, len(list_of_rows1)):
    for j in range(4, len(list_of_rows1[0])):
        list_of_rows1[i][j] = int(list_of_rows1[i][j])



for i in range(1, len(list_of_rows)):
    for j in range(4, len(list_of_rows[0])):
       list_of_rows[i][j] = list_of_rows[i][j] - list_of_rows0[i][j] - list_of_rows1[i][j]

'''
for i in range(0, 20):
    for j in range(0, 10):
       print(list_of_rows[i][j])
'''


df = pd.DataFrame(list_of_rows)

df.to_csv('active.csv', index=False)
