class A():
    def __init__(self, a="a"):
        self.a = a

# new then init
# can use new to return dfferent class as in a factory but then init of class never runs
# new can be used to subclass built in types

from operator import itemgetter

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
            return super().__new__(cls, args)

        def __repr__(self):
            return f"""{type_name} ({", ".join(repr(arg) for arg in self)})"""

    return NamedTuple

if __name__ == "__main__":
    Point = named_tuple_factory("point", "x", "y")
    print(Point)
    point = Point(21, 42)
    print(point)
    print(point.x + point.y)
    print(dir(point))
    print(point.__class__.__name__)

