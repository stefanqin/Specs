from values import *

global USAGE_STATEMENT;
#TITLES
global title_dict;
global written_vals;
global iv; #independent var chosen -> generator obj
global ind_var_flag; #console switch (one at a time)
#Info_flag controls what's shown, not what's calculated
#info_flag uses flags since more than one can be active
#flags are: [0,0,0] = [simple, virtual, offset]
global info_flag; #output flag (independent flags)
global output_type_flag;

global titles;
global variables

USAGE_STATEMENT = "USAGE: python3 calculator.py [Options].\nType python3 calculator.py -h for more info."

title_dict = {};
written_vals = {};
ind_var_flag = "d"
#initialise generator IV here -> dunno how to yet
info_flag = [0,0,0]#default
output_type_flag = "c"; #c for console, e for excel
iv = range(6,11)

titles = [
    v.DIAMETER, v.AREA, v.BASE_FRAME_LENGTH,

    v.ARM_LENGTH_S, v.BUILD_HEIGHT_S, v.BUILD_VOLUME_S,

    v.ARM_LENGTH_ANGLE, v.BUILD_HEIGHT_ANGLE, v.BUILD_VOLUME_ANGLE,

    v.CARR_OFFSET,v.EFF_OFFSET,v.DIAMETER_OFFSET,
    v.AREA_OFFSET,v.BASE_FRAME_LENGTH_OFFSET]

#variables to print in console
variables = [
    v.diameter,v.area,v.base_frame_length,

    v.arm_length,v.build_height,v.build_volume,

    v.arm_length_angle,v.build_height_angle,v.build_volume_angle,

    v.carr_offset,v.eff_offset,
    v.diameter_offset,v.area_offset,v.base_frame_length_offset]

HELP_STATEMENT = '''
    -ind_var const_var: #choose independent variable, followed by const_var
    default: -d e

    variables:
    d = diameter
    b = base_height_angle
    a = elevation_angle
    l = arm_lengthss

    -output_type: #console or spreadsheet output
    default: -c

    variables:
    c = console
    e = spreadsheet
    p = output to both

    -info_shown... : #variable number of args. Choose variables to show
    default: only diameter, area and base_frame_length shown.

    Show extra variables:
    s = simple (arm rotation 90 degrees)
    v = virtual (emulate virtual delta machine)
    o = offset (design specs w/ offset included)

    -h: #HELP_STATEMENT
    Show this interface.

    Note: If multiple args of the same type are passed, only the most recent is
    registered.
    '''
