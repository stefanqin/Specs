#read console params and update vars
#add constant var for arg[2]
#arg[3] is choosing console or excel output
#arg[4] is choosing info shown
def read_console():
    #first arg
    global info_flag
    try:
        if(sys.argv[1] is None):
            raise IndexError;
        if i[0] == "-" && len(i) == 2: #USAGE: -d, -b or -h
            if i[1] == "h":
                print(HELP_STATEMENT)
                exit(1)
            elif i[1] == "d": #iv = diameter
                iv = (diameter*0.1 for diameter in range(6,11));
                ind_var_flag = "d"
            elif i[1] == "b":#iv = build_height_angle
                iv = (build_height_angle*0.1 for build_height_angle in range(6,11));
                ind_var_flag = "b"
            else:
                print(USAGE_STATEMENT)
                exit(2)
        else:
            print(USAGE_STATEMENT)
            exit(1) #Usage error
    except:#default: iv = diameter if nothing entered
        iv = (diameter*0.1 for diameter in range(6,11));
        ind_var_flag = "d"

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
