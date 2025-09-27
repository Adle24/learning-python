# exercise 1
class Thing:
    pass


example = Thing()

print(Thing)
print(example)


# exercise 2
class Thing2:
    letters = "abc"


print(Thing2.letters)


# exercise 3
class Thing3:
    def __init__(self, letters):
        self.letters = letters


my_thing = Thing3("xyz")
print(my_thing.letters)


# exercise 4
class Element:
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def number(self):
        return self._number

    def dump(self):
        print(f"{self._name} {self._symbol} {self._number}")

    def __str__(self):
        return f"{self._name} {self._symbol} {self._number}"


my_element = {"name": "Hydrogen", "symbol": "H", "number": 1}

hydrogen = Element(**my_element)

hydrogen.dump()
print(hydrogen)
print(hydrogen.number)
print(hydrogen.symbol)
print(hydrogen.name)


# exercise 5
class Bear:
    def eats(self):
        print("Bear eats berries")


class Rabbit:
    def eats(self):
        print("Rabbit eats clover")


class Octotphore:
    def eats(self):
        print("Octotphore eats campers")


my_bear = Bear()
my_rabit = Rabbit()
my_octotphore = Octotphore()

my_octotphore.eats()
my_bear.eats()
my_rabit.eats()


# exercise 6
class Laser:
    def does(self):
        print("Disintegrate")


class Claw:
    def does(self):
        print("Crash")


class Smartphone:
    def does(self):
        print("Ring")


class Robot:
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone

    def does(self):
        self.laser.does()
        self.claw.does()
        self.smartphone.does()


my_robot = Robot(Laser(), Claw(), Smartphone())
my_robot.does()
