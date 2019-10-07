def single_element(list1):
    solution = [value for value in list1 if list1.count(value) == 1]
    return print(solution)


list1 = [4, 8, 3, 2, 8, 1, 4, 3, 1]
single_element(list1)
