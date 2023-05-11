def bubble_sort(list1):
    for i in range(0, len(list1)-1):
        for j in range(0, len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return (list1)


list1 = [5, 3, 2, 1, 0, 6]
print(bubble_sort(list1))
