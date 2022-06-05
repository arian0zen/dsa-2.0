"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

from http.client import HTTP_VERSION_NOT_SUPPORTED


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        #storing input string value to store in hash table
        hValue = self.calculate_hValue(string) #getting the hash value from calculated_hValue function
        if hValue != -1: #if the hash value is not -1, that means it is a valid hash value, then checking if the hash value is already in the table
            if self.table[hValue] != None: #if the hash value index of the table is not none, that means there is already a value in that i index
                self.table[hValue].append(string) #if the index is already filled, append the string to the list
            else:
                self.table[hValue] = [string]   #else if that index is empty, fill the index with the string
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        
        hValue = self.calculate_hValue(string)  #getting the hash value from calculated_hValue function
        if hValue != -1: #if the hash value is not -1, that means it is a valid hash value, then checking if the hash value is already in the table
            if self.table[hValue] != None: #if the hash value index of the table is not none, that means there is already a value in that i index
                if string in self.table[hValue]: #getting the string assigned to the index [hValue]
                    return hValue #returning the hash value! if we need to get the string we can always return string value {return string}, even we can return the whole list inside the table if there are more than one element{return self.table[hValue]}
        return -1

    def calculate_hValue(self, string):
        """Calculating the hash value according to the gives hash function that is 
        Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter"""
        
        if len(string) < 2: #the string must be of atleast 3 charecters
            print ("This is an invalid strin") #if not, then clearly saying it is invalid
        else:
            hashValue = ord(string[0])*100 + ord(string[1]) #if the string is of more than 2 chars, calculating the hash value
            return hashValue
        
        """Helper function to calulate a
        hash value from a string."""
        return -1
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hValue('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
print (hash_table.lookup('UDACITY'))





#overall time complexity for searching and adding elements is O(1).. better than most of the time complexity for searching and adding elements