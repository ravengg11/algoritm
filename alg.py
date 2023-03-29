# algoritm

1)  
import itertools


lst=['A','B' 'C']
perms=itertools.permutation 

for perm in perms:
    
    print(perms)
    
4)

import itertools


lst=['A','B','C']
perms=itertools.product(lst, repeat=len(lst)) 

for perm in perms:
    
    print(perm)


2)
lst1=['A','B','C']
lst2=['X','Y','Z']


cartesian_product=[]


for i in lst1:
    for j in lst2:
        cartesian_product.append((i,j))
        
        
print(cartesian_product)


5)
import itertools 


set=['X','Y','Z']


for i in range(len(set)+1):
 for element in itertools.combinations(set,i):
     print(element)
     
6)
from itertools import permutations 
perms = [''.join(S) for S in permutations('ABC')]
print(perms)

7)

import itertools


s='ABC'


combinations=list(itertools.permutations(s))


print(combinations)

9)


import math
n=int(input())
math.factorial(n)
