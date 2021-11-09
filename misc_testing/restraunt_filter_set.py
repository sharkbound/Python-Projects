from enum import auto, Flag


class Features(Flag):
    VEGETARIAN = auto()
    VEGAN = auto()
    GLUTEN_FREE = auto()
    NONE = auto()


restaurants = (
    ("joe's Gourmet Burgers", set()),
    ('Main Street Pizza Company', {Features.VEGETARIAN, Features.GLUTEN_FREE}),
    ('Corner Cafe', {Features.VEGETARIAN, Features.GLUTEN_FREE, Features.VEGAN}),
    ("Mama's Fine Italian", {Features.VEGETARIAN}),
    ("The Chef's Kitchen", {Features.VEGETARIAN, Features.GLUTEN_FREE, Features.VEGAN}),
)


def ask(msg, on_yes):
    while True:
        value = input(msg).strip().lower()
        if value in ('y', 'n'):
            return on_yes if value == 'y' else None


required = set(
    filter(None,
           [ask('vegetarian? ', Features.VEGETARIAN),
            ask('vegan? ', Features.VEGAN),
            ask('gluten free? ', Features.GLUTEN_FREE)]
           ))

print('\n\nsafe restaurants:')
for name, features in restaurants:
    if features >= required:
        print(name)
