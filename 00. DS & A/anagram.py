from collections import Counter
from this import s
str1 = 'listen'
str2 = 'silent'
str1_list = {}
str2_list = {}

for each in str1:
    if (each in str1_list):
        str1_list[each] += 1
    else:
        str1_list[each] = 1

for each in str2:
    if (each in str2_list):
        str2_list[each] += 1
    else:
        str2_list[each] = 1
print(str2_list)

if str2_list == str1_list:
    print("they are same")