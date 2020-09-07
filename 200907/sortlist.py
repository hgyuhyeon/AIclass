import copy as cp

l = "sentence"

examp = cp.copy(l)
exampl = cp.deepcopy(l)

print(id(examp), id(exampl))

#

import random as r

qlist = list(range(1,10))

print(qlist)
r.shuffle(qlist)
print(qlist)

qlist.sort() #ascending order: 오름차순
print(qlist)
qlist.sort(reverse=True) #descending order: 내림차순
print(qlist)
