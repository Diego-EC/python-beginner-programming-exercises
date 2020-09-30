def number_of_bottles():
    number_of_bottles = 99
    #range(5,0,-1)
    for x in range(99,0,-1):
        if x == 1:
            sentence_1 = str(x) + " bottle of milk on the wall, " + str(x) + " bottle of milk.\n" + "Take one down and pass it around, no more bottles of milk on the wall."
            sentence_2 = "No more bottles of milk on the wall, no more bottles of milk.\n" + "Go to the store and buy some more, 99 bottles of milk on the wall."
        else:
            sentence_1 = str(x) + " bottles of milk on the wall, " + str(x) + " bottles of milk."
            sentence_2 = "Take one down and pass it around, " +  str(x -1) + " bottles of milk on the wall."
        print(sentence_1)
        print(sentence_2)


number_of_bottles()