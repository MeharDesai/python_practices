
from sys import dont_write_bytecode
l1=['a','b','c']
l2=['1','2','4']

dict1=dict(zip(l1,l2))
print(dict1)

dict2={l1[i]:l2[i] for i in range(len(l1))}
print(dict2)

dict4={}
for key in l1:
    for value in l2:
        dict4[key]=value
        l2.remove(value)
        break

print(dict4)