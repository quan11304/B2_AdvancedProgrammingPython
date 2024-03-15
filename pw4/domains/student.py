class Student:
    def __init__(self, id_, name, dob):
        self.__id = id_
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def set_id(self, id_):
        self.__id = id_

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def __str__(self):
        return f'{self.__id} - {self.__name} - {self.__dob}'
