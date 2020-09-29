import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    example_color = 1
    students_array = ["uno", "dos", "tres", "cuatro", "cinco", 
    "seis", "siete", "ocho", "nueve", "diez"]
    #your loop here
    colors = []
    for x in students_array:
        colors.append(get_color(random.randint(1,4)))

    return colors




print(get_allStudentColors())