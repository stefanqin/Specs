from math import *

#indepen var:
class v:

    def __init__(self,name):
        self.name = name;

    diameter = 0;

    #offsets
    #use ROSTOCK MAX offsets for now
    #in m
    carr_offset = 18/1000;
    eff_offset = 33/1000;
    tot_offset = carr_offset + eff_offset;

    #VARIABLES
    area = 0;
    base_frame_length = 0;

    #simplified
    arm_length = 0;
    build_height = 0;
    build_volume = 0;

    #Including angles
    arm_length_angle = 0;
    build_height_angle = 0;
    build_volume_angle = 0;

    #including offset (& angles)
    diameter_offset = 0;
    area_offset = 0;
    base_frame_length_offset = 0;

    #CONSTANTS
    ceiling_height = 2; #doesn't account for very top of frame, which would be about 15cm
    base_height = 0.3;

    #initial elevation is the angle between build plate and arm at the center.

    init_elev_degrees = 51.5;
    init_elev = radians(init_elev_degrees);
    min_angle = asin(cos(init_elev)/2);
    max_angle = asin(3*sin(min_angle));#radians(max_angle_degrees);

    #min_angle_degrees = 19; #min_angle to print circle - based on range of rotation #can't go greater than 20??
    #sin(max_angle) = 3*sin(min_angle)
    #max_angle_degrees = 77;
    #changing min_angle



    #changing max_angle
    '''
    max_angle = radians(max_angle_degrees);
    min_angle = asin(sin(max_angle)/3.0);
    '''

    #pi = 3.1415926;

    #HEADINGS
    #CHANGE these

#when using console
    DIAMETER = "D    "
    AREA = "A    "
    BASE_FRAME_LENGTH = "BFL  "

    ARM_LENGTH_S = "AL(S)"
    BUILD_HEIGHT_S = "BL(S)"
    BUILD_VOLUME_S = "BV(S)"

    ARM_LENGTH_ANGLE = "AL(A)"
    BUILD_HEIGHT_ANGLE = "BH(A)"
    BUILD_VOLUME_ANGLE = "BV(A)"

    CARR_OFFSET = "CO   "
    EFF_OFFSET = "EO   "
    DIAMETER_OFFSET = "DO   "
    AREA_OFFSET = "AO   "
    BASE_FRAME_LENGTH_OFFSET = "BFLO "

#when using excel
'''
    DIAMETER = "Diameter(m)";
    AREA = "Area(m^2)";
    BASE_FRAME_LENGTH = "Base Frame Length(m)";

    ARM_LENGTH_S = "Arm Length (S)(m)";
    BUILD_HEIGHT_S = "Build Height(m) (S) w/ B = " + str(base_height) + "cm";
    BUILD_VOLUME_S = "Build Volume(m^3)";

    ARM_LENGTH_ANGLE = "Arm Length(m) w/ " + str(init_elev_degrees) \
    + " deg";
    BUILD_HEIGHT_ANGLE = "Build Height(m) w/ " + str(init_elev_degrees) \
    + " deg";
    BUILD_VOLUME_ANGLE = "Build Volume(m^3) w/ " + str(init_elev_degrees) \
    + " deg";

    CARR_OFFSET = "Carriage Offset=" + ("%.3f" % carr_offset) + "m";
    EFF_OFFSET = "Effector Offset=" + ("%.3f" % eff_offset) + "m";
    DIAMETER_OFFSET = "Diameter(m) w/ tot_offset=" + \
    ("%.3f" % tot_offset) + "m";
    AREA_OFFSET = "Area(m^2) w/ tot_offset=" + ("%.3f" % tot_offset) + "m";
    BASE_FRAME_LENGTH_OFFSET = "Base Frame Length(m) w/ tot_offset=" \
    + ("%.3f" % tot_offset) + "m";
    '''
