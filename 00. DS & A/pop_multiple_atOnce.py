def stPop(stack):
    if(pop<=0):
        return 0;
    else:
        for i in range(0,pop):
            stack.pop()
stack=[]
numOfElement=int(input('Enter number of elemnets to be inserted:\n'))

print('Enter the elements to fill the stack:')
for i in range(0,numOfElement):
    i=int(input())
    stack.append(i)

print('The stack is',stack)

pop=int(input('Enter the number of elements you eant to pop'))
stPop(stack)
# if(pop<=0):
#     print('no items to be popped')
# else:
#     for i in range(0,pop):
#         stack.pop()

print('after popping elemets',stack)