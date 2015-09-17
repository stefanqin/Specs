from values import * #is this import necessary?
from globs import *
import sys

#the reason why a lot of these don't work is because i'm rebinding immutable objects

class ConsoleRead:
    #no need for init function as not initialising an instance, ever.
    minimum = [0,"minimum"];
    maximum = [0,"maximum"];
    step = [0,"step"];
    most_dec_places = set()

    #check number of decimal places in a number
    def check_decimals(num):
        num_dec_places = 0
        number_dec_places = 0

        while num % 1 != 0:
            num *= 10; #ints are immutable. This is reassignment
            #this points to a new object with a value + 1 greater than the previous
            #referenced by num_dec_places
            num_dec_places += 1;
        ConsoleRead.most_dec_places.add(num_dec_places)
        print(ConsoleRead.most_dec_places)

    #Ask user for a number and return it. Used for configuring range.
    def take_number(string,variable_string):
        number = 0

        while True:
            try:
                number = float(input("Enter the " + string + " " +\
                variable_string + ' in m:\n'))
                if number < 0:
                    raise ValueError;
                ConsoleRead.check_decimals(number)
                return number
            except ValueError:
                print("Please enter a valid number. ")
                continue

    #run if variable flag is given
    def take_input(variable_string):
        global iv

        max_dec_places = 0;

        def_or_not = input("Press d to use defaults,"
        " any other key to continue.\n")

        if def_or_not == "d":
            return
        else:
            ConsoleRead.minimum[0] = ConsoleRead.take_number(\
            ConsoleRead.minimum[1],variable_string)

            ConsoleRead.maximum[0] = ConsoleRead.take_number(\
            ConsoleRead.maximum[1],variable_string)

            ConsoleRead.step[0] = ConsoleRead.take_number(\
            ConsoleRead.step[1],variable_string)

            max_dec_places = int(10**max(ConsoleRead.most_dec_places))
            #homogenise number of digits
            ConsoleRead.minimum[0] = int(ConsoleRead.minimum[0]*max_dec_places)
            ConsoleRead.maximum[0] = int(ConsoleRead.maximum[0]*max_dec_places)
            ConsoleRead.step[0] = int(ConsoleRead.step[0]*max_dec_places)

            iv = ((some_var/max_dec_places) \
            for some_var in range(ConsoleRead.minimum[0],
            ConsoleRead.maximum[0],ConsoleRead.step[0]));

    #read command line args
    def read_console():

        #when we run this function, the variables haven't been declared
        #in the script yet. Get rid of this to test

        global output_type_flag
        global info_flag
        global iv
        global ind_var_flag

        #first arg
        for i in sys.argv[1:]:
            if i[0] == "-" and len(i) == 2:
                #HELP_STATEMENT
                if i[1] == "h":
                    print(HELP_STATEMENT)
                    exit(1)

                #Variable
                if i[1] == "d": #iv = diameter
                    iv = (diameter*0.1 for diameter in range(6,11));
                    ind_var_flag = "d"
                    ConsoleRead.take_input("diameter")
                elif i[1] == "b":#iv = build_height_angle
                    iv = (build_height_angle*0.1 for build_height_angle in range(6,11));
                    ind_var_flag = "b"
                    ConsoleRead.take_input("build_height")
                elif i[1] == "l": #iv = arm_length_angle
                    iv = (arm_length_angle*0.1 for arm_length_angle in range(9,20))
                    ind_var_flag = "l"
                    ConsoleRead.take_input("arm_length")

                #output switch
                if i[1] == "c":#console
                    output_type_flag = "c"
                elif i[1] == "e": #spreadsheet
                    output_type_flag = "e"
                elif i[1] == "p": #print to both
                    output_type_flag = "p"

                #show info
                if i[1] == "A": #print all extra vars
                    #note: this way (rather than info_flag = [1,1,1]) mutates rather than rebinds
                    info_flag[0] = 1
                    info_flag[1] = 1
                    info_flag[2] = 1
                elif i[1] == "s": #simple
                    info_flag[0] = 1;
                elif i[1] == "v": #virtual
                    info_flag[1] = 1;
                elif i[1] == "o":#show offsets
                    info_flag[2] = 1;
                #dealing with nonsensical arg
                elif i[1] not in ["h","d","b","l","c","e","A","s","v","o","p"]:
                    print("Argument",i,"ignored.");
            else:
                print("Argument",i,"ignored.");
        return iv, ind_var_flag,info_flag,output_type_flag;
        #return iv, ind_var_flag,info_flag,output_type_flag
