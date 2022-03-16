#!/usr/bin/env python
# coding: utf-8

# In[3]:


def minimax(depth, node, isMaximizingPlayer, values, alpha, beta):
  
  if depth == 3:
    return values[node]
  
  if isMaximizingPlayer == True:
    best = Minimum
    for i in range(2):
      value = minimax(depth+1, node*2+i, False, values, alpha, beta)
      best = max(best, value)
      alpha = max(alpha, best)
      
      if beta <= alpha:
        break
    return best
  
  else:
    best = Maximum
    for i in range(2):
      value = minimax(depth+1, node*2+i, True, values, alpha, beta)
      best = min(best, value)
      alpha = min(alpha, best)

      if beta <= alpha:
        break
    return best

Min = int(input('***Enter the Minimum value: '))
Max = int(input('***Enter the Maximum value: '))
Minimum, Maximum = Min, Max
if __name__ == '__main__':
  
  values = []
  valN = int(input('***Enter the value number: '))
  for i in range(valN):
    x = int(input('Enter the {} no element: '.format(i+1)))
    values.append(x)
  print('***Values = {}'.format(values))
  print('***Optimal value is: {}.'.format(minimax(0, 0, True, values, Minimum, Maximum)))


# In[ ]:




