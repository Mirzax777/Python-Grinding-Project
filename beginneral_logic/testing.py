class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def demo():
    person = Person('John Doe', 30)
    for attr in dir(person):
        if not attr.startswith('__') and not callable(getattr(person, attr)):
            value = getattr(person, attr)
            print(f'{attr}: {value}')


if __name__ == '__main__':
    demo()
