from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print("%s汪汪汪" % self._nickname)

class Cat(Pet):
    def make_voice(self):
        print("%s喵喵喵" % self._nickname)

xx = [Dog("gougou"), Cat("maomao")]
for pet in xx:
    pet.make_voice()