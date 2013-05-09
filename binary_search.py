def binary_search(elements, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return "Not found."
    elif elements[mid] == target:
        return "Found."
    elif target < elements[mid]:
        return binary_search(elements, target, low, mid - 1)
    elif target > elements[mid]:
        return binary_search(elements, target, mid + 1, high)

items = []
for i in range(0, 100):
    items.append(i)

x = int(input("Enter number: "))
print(binary_search(items, x, 0, len(items) - 1))
