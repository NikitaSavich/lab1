def unique_elements(lst):
    result = []
    for item in lst:
        if type(item) == list:
            sub_elements = unique_elements(item)
            for sub_item in sub_elements:
                if sub_item not in result:
                    result.append(sub_item)
        else:
            if item not in result:
                result.append(item)
    return result
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(f"Уникальные элементы: {unique_elements(list_a)}")