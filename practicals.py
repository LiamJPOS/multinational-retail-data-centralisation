import numpy as np

#Count the unique values in a row

#random ints between 0 and 10 (so 9) 9 columns, 12 rows 
arr = np.random.randint(0, 10, size=(9,12))

print(arr)

def count_unique(ar):
    return len(np.unique(ar))

for i in arr:
    print(count_unique(i))
    

#--------------------------------------------------------

