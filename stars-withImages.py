from PIL import Image
# Load an image
# img = Image.open('image.jpg')
# # Display the image
# img.show()

def rect_stars (num1,num2):
    for i in range (num1):
        for i in range (num2):
            print ('*',end="")
        print('') 

rect_stars(int(input('rows: ')) , int(input('columns: ')))

def line_star (howmany_):
    for i in range (howmany_):
        print('*',end="")
    print('')

for x in range ((int(input('rows: ')))+1):
    line_star(x)

def triangle_stars(row_):
    row = 0
    for i in range(row_):
        row += 1 
        for x in range(row):
            print("*",end="")
        print("")


triangle_stars(int(input('rows: ')))

