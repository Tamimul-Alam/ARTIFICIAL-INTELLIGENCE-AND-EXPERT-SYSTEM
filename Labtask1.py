#!/usr/bin/env python
# coding: utf-8

# In[29]:


problem = {
  'S' : {'A':2,'B':1},
  'A' : {'C':2,'D':3},
  'B' : {'D':4,'E':4},
  'C' : {'G':4},
  'D' : {'G':4},
  'E' : {},
  'G' : {}
}

def BFS_Shortest_Path(problem, start, goal):
    explored =[]
    queue = [[start]]
    if start == goal:
        return "start = goal"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = problem[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
                
            explored.append(node)
    return

BFS_Shortest_Path(problem, 'S','G')


# In[ ]:





# In[ ]:





# In[ ]:




