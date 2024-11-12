def find_best_couples(boys: list, girls: list) -> None:
    """
    Поиск лучших рекомендаций пар
    :param boys: список имен юношей
    :param girls:  список имен девушек
    """
    boys_count = len(boys)
    girls_count = len(girls)
    if boys_count != girls_count:
        print("Внимание, кто-то может остаться без пары!")
        return

    print("Идеальные пары:")
    for boy, girl in zip(sorted(boys), sorted(girls)):
        print(f"{boy} и {girl}")


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
find_best_couples(boys, girls)

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
find_best_couples(boys, girls)