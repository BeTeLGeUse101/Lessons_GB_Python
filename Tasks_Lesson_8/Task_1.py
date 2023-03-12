""" 
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной 
"""

# Определяем функцию для добавления новой записи в телефонную книгу
def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    with open("Tasks_Lesson_8/phonebook.txt", "a", encoding='utf-8') as f:
        f.write(f"{surname},{name},{patronymic},{phone_number}\n")
    print("Контакт успешно добавлен в телефонную книгу")

# Определяем функцию для вывода всех записей в телефонной книге
def print_contacts():
    with open("Tasks_Lesson_8/phonebook.txt", "r", encoding='utf-8') as f:
        contacts = f.readlines()
        if not contacts:
            print("Телефонная книга пуста")
            return
        for contact in contacts:
            surname, name, patronymic, phone_number = contact.strip().split(",")
            print(f"{surname} {name} {patronymic}: {phone_number}")

# Определяем функцию для поиска записей в телефонной книге по заданной характеристике
def find_contacts():
    characteristic = input("Введите характеристику для поиска: ")
    with open("Tasks_Lesson_8/phonebook.txt", "r", encoding='utf-8') as f:
        contacts = f.readlines()
        found_contacts = []
        for contact in contacts:
            if characteristic.lower() in contact.lower():
                found_contacts.append(contact)
        if not found_contacts:
            print("Ничего не найдено")
            return
        for contact in found_contacts:
            surname, name, patronymic, phone_number = contact.strip().split(",")
            print(f"{surname} {name} {patronymic}: {phone_number}")

# Определяем функцию для экспорта данных из телефонной книги в файл
def export_contacts():
    with open("Tasks_Lesson_8/phonebook.txt", "r", encoding='utf-8') as f:
        contacts = f.read()
    with open("exported_phonebook.txt", "w") as f:
        f.write(contacts)
    print("Телефонная книга успешно экспортирована в файл")

# Определяем функцию для импорта данных в телефонную книгу из файла
def import_contacts():
    with open("Tasks_Lesson_8/imported_phonebook.txt", "r", encoding = 'utf-8') as f:
        contacts = f.readlines()
        with open("phonebook.txt", "a") as f2:
            for contact in contacts:
                f2.write(contact)
        print("Данные успешно импортированы в телефонную книгу")

# Определяем основную функцию, которая обеспечивает взаимодействие с пользователем
def main():
    while True:
        print("\nТелефонная книга\n")
        print("1. Добавить контакт")
        print("2. Вывести все контакты")
        print("3. Найти контакт по характеристике")
        print("4. Экспортировать телефонную книгу в файл")
        print("5. Импортировать данные в телефонную книгу из файла")
        print("6. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            print_contacts()
        elif choice == "3":
            find_contacts()
        elif choice == "4":
            export_contacts()
        elif choice == "5":
            import_contacts()
        elif choice == "6":
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")


main()