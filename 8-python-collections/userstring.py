from collections import UserString

class AppendString(UserString):
    """Take a sequence and return the instance data, concatenated with
    the sequence argument"""
    def append(self, string):
        self.data = self.data + string


if __name__ == "__main__":
    s = AppendString("banana-foster")
    s.append("spam and pineapples")
    print(s)
    new_s = "banana"
    new_s.append("apples") # Normal strings don't have append() function
    print(new_s)

