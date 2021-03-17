# HW5-1:

originallist = [1, 2, 3, 4, 5, 6,7,8,9]
outputlist = []
n = sum(originallist) / len(originallist)
for item in originallist:
    if item < n:
        outputlist.append(item)

print(outputlist)

# HW5-2:

list = [14, 35, 8, 61, 71, 20, 9, 2, 16, 88, 92, 70]

def find_len(list):
    length = len(list)
    list.sort()
    print("Smallest number is:", list[0])
    print("Second Smallest number is:", list[1])

Largest = find_len(list)
