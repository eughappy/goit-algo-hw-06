from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __eq__(self, another_value: str) -> bool:
        return self.value == another_value

class Phone(Field):
    def __init__(self, num):
        nums = re.findall(r'\d+', num)
        if (len(str(nums[0]))) == 10:
            super().__init__(num)
        else:
            print('Wrong number!')
            self.value = None
         
    def __eq__(self, another_value: str) -> bool:
        return self.value == another_value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if Phone(phone).value:
            self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print('This user has not such number. Nothing to delete!')

    def edit_phone(self, phone, new_phone):
        if phone in self.phones:
            self.phones[self.phones.index(phone)] = Phone(new_phone)
        else:
            print('This user has not such number. Nothing to change!')

    def find_phone(self, phone):
        if phone in self.phones:
            return Phone(phone)
        else:
            return 'This user has no such phone, sorry'
                

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        AddressBook.data = {}

    def add_record(self, rec:Record):
        AddressBook.data.update({rec.name.value:rec})

    def find(self,name):
        if name in AddressBook.data.keys():
            for n,p in AddressBook.data.items():
                if n == name:
                    return p
        else:
            print('No such user in adress book!')

    def delete(self,name):
        if name in AddressBook.data.keys():
            del AddressBook.data[name]


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    