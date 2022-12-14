
import json
import pickle

class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone


    def __str__(self):
        return f'{self.__firstname} {self.__lastname} {self.__phone}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(self.__str__() + '\n')

    @staticmethod
    def from_file(filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            return Person(res[0], res[1], res[2])
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])


class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group = group

    def get_group(self, group : str):
        self.__group = group
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def __str__(self):
        return f'{super().__str__()} {self.__group}'


    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_group(res[3])


class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def __str__(self):
        return f'{super().__str__()} {self.__subject}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_subject(res[3])


li = []

li.append(Student('Ivasyk', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Student('Grigoiy', 'Terkin', '+387415874165', 'Python21'))
li.append(Student('Anna', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Teacher('Borys', 'Borysov', '0991234757', 'C++17'))
li.append(Student('Svetlana', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Student('Anatloiy', 'Fedorov', '0991234756', 'C++17'))
li.append(Teacher('Anton', 'Chigur', '0991234756', 'Python11'))

for i in li
     print(i)

for i in li:
    i.to_file('test.txt')

# li[0].from_file('test.txt')





# json_object = json.load(Person, default = lambda obj: __dict__, sort_keys = True,  indent=4)
with open("test2.json", "wb")  as file:
    pickle.dump(Person, file)

with open("test2.json", "wb")  as file:
    pickle.dump(Student, file)

with open("test2.json", "wb")  as file:
    pickle.dump(Teacher, file)

with open("test2.json", "wb")  as file:
    pickle.dump(li, file)




"???????????????? ????????????????????, ???????????????????? ???????????????? ?????????????????????? ???????????????? \
?? ?????????? ????????????/?????????? ?????????????????? ?? ??????????????????????????. ???????????????? ???????????????? ???? ???????????? ????????????/???????????? ?? ????????."
