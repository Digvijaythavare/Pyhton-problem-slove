words = ["apple", "banana", "cherry", "date", "fig", "grape"]

count = 0

for word in words:
    for ch in word:
        if word.startswith("a"):
            count +=1
print(count)
