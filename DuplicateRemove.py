def remove_duplicates(arr):
    result = []
    for num in arr:
        already_exists = False
        for item in result:
            if item == num:
                already_exists = True
                break
        if not already_exists:
            result.append(num)
    return result

print(remove_duplicates([1,2,2,3,4,4,5])) 
