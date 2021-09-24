import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


class Student(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.logger = logging.getLogger('Student')

    def sayHello(self):
        print('Hello {}'.format(self.name))
        self.logger.info('Hello {}'.format(self.name))


if __name__ == '__main__':
    student = Student('NGM', 12, 'men')
    student.sayHello()
