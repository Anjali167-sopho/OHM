
# coding: utf-8

# In[44]:


import numpy as np
import math
import random


# In[45]:


def fitness(x1,x2,x3,x4):
    f = ((1/6.931) - (x1*x2)/(x3*x4))**2
    return f


# In[46]:


def position(r):
    x = 12 + r*(60-12)
    for i in range(0,len(x)):
        x[i] = int(x[i])
    return x


# In[47]:


def velocity(r):
    x = r - 0.5
    return x


# In[77]:


w = 0.7
c1 = 0.3
c2 = 0.5
n = 25
e = 100000


# In[78]:


f = np.zeros((n))
r1 = np.random.rand(n)
r2 = np.random.rand(n)
r3 = np.random.rand(n)
r4 = np.random.rand(n)
r5 = np.random.rand(n)
r6 = np.random.rand(n)
r7 = np.random.rand(n)
r8 = np.random.rand(n)
x1 = position(r1)
x2 = position(r2)
x3 = position(r3)
x4 = position(r4)
v1 = velocity(r5)
v2 = velocity(r6)
v3 = velocity(r7)
v4 = velocity(r8)
for i in range(0,n):
    f[i] = fitness(x1[i],x2[i],x3[i],x4[i])
l_best_fit = f
l_best_position1 = x1
l_best_position2 = x2
l_best_position3 = x3
l_best_position4 = x4
g_best_fit = np.min(f)
g_best_position1 = x1[np.argmin(f)]
g_best_position2 = x2[np.argmin(f)]
g_best_position3 = x3[np.argmin(f)]
g_best_position4 = x4[np.argmin(f)]


# In[79]:


for j in range(0,e):
    v1 = w*v1 + c2*np.multiply(np.random.rand(n),(l_best_position1 - x1)) + c1*np.multiply(np.random.rand(n),(g_best_position1 - x1))
    v2 = w*v2 + c2*np.multiply(np.random.rand(n),(l_best_position2 - x2)) + c1*np.multiply(np.random.rand(n),(g_best_position2 - x2))
    v3 = w*v3 + c2*np.multiply(np.random.rand(n),(l_best_position3 - x3)) + c1*np.multiply(np.random.rand(n),(g_best_position3 - x3))
    v4 = w*v3 + c2*np.multiply(np.random.rand(n),(l_best_position4 - x4)) + c1*np.multiply(np.random.rand(n),(g_best_position4 - x4)) 
    for i in range(0,len(v1)):
        v1[i] = int(v1[i])
        v2[i] = int(v2[i])
        v3[i] = int(v3[i])
        v4[i] = int(v4[i])
    x1 = x1 + v1
    x2 = x2 + v2
    x3 = x3 + v3
    x4 = x4 + v4
    for i in range(0,n):
        f[i] = fitness(x1[i],x2[i],x3[i],x4[i])
        if(f[i]<l_best_fit[i]):
            l_best_position1[i] = x1[i]
            l_best_position2[i] = x2[i]
            l_best_position3[i] = x3[i]
            l_best_position4[i] = x4[i]
            l_best_fit[i] = f[i]
        if(f[i]<g_best_fit):
            g_best_fit = f[i]
            g_best_position1 = x1[i]
            g_best_position2 = x2[i]
            g_best_position3 = x3[i]
            g_best_position4 = x4[i]
print(g_best_fit)


# In[80]:


g_best_position1*g_best_position2/(g_best_position3*g_best_position4)


# In[76]:


1/6.931


# In[81]:


print(g_best_position1,g_best_position2,g_best_position3,g_best_position4)

