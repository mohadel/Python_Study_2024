import timeit

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=100)

tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=100)

print('list time: ', list_test)
print('tuple time: ', tuple_test)