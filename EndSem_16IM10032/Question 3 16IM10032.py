
# coding: utf-8

# In[95]:


import numpy as np
import math
import random


# In[96]:


data = np.genfromtxt("TSP 42 Cities.txt", dtype='int')
d = data


# In[97]:


n_ants = 700000
int_pheromone = 1
alpha = 1
beta = 1
pher_evap = 0.1
Q = 5


# In[98]:


def tabu_matrix(n):
    tabu = np.ones((n),dtype = float)
    for i in range(0,n):
        tabu[i]= 1
    return tabu


# In[ ]:


pheromone = np.multiply(np.ones((42,42),dtype = float),int_pheromone)
best_route = []
best_route_length = 3400
for i in range(n_ants):
    initial_node = random.randint(0,41)
    tabu = tabu_matrix(42)
    route = []
    route.append(initial_node)
    curr_node = initial_node
    count = 1
    route_length = 0
    tabu[initial_node] = 0
    while(count!=42):
        p = np.array(pheromone[curr_node,:])
        #print(p)
        for i in range(0,42):
            if(tabu[i] == 1):
                p[i] = p[i]**alpha/d[curr_node][i]**beta
            else:
                p[i] = 0
        max_sum = np.sum(p,axis = 0)
        p= p/max_sum
        roulette_wheel = random.random()
        sums = 0
        for i in range(0,42):
            if(tabu[i] == 1):
                sums = sums + p[i]
                if(sums>=roulette_wheel):
                    next_node = i
                    break
        route_length += d[curr_node][next_node]
        tabu[next_node] = 0
        curr_node = next_node
        route.append(curr_node)
        count += 1 
    #print(route_length)
    if(best_route_length>route_length):
        best_route_length = route_length
        best_route = route
    for i in range(0,len(route)-1):
        updated_pher = (1-pher_evap)*pheromone[route[i]][route[i+1]] + Q/route_length
        pheromone[route[i]][route[i+1]] = updated_pher
        pheromone[route[i+1]][route[i]] = updated_pher


# In[ ]:


print(best_route_length)


# In[ ]:


print(best_route)


# In[ ]:


len(best_route)

