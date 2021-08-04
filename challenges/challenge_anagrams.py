def quickSort(myList, start, end):
    if start < end:
        pivot = partition(myList, start, end)
        quickSort(myList, start, pivot - 1)
        quickSort(myList, pivot + 1, end)
    return myList


def partition(myList, start, end):
    pivot = myList[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp
    temp = myList[start]
    myList[start] = myList[right]
    myList[right] = temp
    return right


def is_anagram(first_string, second_string):
    """ verifica se duas palavras são anagramas """
    if first_string == "" or second_string == "":
        return False
    if len(first_string) != len(second_string):
        return False

    return quickSort(
        list(first_string), 0, len(first_string) - 1
    ) == quickSort(list(second_string), 0, len(second_string) - 1)

# https://codezup.com/quick-sort-implementation-example-in-python/