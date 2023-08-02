def create_actor(name: str = 'Райан', surname: str = 'Рейнольдс', age: int = 46, **kwargs):
    """-> {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }
    """
    output_dict = {'name': name, 'surname': surname, 'age': age}
    for key, val in kwargs.items():
        output_dict[key] = val
    return output_dict

print(create_actor(name='Jack', age=20, height = 180, movies = ['DedPool', 'Potter']))