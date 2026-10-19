def merge_dicts(dict_a, dict_b):
    for key, val_b in dict_b.items():
        if key in dict_a:
            val_a = dict_a[key]
            if type(val_a) == dict and type(val_b) == dict:
                merge_dicts(val_a, val_b)
            elif type(val_a) == list and type(val_b) == list:
                dict_a[key] = val_a + val_b
            elif type(val_a) == set and type(val_b) == set:
                dict_a[key] = val_a | val_b
            elif type(val_a) == tuple and type(val_b) == tuple:
                dict_a[key] = val_a + val_b
            else:
                dict_a[key] = val_b
        else:
            dict_a[key] = val_b
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(f"Результат слияния словарей: {dict_a}")