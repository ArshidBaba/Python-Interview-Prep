# Syntax: type(class_name, bases, dict)

Person = type(
    'Person',             # class name
    (object,),            # base classes (tuple)
    {                     # class body as a dictionary
        'species': 'Human',
        '__init__': lambda self, name: setattr(self, 'name', name),
        'say_hello': lambda self: print(f"Hello, I am {self.name}")
    }
)

# Using the dynamically created class
p = Person("Arshid")
p.say_hello()
print(p.species)