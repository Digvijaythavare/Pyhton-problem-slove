num = int(input("Enter the number of elements:"))
total_sum = 0

for i in range(num):
    element = float(input("Enter element :"))
    total_sum += element

average = total_sum / num

print("The average is: ",average)
