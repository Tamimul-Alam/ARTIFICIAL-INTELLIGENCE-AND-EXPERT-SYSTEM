#!/usr/bin/env python
# coding: utf-8

# In[49]:



Destination={
    
    'A': [('S', 140), ('Z', 75), ('T',118)],

    'Z': [('A', 75), ('O', 71)],

    'O': [('Z', 71), ('S', 151)],

    'S': [('A', 140), ('O', 151), ('F', 99), ('R', 80)],

    'T': [('A', 118), ('L', 111)],

    'L': [('T', 111), ('M', 70)],

    'M': [('L', 70), ('D', 75)],

    'D': [('M', 75), ('C', 120)],

    'C': [('D', 120), ('R', 146), ('P', 138)],

    'R': [('S', 80), ('C', 146), ('P', 97)],

    'F': [('S', 99), ('B', 211)],

    'P': [('R', 97), ('C', 138), ('B', 101)],

    'B': [('F', 211), ('P', 101), ('G', 90), ('U', 85)],

    'G': [('B', 90)],

    'U': [('B', 85), ('V', 142), ('H', 98)],

    'H': [('U', 98), ('E', 86)],

    'E': [('H', 86)],

    'V': [('I', 92),('U', 142)],

    'I': [('V', 92), ('N', 87)],

    'N': [('I', 87)]


}


class A:

    def h(self, n):
        h_SLD = {

            'A': 366,

            'Z': 374,

            'O': 380,

            'S': 253,

            'T': 329,

            'L': 244,

            'M': 241,

            'D': 242,

            'C': 160,

            'R': 193,

            'F': 176,

            'P': 100,

            'B': 0,

            'G': 77,

            'U': 80,

            'H': 151,

            'E': 161,

            'V': 199,

            'I': 226,

            'N': 234

        }

        return h_SLD[n]

    def __init__(self, c_list):

        self.c_list = c_list

    def get_neighbors(self, i):

        return self.c_list[i]

    def A_Star(self, start, stop):
        open_l = set(start)
        closed_l = set([])
        dist = {}
        dist[start] = 0
        par = {}
        par[start] = start

        while len(open_l) > 0:
            n = None

            for i in open_l:
                if n == None or dist[i] + self.h(i) < dist[n] + self.h(n):
                    n = i

            if n == None:
                print('Path Not Found')

                return None

            if n == stop:

                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
                reconst_path.append(start)
                reconst_path.reverse()   
                print('Path', reconst_path)
                return reconst_path  

            for m, weight in self.get_neighbors(n):

                if m not in open_l and m not in closed_l:
                    open_l.add(m)
                    par[m] = n
                    dist[m] = dist[n] + weight

                else:

                    if dist[m] > dist[n] + weight:
                        dist[m] = dist[n] + weight
                        par[m] = n

                        if m in closed_l:
                            closed_l.remove(m)
                            open_l.add(m)

            open_l.remove(n)
            closed_l.add(n)

        print('Path Not Found')
        return None

graph = A(Destination)
graph.A_Star('O','E')


# In[ ]:





# In[ ]:




