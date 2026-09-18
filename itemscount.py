text = "banana" 
count = {}
for ch in text:
    if ch in count:
         count[ch] += 1
    else:
        count[ch] = 1
items = sorted(count.items())
print(items)