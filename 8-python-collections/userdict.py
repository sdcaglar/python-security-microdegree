from collections import UserDict

user_dict = UserDict(a=1) # UserDict
norm_dict = dict(d=3) # Normal dictionary

# Direct calls function like normal dictionary
print(user_dict)
print(norm_dict)

# UserDict supports calling the underlying dictionary via "data" method
print(user_dict.data)

# Iteration over dictionary
for key in norm_dict:
    print(key, norm_dict[key])

for key in user_dict:
    print(key, user_dict[key])

# Data retrieval using items()
print(norm_dict.items())
print(user_dict.items())

