def number_of_bottles():
    number_of_bottles = 99
    for x in reversed(number_of_bottles):
        string = x + " bottles of milk on the wall, " + x + " bottles of milk."
        print(string)


number_of_bottles()