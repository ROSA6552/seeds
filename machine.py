import json

#JSON
with open("data.json", "r") as data_file:
    data = json.load(data_file)


#Money
seedbucks = data['money']

#Seeds
seeds = data['seeds']


while(True):
    print('You have', seedbucks, '. Also', seeds['seeds1']['name'], 'and', seeds['seeds2']['name'])
    print('Do you have:\n1: plant seeds\n2: harvest\n3: sale seeds')
    action = int(input())
    if (action == 1):
        print('The seeds have been planted)')
    elif (action == 2):
        print('/harvest/')
    elif (action == 3):
        print('moneyyy')
    print('\n')
