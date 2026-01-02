class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_puppy(self):
        if self.age < 2:
            return True