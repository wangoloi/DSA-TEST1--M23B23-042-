def is_martyr(name):
    # Check if the name is in either list
    if name in catholic_martyrs or name in anglican_martyrs:
        return True
    # If not, return False
    else:
        return False
