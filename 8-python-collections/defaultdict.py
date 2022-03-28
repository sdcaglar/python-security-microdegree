from collections import defaultdict

colors = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
def_dict = defaultdict(list) # Default factory is a list

# Iterate through tuples; each tuple pair is provided to the list factory
for key, value in colors:
    def_dict[key].append(value)


if __name__ == "__main__":
    # New key created for each new item in the tuple's list.
    # If a key already present, the value is added to the existing key
    print(sorted(def_dict.items()))
                          
