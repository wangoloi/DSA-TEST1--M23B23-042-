# set of names that are common in both lists
common_names = set(catholic_martyrs).intersection(set(anglican_martyrs))

# Remove the common names from both lists
for name in common_names:
    catholic_martyrs.remove(name)
    anglican_martyrs.remove(name)
