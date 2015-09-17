#THIS IS A CALCULATOR FOR BUILD SPECIFICATIONS
#all lengths are in meters
#configuration of values: go to values.py

import csv
from globs import *
from math import *
from values import *
from output import *
from consoleargs import *

#angle maths
#can add filter out undesirable values

#assignment statement necessary to search module scope rather than local scope
def main():
    global USAGE_STATEMENT;
    #TITLES
    global title_dict;
    global written_vals;
    global iv; #independent var chosen -> generator obj HOW DO YOU INITIALISE THIS??
    global ind_var_flag; #console switch (one at a time)
    global info_flag; #output flag (independent flags)
    global output_type_flag;
    global titles;
    global variables

    #default if no cmd args
    try:
        iv, ind_var_flag,info_flag,output_type_flag = \
        ConsoleRead.read_console()
    except TypeError:
        pass
    #print(ind_var_flag,iv,info_flag,output_type_flag) #for debugging purposes only

    ExcelOut.title_gen()
    ExcelOut.heading_gen()

    if output_type_flag == "c" or output_type_flag == "p":
        ConsoleOut.print_titles(1) #console output #5 if using excel
    if output_type_flag == "e" or output_type_flag == "p":
        try:
            headings = open('OptimalSpecs.csv','w')
        except OSError: #exception handling to future proof; might need to add additional code
            print("Failed to open file.")
            exit(3)
        #with open('OptimalSpecs.csv','w') as headings:
        header = csv.DictWriter(headings,titles,
        delimiter = ',', dialect = 'excel')
        header.writerow(title_dict)
        writer = csv.DictWriter(headings,titles,
        delimiter = ',', dialect = 'excel')

#note: if we put the calcs in a sepearate module, we'd need to make class v global
    for variable in iv:

        #algorithm for calculating based on ind_var, etc.
        #put in calculations for two arms
        if ind_var_flag == "d":#iv: diam, const: elevation
            v.diameter = variable;
        elif ind_var_flag == "b": #iv: BHA, Const: elevation
            v.build_height_angle = variable;
            v.diameter = ((-1*(v.build_height_angle + v.base_height \
             - v.ceiling_height)/cos(v.min_angle))*(2*sin(v.max_angle)))/3
        if ind_var_flag == "l": #iv: AL, const: elevation
            v.arm_length_angle = variable
            v.diameter = v.arm_length_angle*2*sin(v.max_angle)/3

        #value calculations
        v.area = pi*(v.diameter*0.5)**2
        v.base_frame_length = v.diameter*(3**0.5)

        #simple
        v.arm_length = v.diameter*(3**0.5)
        v.build_height = v.ceiling_height - v.base_height - v.arm_length
        v.build_volume = pi*(v.diameter*0.5)**2*v.build_height

        #include angle
        v.arm_length_angle = \
        (3*v.diameter)/(2*sin(v.max_angle)); #diameter/(2*sin(min_angle))

        v.build_height_angle = v.ceiling_height - \
        v.arm_length_angle*cos(v.min_angle) - v.base_height;
        v.build_volume_angle = pi*(v.diameter*0.5)**2*v.build_height_angle;

        v.diameter_offset = v.diameter + v.tot_offset
        v.area_offset = pi*(v.diameter_offset*0.5)**2
        v.base_frame_length_offset = v.diameter_offset*(3**0.5)

        if output_type_flag == "c" or output_type_flag == "p":
            #vars to print to console
            variables = [
                v.diameter,v.area,v.base_frame_length,

                v.arm_length,v.build_height,v.build_volume,

                v.arm_length_angle,v.build_height_angle,v.build_volume_angle,

                v.carr_offset,v.eff_offset,
                v.diameter_offset,v.area_offset,v.base_frame_length_offset]

            #write to console
            ConsoleOut.vars_to_print(variables)
            ConsoleOut.printer_float(variables,2)

        if output_type_flag == "e" or output_type_flag == "p":
            #write to excel
            ExcelOut.value_generator()
            writer.writerow(written_vals)

    try:#will fail if output_type_flag is != e (i.e file was never opened)
        headings.close()
    except NameError:
        pass

if __name__=="__main__":
    main()
