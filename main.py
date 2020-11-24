## Nested List & indexing #
def nestedList():
    print('######## Nested List & indexing ####')
    nested = ['a', ['b', ['c'], ['d', 'e'], 'f'], 'g']
    print('This id a nested list : ', nested)
    #one level index#
    print(
        'Example for accessing elements using one level index we use nested[2] :',
        nested[2])
    print(
        'Example for accessing elements using nested index we use nested[1][2][0] :',
        nested[1][2][0])
    return nested


## list length ##
def getLength(li):
    print('######## list length ########')
    print('The length of the passed list ', li, ' is : ', len(li))


## List Membership operators ##
def ListMemeberShip(item):
    print('######## List Membership operators ########')
    list = [1, 2, 3, 4, 5]
    if (item in list):
        print(item, " is available in the list", list)
    else:  # or if ( b not in list ):
        print(item, " is not available in the list", list)


## List concatenation ##
def listConcat():
    print('######## List concatenation ########')
    list1 = ['I', ' am']
    list2 = [' wegdan ']
    print('list1 :', list1)
    print('list2 :', list2)
    print('Concatenate list , list2  :', list1 + list2)


## list slicing ##
print("###### list slicing #####")


def Listslice():
    l = [0, 10, 20, 30, 40, 50, 60]
    print(l[:3])
    # [0, 10, 20]
    print(l[3:])
    # [30, 40, 50, 60]
    print(l[:])


# [0, 10, 20, 30, 40, 50, 60]
## list itration ##
def iterate(l):
    for el in l:
        print(el)


getLength(nestedList())
print("###### list itration ######")
ListMemeberShip(3)
ListMemeberShip(9)
listConcat()
Listslice()
iterate("wegdan")
