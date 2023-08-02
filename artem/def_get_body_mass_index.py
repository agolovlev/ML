def get_body_mass_index(mass, growth):
    bodyIndex = mass / ((growth/100) ** 2)
    if bodyIndex < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= bodyIndex <= 25:
        print('Норма')
    else:
        print('Избыточная масса тела')

get_body_mass_index(82, 182)

