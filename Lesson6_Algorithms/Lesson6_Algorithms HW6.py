list = [6, 20, 30, 90, 200, 300, 500, 700, 4, 3, 0]

def biggest(list, low, high):
    if low == high:
        return list[low]
    mid = low + (high - low) // 2
    if list[mid] > list[mid + 1]:
        if list[mid] > list[mid - 1]:
            return list[mid]
        else:
            return biggest(list, low, mid)
    else:
        return biggest(list, mid + 1, high)
print(biggest(list, 0, len(list) - 1))
