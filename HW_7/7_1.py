# Задача про римфы: количество гласных во всех фразах должно быть одинаковым, тогда с ритмом все в порядке
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

line = (input("Введиту фразу для проверки ритма:\n"))


def check_rhythm(line):
    list_read = line.split(" ")
    quantity_of_vowels = []
    count = 0

    for word in list_read:
        for char in word:
            if str(char) == str(
                    "у" or "У" or "е" or "Е" or "ы" or "Ы" or "а" or "А" or "о" or "О" or "э" or "Э" or "я" or "Я" or "и" or "И" or "ю" or "Ю" or "ё" or "Ё"):
                count = count + 1
        quantity_of_vowels.append(count)
        count = 0

    # print(list_read)
    # print(quantity_of_vowels)
    first_vowel = quantity_of_vowels[0]
    is_rhythm = False

    for vowels in quantity_of_vowels:
        if first_vowel != vowels:
            is_rhythm = False
            break
        else:
            is_rhythm = True

    if is_rhythm == True:
        print("Парам пам-пам")
        return is_rhythm
    else:
        print("Пам парам")
        return is_rhythm


check_rhythm(line)
