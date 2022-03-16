#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as NP 
from geneticalgorithm import geneticalgorithm as GG

def f(x):
    
    return NP.sum(x)  
    
    
varbound=NP.array([[0,10]]*3)

algorithm_param = {
    'max_num_iteration' : 3000,\
    'population_size' : 100,\
    'mutation_probability' : 0.1,\
    'elit_ratio' :0.01,\
    'crossover_probability' : 0.5,\
    'parents_portion' : 0.3,\
    'crossover_type' : 'uniform',\
    'max_iteration_without_improv' : None,\
}

model=GG(
    function=f,\
    dimension=3,\
    variable_type='real',\
    variable_boundaries=varbound,\
    algorithm_parameters=algorithm_param

)
model.run()


# In[ ]:





# In[ ]:




