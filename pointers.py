num1 = 11

num2 = num1

print("Before value is udpated:")
print("num1 =", num1)
print("num2 =", num2)

num1 = 22

print("\nAfter value is udpated:")
print("num1 =", num1)
print("num2 =", num2)

dict1 = {
    'value': 11
}

dict2 = dict1

dict3 = dict2

print("Before value is udpated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

dict1['value'] = 22

print('/nAfter value is updated:')
print('dict1 =', dict1)
print('dict2 =', dict2)

# with a vairble pointed to a next vairable after the variable pointed to is updated the pointer still keeps its value
# when a dictionary pointed another the dictoanry gets updated if the main dictionary pointed values updates