class Course:
    def __init__(self, id_, name):
        self.__id = id_
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id_):
        self.__id = id_

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__id} - {self.__name}'
