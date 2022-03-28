from collections import OrderedDict

d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
d2 = OrderedDict({"banana": 3, "apple": 4, "pear": 1, "orange": 2})

if __name__ == "__main__":
    try:
        print(f"Normal dict: {d}")
        print(f"Pop last item: {d.popitem()}")
        print(f"Pop first item: {d.popitem(False)}") # Will generate error
    except TypeError:
        print("Invalid method call")

        print(d2)
        #print(f"Pop first item: {d2.popitem(False)}") # Will not generate error
        print(d2) # Show the first item has been removed
        d2.move_to_end("apple") # Move key to end
        print(f"Print dict: {d2}") # Show the new arrangement
        for item in d2.__reversed__():
            print(item) # Print the items from last to first

