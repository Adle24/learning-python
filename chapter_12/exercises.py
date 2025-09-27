from collections import defaultdict, OrderedDict


# exercise 1
dict_of_lists = defaultdict(list)
dict_of_lists["a"].append("something for a")
print(dict_of_lists["a"])

# exercise 2
plain = {"a": 1, "b": 2, "c": 3}
print(plain)

ordered_dict = OrderedDict(plain)
print(ordered_dict)
