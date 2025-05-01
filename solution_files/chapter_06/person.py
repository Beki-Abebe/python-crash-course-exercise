person1 = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
    }
person2 = {
    'first_name': 'beki',
    'last_name': 'abebe',
    'age': 27,
    'city': 'Addis Ababa',
    }

peoples = [person1, person2]
for people in peoples:
    name = f"{people['first_name'].title()} {people['last_name'].title()}"
    age = people['age']
    city = people['city'].title()
    print(f"\n{name} of {city}, is {age} years old.")