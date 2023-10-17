def looping_func(range, current):
    print(current)
    current += 1

    if(current < range - 1):
        return looping_func(range, current)
    return current

print(looping_func(5, 0))

