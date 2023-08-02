def info_kwargs(**kwargs):
    output_dict = dict()
    for key, val in kwargs.items():
        output_dict[key] = val

    for key, val in sorted(output_dict.items()):
        print(f'{key} = {val}')

info_kwargs(first_name="John", last_name="Doe", age=33)
