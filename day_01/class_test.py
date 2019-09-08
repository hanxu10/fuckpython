from time import localtime, time, sleep


class Student(object):
    def __init__(self, name, age, xx = '隐藏'):
        self.name = name
        self.age = age
        self.__xx = xx

    def study(self, course_name):
        print("%s正在学习%s" % (self.name, course_name))


    def watch_movie(self):
        if self.age < 18:
            print("%s只能开《熊出没》" % (self.name))
        else:
            print("%s可以看avv" % self.name)


class Person(object):
    __slots__ = ('_name','_age','address')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('小于等于16')
        else:
            print('大于16')

class SubPerson(Person):
    __slots__ = ()
    pass


class Clock(object):
    def __init__(self, hour = 0, minute = 0, second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)

p = Person('sdf', 12)
p.play()
p.age = 22
p.play()
p.address = '难'

subp = SubPerson("玩儿", 13)
# subp.sex = '难'

clock = Clock.now()
while True:
    print(clock.show())
    sleep(1)
    clock.run()

