from collections import defaultdict

pairs = [("apple", 1), ("banana", 3), ("carrot", 3), ("banana", 4), ("carrot", 1), ("banana", 4)]
def_dict = defaultdict(set) # Default factory is a set

for key, value in pairs: # Create key:value pairs from tuples
    def_dict[key].add(value)

print(sorted(def_dict.items())) # Set removed duplicate entries and combined values to singular keys


