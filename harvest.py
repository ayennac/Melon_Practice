############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        print(f'Code updated to new code: {new_code}')


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )

    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType(
        "cas",
        2003,
        "orange",
        True,
        False,
        "Casaba"
    )
    casaba.add_pairing("strawberries, mint")
    all_melon_types.append(casaba)

    cren = MelonType(
        "cren",
        1996,
        "green",
        True,
        False,
        "Crenshaw"
    )
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType(
        'yw',
        2013,
        "yellow",
        True,
        True,
        "Yellow Watermelon"
    )
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for item in melon.pairings:
            print(f'- {item}')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}
    
    for melon in melon_types:
        melon_dict[melon.code] = melon
    
    return melon_dict
    

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    
    def __init__(self, melon_type, shape, rating, field, farmer):
        self.melon_type = melon_type
        self.shape = shape
        self.rating = rating
        self.field = field
        self.farmer = farmer

    def is_sellable(self):
        if self.shape > 5 and self.rating > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
