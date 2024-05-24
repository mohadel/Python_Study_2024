import math

records = {
    'mms' : 850000,
    'D2' : 30000,
    'zzzzz' : 200000000000000,
    'ignition' : 5000,
    'zzzzzzzzzzzzzzz' : 13,
    'agda' :1500,
    "zzz" : 10000000000
    }

# print (records.items())
# records['D2']='not available'
# print (records.items())
# print(records['D2'])

for i in records:
    j = records[i]
    print (i , " :" , j)


def getMaxValue():
    maxvalue = 0
    currentX=0
    for x in records:
        if maxvalue < records[x]:
            maxvalue = records[x]
            currentX=x

    # print ('the highest value : ', maxvalue)
    return maxvalue, currentX

# max_key = None
# for key in records.keys():
#     if max_key:
#         if records[max_key] < records[key]:
#             max_key = key
#     else:
#         max_key = key
# print("****************************** ",max_key,": ",records[max_key])

def getMaxKey():
    maxkey=None
    for y in records:
        if str(maxkey) <y:
            maxkey=y
    # print ('the highest key :', maxkey)
    return maxkey

def getLowestValue():
    lowestvalue= float('inf')
    for z in records:
        if lowestvalue > records[z]:
           lowestvalue = records[z]
    # print ('the lowest value : ', lowestvalue)
    return lowestvalue



# for i in records:
#     if maxvalue < records[i]:
#         maxvalue = records[i]
#     if maxkey <i:
#         maxkey=i
#     if lowestvalue > records[i]:
#         lowestvalue = records[i]

   
print ('------------------------------')
# getMaxValue()
print ('the highest key is: ' , getMaxKey())
print('the highest record:' , getMaxValue())
print('the lowest value is: ' , getLowestValue())
print ('------------------------------')


# searched = input('Enter the key you are searching for: ')
# answer = ''
# for j in records:
#     if searched == j:
#         answer = records[j]
#         break
#     else: answer='item not found'
# print (searched, ' : ' , answer)
# try:
#     print(records["sdsad"])
# except Exception as e:
#     print("key not found ",e)
# print (records.get(input('Enter the key you are searching for: '),"item not found"))

# def sum_ (a):
#     try:
#         return 5+a
#     except:
#         return "validation error"
    
# print(sum_("ss"))

