# Delta-Specs-Calc
Build specification calculator for delta printer

Use this calculator to determine frame height, arm length, etc; given a desired build height + diameter.

Note: many variables are not taken into account, such as extruder weight, etc. This is not calibration, nor firmware.
It is merely a calculator you run from the shell to determine values.

Has console output or excel output.

USAGE: python3 calculator.py independent_var constant_var [info_shown ...]
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

Please note: these OFFSETS have not been measured yet and were taken from ROSTOCK MAX firware definitions.

GOOD LUCK!
