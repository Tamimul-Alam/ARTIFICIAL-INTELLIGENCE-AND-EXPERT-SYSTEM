#!/usr/bin/env python
# coding: utf-8

# In[10]:


def getInvCount(arr):
    inv_count = 0
    e_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != e_value and arr[i] != e_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count 
     
def isSolvable(puzzle) :
  
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    print("***Inversion Count : ",inv_count,"***")
    return (inv_count % 2 == 0)
     
puzzle = [[7, 1, 2],[5, 0, 4],[8, 3, 6]]
if(isSolvable(puzzle)) :
    
    print("***Puzzle is Solvable***")
else :
    
    print("***Puzzle is Not Solvable***")
            


# In[ ]:




