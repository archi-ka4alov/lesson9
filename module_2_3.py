my_list = [42, 69, 0, 15, 0, 5, 9, 8, -6, 5]
counter = 0
while counter <= len(my_list):
    if my_list[counter] < 0:
        break
    elif my_list[counter] > 0:
        print(my_list[counter])
    counter += 1