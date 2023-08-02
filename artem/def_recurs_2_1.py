# nested = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}
"""
def flatten_dict(nested_dict={}, flatten=None):
    if flatten is None:
        flatten = {}
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            flatten_dict({f'{key}_{sub_key}': sub_value for sub_key,
                         sub_value in value.items()}, flatten)
        else:
            flatten[key] = value
    return flatten
"""
# {'a': 1, 'b': {'c': 2, 'd': 3, 'e': {'5': {'g': 6}, '6': 100, 'f': 4, 'l': 1}}}
def flatten_dict(d: dict, k: str = '') -> dict:
    my_dict = {}
    for key, value in d.items():
        if type(value) == dict:
            my_dict.update(flatten_dict(value, k + key + '_'))
        else:
            my_dict[k + key] = value

    return my_dict


# print(flatten_dict({'Germany': {'berlin': 7},
#          'Europe': {'italy': {'Rome': 3}},
#          'USA': {'washington': 1, 'New York': 4}}))
print(flatten_dict({"a": 1,
                     "b": {
                         "c": 2,
                         "d": 3,
                         "e": {
                             "f": 4,
                             '6': 100,
                             '5': {"g": 6},
                             "l": 1,
                         }
                     }}))


assert flatten_dict({"a": 1,
                     "b": {
                         "c": 2,
                         "d": 3,
                         "e": {
                             "f": 4,
                             '6': 100,
                             '5': {"g": 6},
                             "l": 1,
                         }
                     }}) == {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 100, 'b_e_5_g': 6, 'b_e_l': 1}
