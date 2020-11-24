## Nested List #
def nestedList():
  print('#### Nested List ####')
  nested=['a',['b',['c'],['d','e'],'f'],'g']
  print('This id a nested list : ',nested)
  print('Example for accessing elements we use nested[1][2][0] :',nested[1][2][0])
  print('#####################')
  return nested;
## list length ##
def getLength(li):
  print('#### list length ####')
  print('The length of the passed list ', li,' is : ',len(li))
  print('#####################')


getLength(nestedList())
