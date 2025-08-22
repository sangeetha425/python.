#print(list(range(15,500,3*5)))

#set => unordered ,finite ,unique elements ,heterogenous ,immutable
#it doesnt allow list in it ,it takes only immutable elements ,but set is mutable.
#it dosent allow duplicate values.
# set1={4,5,'str1',9.5,(1,2,4)}
# print(set1)

# list1=[1,1,1,2,2,2,3,3,'str1','str1']
# print(set(list1))#to remove duplicates from the list.
# print(list(set(list1)))#to convert set to list.

#Frozen set
#frozen set is immutable and it only allows immutable elements.
fset1=frozenset([1,2,3,4,5,6,6])
print(fset1)
