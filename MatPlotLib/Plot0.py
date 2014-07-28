# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 18:34:34 2014

@author: alvin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

d={'one':[1,2,3,4,5],
   'two':[4,3,2,1,5]}
df=pd.DataFrame(d)
print df
'''
x=np.arange(0,4,0.2)
y=np.exp(-x)

e1=0.1*np.abs(np.random.randn(len(y)))
plt.errorbar(x,y,yerr=e1,fmt='.-')
plt.show()
'''
'''
y=np.random.randn(1000)

plt.hist(y,50)

plt.show()
'''
'''
y=np.arange(1,3,0.5)

plt.axis(xmin=-1,xmax=6,ymax=6)
plt.plot(y,color='blue',linestyle='dashdot',linewidth=4,marker='o',markerfacecolor='red',markeredgecolor='black',markeredgewidth=3,markersize=12)
plt.show()
''''''
y=np.arange(1,3)
plt.plot(y,'y',label='yellow')
plt.plot(y+1,'m',label='magenta')
plt.plot(y+2,'c',label='cyan')
plt.legend(loc=0)
plt.grid()
plt.xlabel("hello",fontsize=19)
plt.ylabel("Yum")
plt.title("Booyah")
plt.show()
'''

'''
x=np.array([1,2,3,4,5,6])

plt.plot(x,x+1,label="+1")
plt.plot(x,x**2,label="squared")
plt.grid()

plt.legend(loc=0)
plt.title("Simple plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
''''''
#x=np.arange(0.0,4,.01)
#plt.plot(x,[i**2 for i in x ],x,[i+3 for i in x ],x,[i*4 for i in x ])
y=np.arange(1,5)

plt.plot(y,y*1.5,y,y*2)

plt.plot([2,4,6])

plt.show()

'''