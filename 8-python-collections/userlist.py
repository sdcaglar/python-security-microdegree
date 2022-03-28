from collections import UserList

class ExtendedList(UserList):
    """Class that allows a list to be added to via value assignment,
    rather than using append().

    If key equals length of list a new value is appended. Otherwise the
    existing value is overwritten. """
    def __setitem__(self, key, value):
        if key == len(self.data):
            self.data.append(value)
        else:
            self.data[key] = value

if __name__ == "__main__":
    ext_list = ExtendedList()
    for i in range(10):
        ext_list[i] = i

    print(f"Unmodified list: {ext_list}")
    ext_list[10] = 10
    print(f"Modified last value: {ext_list}")
    ext_list[2] = 42
    print(f"Modified index 2: {ext_list}")
    ext_list[12] = 90 # Accessing index beyond list length results in error
    print(f"Modified non-existent index: {ext_list}")

