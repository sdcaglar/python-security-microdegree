## Section Topics

### 8.1 - Python Collections

- 01 | Sequences
    - Mutable lists and immutable tuples with associated methods
- 02 | Dictionaries
    - Hashable mappings and associated methods
- 03 | Sets
    - Mutable sets and immutable sets with associated methods

#### What are Collections?
Improving Python Containers

![collections](collections.png)

#### Container Review
Containers that have associated Collections

![Container Review](container-review.png)

#### Sequences: Common Operations

* x in s: Returns true if an item in sequence s is equeal to x; otherwise it returns
  false
* x not in s: Returns true if no item in sequence s is equeal to x; otherwise it
  returns false
* s + t: Concatenates sequence s with sequence t
  - Concatenating immutable sequences creates a new object
* s * n: This adds s to itself n times
  - Items in the sequence are not copied, but referenced multiple times
* s[i]: This retrieves the ith item in sequence s, starting from the 0th index
  - Negative numbers start counting from the end of the sequence
* s[i:j]: This retrieves a slice of s, from i (inclusive) to j (exclusive)
* s[i:j:k]: This retrieves a slice from s, from i to j, skipping k times
* len(s): This returns the length of s
* min(s): This returns the smallest item in s
* max(s): This returns the largest item in s
* s.index(x[, i[, j]]): This indexes the first instance of x in s; optionally
  it returns x at or after index i and (optionally) before index j
* s.count(x): This returns the total count of x instances in s

#### Mutable Sequence Operations

* s[i] = x: This replaces the object at index position i with object x
* s[i:j] = t: The slice from i (inclusive) to j (exclusive) is replaced with the
  contents of object t
* del s[i:j]: This deletes the contents of s from indexes i to j
* s[i:j:k] = t: This replaces the slice of i to j (stepping by k) by object t
  (t must have the same length as s)
* del s[i,j,k]: This deletes elements of the sequence as determined by the slice
  indexes and stepping, if present
* s.append(x): This adds x to the end of s
* s.clear(): This deletes all elements from the sequence
* s.copy(): This is used to shallow copy of s
* s.extend(t): Extends s with the contents of t (can also use s += t)
* s *= n: This is used to update w with its contents repeated n times
* s.insert(i, x): This inserts x into s at position i
* s.pop([i]): Extract an item at index i from s, returning it as a result and
  removing it from s (defaults to removing the last item from s)
  s.remove(x): Delete the first item from s that matches x (throws an exception if
  x is not present)
* s.reverse(): Reverse s in-place

#### Dictionaries

* len(d): This returns the number of items in a dictionary
* d[key]: This return the value associated with key
* d[key] = value: This is used to set the mapping of key to value
* del d[key]: This deletes the value associated with key
* key in d: If key exists in the dictionary, return true, otherwise return False
* key not in d: If key exists in the dictionary, return False; otherwise return True
* iter(d): This returns an iterator object from the dictionary keys. To actually
  use the iterated keys, you must use a for loop
* clear(): This removes all items from the dictionary
* copy(): This returns a shallow copy of the dictionary
* fromkeys(seq[, value]): This creates a new dictionary using the keys listed in
  seq and sets their values to value. If no value is provided, it defaults to None
* get(key[, default]): This returns the value associated with key, if key exists.
  Otherwise, the default value is returned. If default is not set, then None is
  returned, that is no response, but not an error
* items(): This returns a view object of the key:value pairs in the dictionary
* keys(): This returns a view object of just the dictionary keys
* pop(key[, default]): This is used if key exists in the dictionary; remove it
  from the dictionary and return its value; otherwise return default. If default
  isn't provided and the key doesn't exist, then an error is raised
* popitem(): This removes and returns an arbitrary pair from the dictionary. As
  Dictionaries are unsorted, the returned pair is effectively randomly selected
* setdefault(key[, default]): This is used if key is present in the dictionary,
  return its value. If not present then make a new key:value pair with the provided
  key and the default value. If default isn't set, it defaults to None
* update([other]): This modifies the dictionary by updating it with the pairs from
  other. If existing keys are present, they will be overwritten. Other can be
  another dictionary or an iterable object of key:value pairs such as a tuple
* values(): This returns a view object of the dictionaries values

#### Dictionary Views

* Dictionary views are dynamic objects that show the dictionary's items and are
  automatically updated whenever the dictionary is modified
* len(dictview): This returns the number of items in a dictionary
* item(dictview): This returns an iterator object over the dictionary keys,
  values or key:value pairs
* x in dictview: This returns True if x exists within the view object

#### Sets & Frozensets

* len(s): This returns the number of items in set s
* x in s: This returns True if x exists in s; otherwise it is False
* x not in s: This returns False if x exists in s; otherwise it is True
* isdisjoint(other): This returns True if the set has no elements in common with
  object other
* issubset(other): This tests whether all elements in the set are also in other
* issuperset(other): This tests whether all elements in other are also in set
* union(* others): This returns a new set that only contains object that are in
  common between the set and all other objects
* difference(*others): This returns a new set that is only the elements that
  exists in the set, but are not in others
* symmetric_different(other): This returns a new set of elements that are either
  in set or other but not both
* copy(): This returns a new set with a shallow copy of the set

#### Mutable Sets

* update(*others): This updates the set by adding elements from all others
* intersection_update(*others): This updates the set by keeping only the elements
  that are in the set and others
* difference_update(*others): This updates the set by keeping only the elements
  found in others
* symmetric_difference_update(other): This updates the set with only the elements
  found in either set or other, but not common to both
* add(elem): This adds elem to the set
* remove(elem): This deletes elem from the set; it throws an exception if elem
  is not present
* discard(elem): This deletes elem from the set if present

### 8.2 - OrderedDict

- 01 | OrderedDict
    - Largely deprecated in Python 3.7
- 02 | Methods
    - Three OrderedDict methods are still useful
- 03 | Examples
    - Demonstrated how normal dictionaries compare to OrderedDict collection

#### OrderedDict

Mostly redundant as of Python 3.7
  * Normal dictionaries automatically implement insertion order preservation
The methods of OrderedDict are still useful, as regular dictionaries don't include
them

#### OrderedDict Methods

* popitem(last=True): It returns and removes the key:value pair at the end of the
  dictionary. If last is not provided or manually set to True, then the popped
  value is LIFO (last in, first out). If last is set to False, then the popped
  value is FIFO.
* move_to_end(key, last=True): It moves the provided key to the end of the dictionary.
  If last is set to True, then the key moves to the right. If last is set to False,
  the key is sent to the front. If the key does not exist, an error is generated
* reversed(): Since OrderedDict objects are in order, they can be manipulated like
  an iterable object; in this case reverse iteration can be performed on an OrderedDict

#### Commands used in chapters
```
python3 ordereddict.py
# output = Normal dict: {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
           Pop last item: ('orange', 2)
           Invalid method call
           OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])
           OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])
           Print dict: OrderedDict([('banana', 3), ('pear', 1), ('orange', 2), ('apple', 4)])
           apple
           orange
           pear
           banana
```
