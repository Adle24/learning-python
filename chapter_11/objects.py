# class creation
class Cat:
    def __init__(self, name):
        self.name = name


furball = Cat("Grumpy")
print(f"Our latest addition: {furball.name}")


# inheritance
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def exclaim(self):
        print("I am a Car!")


class Yugo(Car):
    def __init__(self, make, model, year, name):
        super().__init__(make, model, year)
        self.name = name

    def exclaim(self):
        print("I am a Yugo! You go not very far with me!")

    def need_push(self):
        print("A little help here?")


my_car = Car(make="Ford", model="Mustang", year=1999)
my_yugo = Yugo(make="Ford", model="Mustang", year=1999, name="Lale")

my_car.exclaim()
my_yugo.exclaim()
my_yugo.need_push()


# mixin
class PrettyMixin:
    def dump(self):
        import pprint

        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


thing = Thing()
thing.name = "Adilet"
thing.age = 20
print(thing.dump())


# attribute access
class Duck:
    acronym = "Duck"

    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def capitalized(self):
        return self.__name.upper()

    @classmethod
    def change_acronym(cls, new_acronym):
        cls.acronym = new_acronym

    @staticmethod
    def commercial():
        print("I am a Duck!")

    def __str__(self):
        return f"I am a {self.capitalized} Duck!"


fowl = Duck(input_name="Duck")

print(fowl.name)
fowl.name = "Ford"
print(fowl.name)
print(fowl.capitalized)
Duck.commercial()
print(fowl)


# composition and aggregation
class Muck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print(
            f"This muck has a {self.bill.description} bill and a {self.tail.length} tail"
        )


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, lenghth):
        self.lenghth = lenghth
