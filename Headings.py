from values import *
from globs import *
import sys

#read console params and update vars
def read_console():
    #first arg
    global info_flag
    for i in sys.argv:
        if i[0] == "-" && len(i) == 2: #check if correct usage
            if i[1] == "d": #iv = diameter
                iv = (diameter*0.1 for diameter in range(6,11));
                ind_var_flag = "d"
            elif i[1] == "b":#iv = build_height_angle
                iv = (build_height_angle*0.1 for build_height_angle in range(6,11));
                ind_var_flag = "b"
            else:
                print(USAGE_STATEMENT)
                exit(1) #Usage error
                '''
            else:#default: iv = diameter if anything else entered
                iv = (diameter*0.1 for diameter in range(6,11));
                ind_var_flag = "d"
                '''
        else:
            print(USAGE_STATEMENT)
            exit(1) #Usage error
    #second arg
    #more than one flag can be active
    try:
        if(sys.argv[2] is None):
            raise IndexError;
        for i in sys.argv[2:]:
            if i == "s": #simple
                info_flag[0] = 1;
            elif i == "v": #virtual
                info_flag[1] = 1;
            elif i == "o":#show offsets
                info_flag[2] = 1;
            elif i != "s" and i != "v" and i != "0": #default: [0,1,0]
                print("Argument",i,"ignored.");
    except IndexError: #default: [0,1,0]
        info_flag = [0,0,0];
    return iv, ind_var_flag,info_flag;

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
