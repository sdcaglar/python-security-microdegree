from collections import defaultdict

def constant_factory(value):
    """Accept an argument and return that value to the caller object"""
    return lambda: value

def_dict = defaultdict(constant_factory("<value_unknow>")) # Generate whatever value is passed in
def_dict.update(name="Marry", action="ran") # Update dict with new keys
print(f"{def_dict['name']} {def_dict['action']} to {def_dict['object']}") # Unnamed key is provided with default value

