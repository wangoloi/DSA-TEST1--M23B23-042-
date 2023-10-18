def martyr_count(name):
    # Check if the name is in the Catholic list
    if name in catholic_martyrs:
        return "Catholic"
    # Check if the name is in the Anglican list
    elif name in anglican_martyrs:
        return "Anglican"
    # If the name is not in either list, return 'Unknown'
    else:
        return "Unknown"
