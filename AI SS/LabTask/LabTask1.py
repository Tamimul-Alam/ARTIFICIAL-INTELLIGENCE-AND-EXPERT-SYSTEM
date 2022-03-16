#!/usr/bin/env python
# coding: utf-8

# In[33]:


def AstarAlgo(start_node, stop_node):
         
        open_set = set(start_node) 
        closed_set = set()
        g = {} 
        parents = {}
 
        
        g[start_node] = 0
        
        
        parents[start_node] = start_node
         
         
        while len(open_set) > 0:
            n = None
 
            
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
             
                     
            if n == stop_node or problem[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                         
     
                    
                    else:
                        if g[m] > g[n] + weight:
                            
                            g[m] = g[n] + weight
                            
                            parents[m] = n
                             
                            
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Path Not Exist')
                return None
 
            
            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()
 
                print('Path : {}'.format(path))
                return path
 
 
            
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path Not Exist')
        return None
         

def get_neighbors(v):
    if v in problem:
        return problem[v]
    else:
        return None

def heuristic(n):
        heuristic = {
            'S': 6,
            'A': 0,
            'B': 6,
            'C': 4,
            'D': 1,
            'E': 10,
            'G': 0,
             
        }
 
        return heuristic[n]
 

    
problem = {
    'S': [('A', 2), ('B', 1)],
    'A': [('C', 2), ('D', 3)],
    'B': [('D', 4),('E', 4)],
    'C': [('G', 4)],
    'D': [('G', 4)],
    'E': None,
    'G': None
     
}
AstarAlgo('S', 'G')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




