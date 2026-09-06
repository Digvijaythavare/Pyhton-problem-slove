value_check_list = [1,2,3,4,6,7,8,9,10]

if 5 in value_check_list:
    print("5 is present in the list.")

elif 5 not in value_check_list:
    value_check_list.insert(4,5)
    print("5 has been inserted into the list.")

print("Updated list:", value_check_list)