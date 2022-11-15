import addressbook_pb2
from google.protobuf.message import Message

person = addressbook_pb2.Person()
print(person)
print(type(person))
print(person.IsInitialized())

person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME
print(addressbook_pb2.Person.WORK)
print(person.name)
print(person)

print(person.phones)
print(type(person.phones))
person.Clear()
print('after clear:', person)
# person.no_such_field = 1  # raises AttributeError
# person.id = "1234"        # raises TypeError