def bubble(elements):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(elements)):
            if elements[i-1] > elements[i]:
                elements[i-1], elements[i] = elements[i], elements[i-1]
                swapped = True
    return elements

def quick(elements):
    if elements == []:
        return []
    else:
        pivot = elements[0]
        less = []
        great = []
        for item in elements[1:]:
            if item < pivot:
                less.append(item)
            else:
                great.append(item)

        less = quick(less)
        great = quick(great)
        return less + [pivot] + great


def insertion(elements):
    for i in range(1, len(elements)):
        cursor2 = i
        cursor1 = i - 1
        while cursor1 >= 0 and (elements[cursor2] < elements[cursor1]):
            elements[cursor2], elements[cursor1] = elements[cursor1], elements[cursor2]
            cursor2 = cursor2 - 1
            cursor1 = cursor1 - 1

    return elements

print(quick([0,2,45,1,432,12,54,2]))
print(bubble([0,2,45,1,432,12,54,2]))
print(insertion([0,2,45,1,432,12,54,2]))
