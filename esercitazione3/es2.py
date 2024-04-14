"""
date due liste di numeri, restituire la lista con
le combinazioni dei valori presenti in queste due liste,
purché questi siano diversi tra loro
"""

list1 = [1,2,3,4]
list2 = [5,1,7,8]

print([(x,y) for x in list1 for y in list2 if x!=y])

