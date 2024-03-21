def insert_number(lst, num, index):
    lst.insert(index, num)
    return lst
my_list = [1, 2, 3, 4, 5]
number_to_insert = 10
index_to_insert = 2
result = insert_number(my_list, number_to_insert, index_to_insert)
print("List after insertion:",result)
