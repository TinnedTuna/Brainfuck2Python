import bf2py
import sys

def main():
    out_file = sys.argv[2]
    in_file = sys.argv[1]
    flag = False
    try:
        if sys.argv[3] == "-d":
            debug = True
        else: 
            debug = False
    except:
        debug = False
    converter = bf2py.BF2Py(debug)
    
    for line in open(in_file,"r").readlines():
        line_arr = [x for x in str(line)]
        for char in line_arr:
            converter.process_char(char)
        
    ofile = open(out_file,"w")
    ofile.write(converter.get_code())
    ofile.close()
    
if (__name__=="__main__"):
    main()
            