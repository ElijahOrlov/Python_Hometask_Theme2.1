def find_middle(word: str) -> None:
    """
    Выводит на экран:
    * среднюю букву, если число букв в слове нечётное;
    * две средних буквы, если число букв чётное.
    :param word: слово из латинских букв
    """
    word_len = len(word)
    if word_len == 0: return

    if word_len % 2 == 0:
        start_index = (word_len // 2) - 1
        end_index = start_index + 2
    else:
        start_index = word_len // 2
        end_index = start_index + 1

    print(word[start_index:end_index])


find_middle('test')
find_middle('testing')
