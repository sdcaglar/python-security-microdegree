from collections import defaultdict

colors = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
def_dict = defaultdict(list) # Default factory is list

for key, value in colors: # Iterate through tuples; each tuple pair is provided to the list factory
    def_dict[key].append(value)

if __name__ == "__main__":
    print(sorted(def_dict.items())) # New key created for each new item int the tuple's list.
    # If a key already present, the value is added to the existing key.

