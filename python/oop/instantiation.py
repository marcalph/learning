from operator import itemgetter

class A():
    def __init__(self, a="a"):
        self.a = a

# new then init
# new can be used to subclass immutable builtin types
class Distance(float):
    def __new__(cls, value, unit):
       instance =  super().__new__(cls, value)
       instance.unit = unit
       return instance
d = Distance(6, "km")    
print(d)

# can use new to return dfferent class as in a factory but then init of class never runs
from random import choice
class Pet:
    def __new__(cls):
        other = choice([Dog, Cat])
        instance = super().__new__(other)
        return instance
    
    def communicate(self):
        pass
    
    def __init__(self):
        print("this never runs")

class Dog():
    def communicate(self):
        print("woof")

class Cat():
    def communicate(self):
        print("meow")

pet = Pet()
pet.communicate()
print(isinstance(pet, Pet))

 
# singleton pattern 
# beware of this apttern with an init 
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

        
# emulate named_tuple
def named_tuple_factory(type_name, *fields):
    num_fields = len(fields)

    class NamedTuple(tuple):
        __slots__ = ()

        def __new__(cls, *args):
            if len(args) != num_fields:
                raise TypeError(
                    f"{type_name} expected exactly {num_fields} " 
                    f"arguments, got {len(args)}"
                )
            cls.__name__ = type_name
            for index, field in enumerate(fields):
                setattr(cls, field, property(itemgetter(index)))
            return super().__new__(cls, args)  # acces tuple.__new__()

        def __repr__(self):
            return f"""{type_name} ({", ".join(repr(arg) for arg in self)})"""

    return NamedTuple


Point = named_tuple_factory("point", "x", "y")
print(Point)
point = Point(21, 42)
print(point)
print(point.x + point.y)
print(dir(point))
print(point.__class__.__name__)

