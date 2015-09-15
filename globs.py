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

global titles;
global variables

USAGE_STATEMENT = "USAGE: python3 calculator.py independent_var constant_var [info_shown ...].\nType python3 calculator.py -h for more info."

title_dict = {};
written_vals = {};
ind_var_flag = ""
#initialise generator IV here -> dunno how to yet

titles = [
    v.DIAMETER, v.AREA, v.BASE_FRAME_LENGTH,

    v.ARM_LENGTH_S, v.BUILD_HEIGHT_S, v.BUILD_VOLUME_S,

    v.ARM_LENGTH_ANGLE, v.BUILD_HEIGHT_ANGLE, v.BUILD_VOLUME_ANGLE,

    v.CARR_OFFSET,v.EFF_OFFSET,v.DIAMETER_OFFSET,
    v.AREA_OFFSET,v.BASE_FRAME_LENGTH_OFFSET]

info_flag = [0,0,0]#default

#variables to print in console
variables = [
    v.diameter,v.area,v.base_frame_length,

    v.arm_length,v.build_height,v.build_volume,

    v.arm_length_angle,v.build_height_angle,v.build_volume_angle,

    v.carr_offset,v.eff_offset,
    v.diameter_offset,v.area_offset,v.base_frame_length_offset]

'''
independent_var: #choose independent variable
d = diameter
b = base_height_angle
e = elevation_angle
l = arm_length

constant var: #choose constant
see (independent_var)

[info_shown ...]: #variable number of args.
s = simple (arm rotation 90 degrees)
v = virtual (emulate virtual delta machine)
o = offset (design specs w/ offset included)
'''
