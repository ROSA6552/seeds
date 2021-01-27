import json
import time
import random


#JSON
with open("user_data.json", "r") as data_file:
    data = json.load(data_file)

with open("types_of_seeds.json", "r") as types_file:
    types = json.load(types_file)


#Money
try:
    seedbucks = data['money']
except:
    seedbucks = 100
    data.update({"money": seedbucks})



#Change of costs
try:
    print(int(time.time()))
except:
    pass



#Seeds
seeds = data['seeds']

with open("user_data.json", "w") as data_file:
    json.dump(data, data_file, indent = 4)
data_file.close()




#Machine

print('Hello,', data['name'], data['surname'], 'from', data['city'], ',', data['birthday'], 'years old')
print('You have', seedbucks, '.')
print('And seeds of:')
for i in range(1, len(seeds) + 1):
    print(seeds[str(i)]['name'])
print('\nDo you have:\n1: plant seeds\n2: harvest\n3: sale seeds')
action = int(input())
if (action == 1):
    print('The seeds have been planted)')
elif (action == 2):
    print('/harvest/')
elif (action == 3):
    print('moneyyy')
print('\n')
