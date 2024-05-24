# Set { }
numbers = [1,2,3,4,5]
first = set(numbers)
second = {2, 7, 8}
print ('first:',first)
print ('second: ', second)

print ('f-s :', first - second)
print ('s-f :', second - first)
print ('| :', first | second)
print ('& :', first & second)
print ('^ :', first ^ second)

if int(input('Enter your search: ')) in first:
    print('exists')
else:
    print ('doesn\'t exist')

# Dictionary: 
capitals = {'Argentina': 'Buenos Aires',
            'Egypt' : 'Cairo',
            'UAE': 'Abu Dhabi',
            'France':'Paris',
            'Italy' : 'Rome',
            }
print('---------------------------------')
print (capitals)
capitals.update({input('Enter the new country: '): input('capital: ')})
print (capitals)
print(capitals.get(input('Enter the country to get the capital: '),"This Country is not registered "))


#Dictionay with multiple fields

Students = {'Ahmed': [21,'egyptian','m','history']}
print (Students)

