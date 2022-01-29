from collections import Counter
list1 = [1,2,3,2,1]
dict1 = Counter(list1)
print(dict1)
duplist = [key for (key,value) in dict1.items()if value >1]
for item in list1:
    if item in duplist:
        print ('first dup',item )
        break