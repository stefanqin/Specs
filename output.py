from values import *
from globs import *
import sys

#console output
class ConsoleOut:#init is not required since will only be using method atrr

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
class ExcelOut:
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
        written_vals[v.DIAMETER] = "%.2f" % v.diameter;
        written_vals[v.AREA] = "%.2f" % v.area;
        written_vals[v.BASE_FRAME_LENGTH] = "%.2f" % v.base_frame_length;
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
