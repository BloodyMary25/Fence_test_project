
def create_groups():
    fencers = input("Введите имена бойцов через пробел: ")
    fencers = fencers.split()
    fencers = list(map(str, fencers))
    # print("Список участников:", fencers)
    if len(fencers) == 18:
        print('Набрано достаточное количество бойцов (18 человек)')
        print("Список участников:", fencers)


    elif len(fencers) > 18:
        print(f'Ввели слишком много участников, {len(fencers)} вместо 18')
        return create_groups()

    elif len(fencers) < 18:
        print(f'Недостаточное количество бойцов! Вы ввели {len(fencers)} участников.')
        return create_groups()



create_groups()
