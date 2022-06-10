def fractional_knapsack(values, weights, capacity):
    
    index = list(range(len(values)))
    #ratios = [v/w for v, w in zip(values, weights)]
    ratios = []
    for i in range(len(values)):
        ratios.append(values[i]/weights[i])
    #print (ratios)
    index.sort(key=lambda i: ratios[i], reverse=True)
    #print(index)
 
    max_value = 0
    fractions = [0] * len(values)
    for i in index:
        #print (i)
        #print (weights[i])
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]
            
        '''
        else:
            #fractions[i] = capacity/weights[i]
            fractions.append(capacity/weights[i])
            max_value += values[i]*capacity/weights[i]
            break
            '''
 
    print (max_value) #fractions))


'''
n = int(input('Enter number of items: '))
values = input('Enter the values items: ').split()
values = [int(v) for v in values]
print(values)
weights = input('Enter the weights: ').split()
weights = [int(w) for w in weights]
print(weights)
capacity = int(input('Enter maximum weight: '))
'''
values = [1,2,3]
weights  = [4,5,6]
capacity = 3

fractional_knapsack(values, weights, capacity)
#print('The maximum value of items that can be carried:', max_value)
#print('The fractions in which the items should be taken:', fractions)