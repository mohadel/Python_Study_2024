items = [1,2,3,4,5,6]

def search_for_item(list_,one_item):
    for x in list_:
        if x == one_item:
            return True
    return False

print (search_for_item (items,int (input ('which number you want to search for? '))))

    