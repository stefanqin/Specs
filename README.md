# Delta-Specs-Calc
Build specification calculator for delta printer

Use this calculator to determine frame height, arm length, etc; given a desired build height + diameter.

Note: many variables are not taken into account, such as extruder weight, etc. This is not calibration, nor firmware.
It is merely a calculator you run from the shell to determine values.

Has console output or excel output.

USAGE: python3 main.py [Options].
Type python3 main.py -h for more info.

python3 main.py -h
-ind_var: #choose independent variable. const var: elevation_angle
default: -d

variables:
d = diameter
b = base_height_angle
l = arm_lengths

-output_type: #console or spreadsheet output
default: -c

variables:
c = console
e = excel
p = output to both

-info_shown... : #variable number of args. Choose variables to show
default: only diameter, area and base_frame_length shown.

Show extra variables:
s = simple (arm rotation 90 degrees)
v = virtual (emulate virtual delta machine)
o = offset (design specs w/ offset included)
A = show all

-h: #HELP_STATEMENT
Show this interface.

Note: If multiple args of the same type are passed, only the most recent is
registered.

To change defaults, enter the "values.py" file under #CONFIGURATIONS.
Please note: these OFFSETS have not been measured yet and were taken from ROSTOCK MAX firware definitions.

GOOD LUCK!
