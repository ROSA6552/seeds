import json
import time
import random
import colorama
from colorama import Fore, Style
def reset():
    print(Style.RESET_ALL)

#JSON READ:
with open("user_data.json", "r") as data_file:
    data = json.load(data_file)
with open("types_of_seeds.json", "r") as types_file:
    types = json.load(types_file)


                                #DEFS
def change_price():
    for i in range(1, 11):
        list = [-1, 1]
        random.seed()
        types[str(i)]['sale'] += random.choice(list) * int(random.random() * 4)
        if types[str(i)]['sale'] <= (types[str(i)]['purchase'] * 1):
            types[str(i)]['sale'] += int(random.random() * 4)

#Change of sale price
period = 43200
try:
    last_time = types["last_time"]
except:
    last_time = int(time.time())
    types.update({"last_time": last_time})
    change_price()

def name(index):
    return types[str(indxs_of_seeds[i])]['name']

def time_of_rise(index):
    return types[str(indxs_of_seeds[i])]['time_of_rise']

def price(index):
    return types[str(indxs_of_seeds[index])]['purchase']

def all_seed(index):
    return types[str(indxs_of_seeds[index])]

def inttime() :
    return int(time.time())

def time_of_harvest(index) :
    return data['to_harvest'][str(index)]['time_of_plant'] + data['to_harvest'][str(index)]['time_of_rise']


                                #JSON WRITE
def json_write(file):
    if (file == "data"):
        with open("user_data.json", "w") as data_file:
            json.dump(data, data_file, indent = 4)
        data_file.close()
    elif (file == "types"):
        with open("types_of_seeds.json", "w") as types_file:
            json.dump(types, types_file, indent = 4)
        types_file.close()





                                #Money
try:
    seedbucks = data['money']
    if seedbucks == None:
        seedbucks = 100
        data['money'] = seedbucks
except:
    seedbucks = 100
    data.update({"money": seedbucks})



                                #HELLO

print('Hello,', data['name'], data['surname'], 'from', data['city'], ',', data['birthday'], 'years old\n')


                                #Machine
while True:
    if (inttime() - last_time >= period):
        types.update({"last_time": last_time + period})
        last_time += period
        change_price()
    json_write("types")
    print(Fore.BLUE + time.ctime())
    print('Next change of sale prices after', last_time + period - int(time.time()), 'second\n')
    print(Fore.GREEN + 'You have', seedbucks, 'seedbucks .')
    print(Style.RESET_ALL + '\nDo you want:')
    print(Fore.YELLOW + '1: plant seeds')
    print(Fore.MAGENTA + '2: harvest the crop')
    print(Fore.GREEN + '3: sale crop')
    print(Fore.RED + '4: exit')
    reset()

    action = int(input())
    if action == 1:
        #randomazing seeds
        print(Fore.YELLOW)
        list = []
        for i in range(1, 11):
            list.append(i)
        indxs_of_seeds = random.sample(list,3)
        for i in range(3):
            print('\n', i + 1, ':', name(i), '\ntime of rise :', time_of_rise(i),
            'seconds\npurchase :', price(i), 'seedbucks')
        position = int(input())

        #buying
        if position == 1:
            if (seedbucks >= price(0)):
                seedbucks -= price(0)
                data['money'] = seedbucks

                data['to_harvest'].update({str(indxs_of_seeds[0]) : all_seed(0)})
                data['to_harvest'][str(indxs_of_seeds[0])].update({"time_of_plant" : inttime()})
                json_write("data")
            else:
                print('Not enough seedbucks')
        elif position == 2:
            if (seedbucks >= price(1)):
                seedbucks -= price(1)
                data['money'] = seedbucks

                data['to_harvest'].update({str(indxs_of_seeds[1]) : all_seed(1)})
                data['to_harvest'][str(indxs_of_seeds[1])].update({"time_of_plant" : inttime()})
                json_write("data")
            else:
                print('Not enough seedbucks')
        elif position == 3:
            if (seedbucks >= price(2)):
                seedbucks -= price(2)
                data['money'] = seedbucks

                data['to_harvest'].update({str(indxs_of_seeds[2]) : all_seed(2)})
                data['to_harvest'][str(indxs_of_seeds[2])].update({"time_of_plant" : inttime()})
                json_write("data")
            else:
                print('Not enough seedbucks')
        reset()
    elif action == 2:
        #harvesting
        count = 0
        for i in range(1, 11):
            try:
                differ = time_of_harvest(i) - inttime()
                if differ > 0:
                    print(Fore.MAGENTA + data['to_harvest'][str(i)]['name'], 'has', differ, 'seconds left')
                else:
                    print(Fore.MAGENTA + data['to_harvest'][str(i)]['name'], 'harvested')
                    data['to_sale'].update({str(i) : data['to_harvest'][str(i)]})
                    del data['to_harvest'][str(i)]
            except:
                continue
        if(count == 10):
            print(Fore.MAGENTA + 'Nothing planted')
        json_write("data")
    elif action == 3:
        #selling
        count = 0
        for i in range(1, 11):
            try:
                print(Fore.GREEN + data['to_sale'][str(i)]['name'], 'sold for', data['to_sale'][str(i)]['sale'], 'seedbucks')
                seedbucks += data['to_sale'][str(i)]['sale']
                del data['to_sale'][str(i)]
            except:
                count += 1
                continue
        if(count == 10):
            print(Fore.GREEN + 'Nothing to sell')
        data['money'] = seedbucks
        json_write("data")
    elif action == 4:
        break
    print('\n')

reset()
