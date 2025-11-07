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

class_code = """
class Animal:
    def __init__(self, species):
        self.species = species
        
    def speak(self):
        print(f"I am a {self.species}")
"""

# Execute in a local dictionary to capture the class
namespace = {}
exec(class_code, globals(), namespace)

# Retrieve the created class
Animal = namespace['Animal']

a = Animal("Cat")
a.speak()