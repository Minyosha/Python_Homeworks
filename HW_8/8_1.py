def search_info(data):
    information = str(input("Введите информацию для поиска:\n"))
    print("Поиск " + str(information) + " в данных:")
    for element in data:
        number_of_element = data.index(element) + 1
        exist = str(information) in element
        if exist == True:
            print("№:" + str(number_of_element) + " ФИО:" + element)
    if exist == False:
        print("Нет таких данных")


def change_user(data):
    index_for_modify = int(input("Введите индекс элемента для изменения:\n"))
    modified_user = str(input("Введите фамилию, имя, отчество и номер телефона через пробел:\n"))
    modified_user = modified_user.replace(" ", ";")
    data[index_for_modify - 1] = str(modified_user + "\n")


def add_user(data):
    added_user = str(input("Введите фамилию, имя, отчество и номер телефона через пробел:\n"))
    added_user = added_user.replace(" ", ";")
    data.append("\n" + added_user)


def delete_user(data):
    index_to_delete = int(input("Введите индекс элемента для удаления:\n"))
    data.pop(index_to_delete - 1)


def write_data(data):
    with open("contacts.txt", "w", encoding="utf-8") as file:
        file.writelines(data)


def read_data():
    with open("contacts.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        return data


def print_data(data):
    for element in data:
        number_of_element = data.index(element) + 1
        element = element.replace(";", " ")
        element = element.replace("\n", "")
        print("№:" + str(number_of_element) + " ФИО:" + element)


def print_menu():
    print("Список команд:")
    print("1. Печать базы")
    print("2. Добавить элемент")
    print("3. Изменить элемент по индексу")
    print("4. Удалить элемент по индексу")
    print("5. Поиск значения в элементах")
    print("6. Сохранить изменения")
    print("Menu. Вывести меню")
    print("Exit. Выйти")


def main():
    data = read_data()
    print("Список команд:")
    print("1. Печать базы")
    print("2. Добавить элемент")
    print("3. Изменить элемент по индексу")
    print("4. Удалить элемент по индексу")
    print("5. Поиск значения в элементах")
    print("6. Сохранить изменения")
    print("Menu. Вывести меню")
    print("Exit. Выйти")
    cmd = input("Введите команду: ")
    while cmd != "Exit":
        if cmd == "1":
            print_data(data)
        elif cmd == "2":
            add_user(data)
        elif cmd == "3":
            change_user(data)
        elif cmd == "4":
            delete_user(data)
        elif cmd == "5":
            search_info(data)
        elif cmd == "6":
            write_data(data)
        elif cmd == "Menu":
            print_menu()
        else:
            print("Такой команды нет!")
        cmd = input("Для вывода меню введите Menu. Введите команду: ")
    return


if __name__ == "__main__":
    main()
