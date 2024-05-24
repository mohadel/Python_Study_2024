answer = 3
# for i in range(4):
#     entered = input('Enter a number: ')
#     if int(entered)==answer:
#         print('Correct!!!')
#         break
#     else:
#         if i ==3 :
#             print ('Exceeded number of trials')
#         else: 
#             print('Try again!')


entered=int(input('Enter a number: '))
while entered != answer:
    if entered < answer:
        print ('increase')
    elif entered > answer:
        print ('reduce')
    #else: break
    entered = int(input('Enter a number: '))
