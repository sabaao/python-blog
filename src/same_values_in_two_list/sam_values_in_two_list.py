list_x = [1,2,3,4,5]
list_y = [3,4,5,6,7]

list_result = [value for value in list_x if value in list_y]

print(list_result) # [3, 4, 5]