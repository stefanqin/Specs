# Delta-Specs-Calc
Build specification calculator for delta printer

<b>Note: Please ignore the comments! They are for reference.</b>

Feel free to delete them.

<b>What is it?</b>

Use this calculator to determine frame height, arm length, etc; given a desired build height + diameter.

Note: many variables are not taken into account, such as extruder weight, etc. This is not calibration, nor firmware.
It is merely a calculator you run from the shell to determine values.

Has console output or excel output.

<b>USAGE:</b>
```
python3 main.py [Options].
```
Type:
```
python3 main.py -h 
```
for more info.

Note: If multiple args of the same type are passed, only the most recent is
registered.

To change defaults, enter the "values.py" file under #CONFIGURATIONS.
Please note: these OFFSETS have not been measured yet and were taken from ROSTOCK MAX firware definitions.

GOOD LUCK!
