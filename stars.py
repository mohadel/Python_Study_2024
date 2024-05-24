# def rect_stars (num1,num2):
#     for i in range (num1):
#         for i in range (num2):
#             print ('*',end="")
#         print('') 

# rect_stars(int(input('rows: ')) , int(input('columns: ')))

# def line_star (howmany_):
#     for i in range (howmany_):
#         print('*',end="")
#     print('')

# for x in range ((int(input('rows: ')))+1):
#     line_star(x)

# def triangle_stars(row_):
#     row = 0
#     for i in range(row_):
#         row += 1 
#         for x in range(row):
#             print("*",end="")
#         print("")


# triangle_stars(int(input('rows: ')))

foo = [1,2,3,4,5,6,7,8]
moo = [55,66,77,88,99,100]

def get_every2(foo_):
    for i in range (0,len(foo_),2):
        print (foo_[i])

get_every2(moo)
