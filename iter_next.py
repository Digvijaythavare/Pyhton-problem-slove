number = [10,20,30]
inter_object = iter(number)

while True:
    try:
        print(next(inter_object))
    except:
        break    