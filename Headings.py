from values import *
from globs import *
import sys

#read console params and update vars
#add constant var for arg[2]
#arg[3] is choosing console or excel output
#arg[4] is choosing info shown
#optional params
#make another console file
def read_console():

    indep_var = False;

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
            #check independent and const vars
            if indep_var == False:
                #Variable
                if i[1] == "d": #iv = diameter
                    iv = (diameter*0.1 for diameter in range(6,11));
                    ind_var_flag = "d"
                    indep_var == True;
                elif i[1] == "b":#iv = build_height_angle
                    iv = (build_height_angle*0.1 for build_height_angle in range(6,11));
                    ind_var_flag = "b"
                    indep_var == True;
            else:
                #code for const var here
                True;

            #output switch
            if i[1] == "c":#console
                output_type_flag = "c"
            elif i[1] == "e": #spreadsheet
                output_type_flag = "e"

            #show info
            if i[1] == "s": #simple
                info_flag[0] = 1;
            elif i[1] == "v": #virtual
                info_flag[1] = 1;
            elif i[1] == "o":#show offsets
                info_flag[2] = 1;
            #dealing with nonsensical arg
            elif i[1] not in ["h","d","b","c","e","s","v","o"]:
                print("Argument",i,"ignored.");
        else:
            print("Argument",i,"ignored.");
        #return iv, ind_var_flag,info_flag,output_type_flag;
    return iv, ind_var_flag,info_flag,output_type_flag

#console output
class console_out:
    def __init__(self,name):
        self.name = name;
    #choose vars to print
    def vars_to_print(variables):
        if info_flag[0] == 0: #simple
            variables.remove(v.arm_length);
            variables.remove(v.build_height);
            variables.remove(v.build_volume);
        if info_flag[1] == 0: #virtual
            variables.remove(v.arm_length_angle);
            variables.remove(v.build_height_angle);
            variables.remove(v.build_volume_angle);
        if info_flag[2] == 0:
            variables.remove(v.carr_offset);
            variables.remove(v.eff_offset);
            variables.remove(v.diameter_offset);
            variables.remove(v.area_offset);
            variables.remove(v.base_frame_length_offset);
    #print titles
    def print_titles(n):
        for i in titles:
            print(i,end=(' '*n));
        print("\n")#"%.2f" %
    #print variables
    def printer_float(list_vars,n):
        for i in list_vars:
            print("%.2f" % i,end=(' '*n)); #choose spacing size
        print("\n")

#excel output
class excel_out:
    def __init__(self,name):
        self.name = name;
    #removes unwanted headings
    def title_gen():
        if info_flag[0] == 0: #simple
            titles.remove(v.ARM_LENGTH_S);
            titles.remove(v.BUILD_HEIGHT_S);
            titles.remove(v.BUILD_VOLUME_S);
        if info_flag[1] == 0: #virtual
            titles.remove(v.ARM_LENGTH_ANGLE);
            titles.remove(v.BUILD_HEIGHT_ANGLE);
            titles.remove(v.BUILD_VOLUME_ANGLE);
        if info_flag[2] == 0:
            titles.remove(v.CARR_OFFSET);
            titles.remove(v.EFF_OFFSET);
            titles.remove(v.DIAMETER_OFFSET);
            titles.remove(v.AREA_OFFSET);
            titles.remove(v.BASE_FRAME_LENGTH_OFFSET);
    #generate headings
    def heading_gen():
        for i in titles:
            title_dict[i] = i;
    #return dictionary for excel row writing reference
    def value_generator():
        if info_flag[0] == 1:
            written_vals[v.ARM_LENGTH_S] = "%.2f" % v.arm_length;
            written_vals[v.BUILD_HEIGHT_S] = "%.2f" % v.build_height;
            written_vals[v.BUILD_VOLUME_S] = "%.2f" % v.build_volume;
        if info_flag[1] == 1:
            written_vals[v.ARM_LENGTH_ANGLE] = "%.2f" % v.arm_length_angle;
            written_vals[v.BUILD_HEIGHT_ANGLE] = "%.2f" % v.build_height_angle;
            written_vals[v.BUILD_VOLUME_ANGLE] = "%.2f" % v.build_volume_angle;
        if info_flag[2] == 1:
            written_vals[v.CARR_OFFSET] = "%.2f" % v.carr_offset;
            written_vals[v.EFF_OFFSET] = "%.2f" % v.eff_offset;
            written_vals[v.DIAMETER_OFFSET] = "%.2f" % v.diameter_offset;
            written_vals[v.AREA_OFFSET] = "%.2f" % v.area_offset;
            written_vals[v.BASE_FRAME_LENGTH_OFFSET] = "%.2f" % \
            v.base_frame_length_offset;
