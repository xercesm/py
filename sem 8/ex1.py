phonebook = {}

def add_contact(name, phone_number):
    phonebook[name] = phone_number

def remove_contact(name):
    if name in phonebook:
        phonebook.pop(name)

def edit_contact(name, new_phone_number):
    if name in phonebook:
        phonebook[name] = new_phone_number

def print_phonebook():
    for name, phone_number in phonebook.items():
        print(f"{name}: {phone_number}")

add_contact("John", "123-456-7890")
add_contact("Jane", "987-654-3210")
print_phonebook()  # выводит все контакты в справочнике
remove_contact("John")
edit_contact("Jane", "555-555-5555")
print_phonebook()  # выводит все контакты после удаления и изменения данных
