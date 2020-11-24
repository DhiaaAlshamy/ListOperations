## Nested List & indexing #
def nestedList():
  print('#### Nested List & indexing ####')
  nested=['a',['b',['c'],['d','e'],'f'],'g']
  print('This id a nested list : ',nested)
  #one level index#
  print('Example for accessing elements using one level index we use nested[2] :',nested[2])
  print('Example for accessing elements using nested index we use nested[1][2][0] :',nested[1][2][0])
  print('#####################')
  return nested;
## list length ##
def getLength(li):
  print('#### list length ####')
  print('The length of the passed list ', li,' is : ',len(li))
  print('#####################')
## List Membership operators ##
def ListMemeberShip(item):
  list = [1, 2, 3, 4, 5 ]
  if ( item in list ):
    print (item ," is available in the list" , list)
  else: # or if ( b not in list ):
    print (item ," is not available in the list" , list)

  
getLength(nestedList())
ListMemeberShip(3)
ListMemeberShip(9)

