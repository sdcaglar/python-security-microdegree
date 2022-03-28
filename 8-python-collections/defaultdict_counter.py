from collections import defaultdict

string = "Mississippi and Alabama"
def_dict = defaultdict(int) # Default factory is integer

# For each character in string, increment a counter for that character
for key in string:
    def_dict[key] += 1

if __name__ == "__main__":
    print(sorted(def_dict.items()))

