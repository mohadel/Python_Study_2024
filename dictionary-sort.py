# Dictionary: 
names = {'Pablo': '23',
            'Leo' : '22',
            'Carla': '40',
            'Ramon':'35',
            'Paula' : '22',
            }
print('---------------------------------')
# print (names)
# for i in range (len(names)):
print (names.keys())
print (names.values())
# max_key = max(names, key=names.get) 
# max_value = names[max_key]

# print ('max value:', max_key, 'which is ', max_value)


# sorted_items = sorted(names.items(), key=lambda item: item[1])
# max_pair = sorted_items[-1]    
# print (max_pair)
maximum_ = None
for key in names.keys():
    #print("key:" , names[key], type(int(names[key])))
    if maximum_:
        if int(names[key]) > int(names[maximum_]):
            maximum_ = key
    else:
        maximum_ = key

print(maximum_)
