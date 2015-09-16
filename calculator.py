#we can set the program to filter out undesirable values. Also test a full range of angles!
##CALCULATOR FOR PRINT SPECIFICATIONS

import csv
import sys
from globs import *
from math import *
from values import *
from Headings import *
#all lengths are in meters

#makes files: calculator, printer files, headings, values, console
#make main.py
#make function: fn(IV,const) which returns table.

#assignment statement necessary to update global var at runtime
if __name__=="__main__":
    iv, ind_var_flag,info_flag,output_type_flag = read_console() #iv is the only uninitialised global
    print(ind_var_flag,iv,info_flag,output_type_flag)

    excel_out.title_gen()
    excel_out.heading_gen()

    if output_type_flag == "c":
        console_out.print_titles(1) #console output #5 if using excel
    elif output_type_flag == "e":
        try:
            headings = open('OptimalSpecs.csv','w')
        except: #exception handling to future proof; might need to add additional code
            print("Failed to open file.")
        #with open('OptimalSpecs.csv','w') as headings:
        header = csv.DictWriter(headings,titles, delimiter = ',', dialect = 'excel')
        header.writerow(title_dict)
        writer = csv.DictWriter(headings,titles, delimiter = ',', dialect = 'excel')

    for variable in iv:
        #put in calculations for two arms
        if ind_var_flag == "d":
            v.diameter = variable;
        elif ind_var_flag == "b":
            v.build_height_angle = variable;
            v.diameter = ((-1*(v.build_height_angle + v.base_height \
             - v.ceiling_height)/cos(v.min_angle))*(2*sin(v.max_angle)))/3

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

        if output_type_flag == "c":
            #vars to print to console
            variables = [
                v.diameter,v.area,v.base_frame_length,

                v.arm_length,v.build_height,v.build_volume,

                v.arm_length_angle,v.build_height_angle,v.build_volume_angle,

                v.carr_offset,v.eff_offset,
                v.diameter_offset,v.area_offset,v.base_frame_length_offset]

            #write to console
            console_out.vars_to_print(variables)
            console_out.printer_float(variables,2)#20 when using excel

        elif output_type_flag == "e": #compare to 1 instead of elif in case need to add code
            #write to excel
            excel_out.value_generator()
            writer.writerow(written_vals)

    try:#will fail if output_type_flag is != e.
        headings.close()
    except NameError:
        pass
