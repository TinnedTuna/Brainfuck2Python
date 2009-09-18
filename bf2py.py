class BF2Py():
    def __init__(self, debug=None):
        """
            Set up the BF2Py env.
        """
        self.code = "tape = [0 for x in range(1,65536,1)]\npoint=0\n"
        self.commands = {">":("point+=1\n", (lambda : self.__nop()),), \
                    "<":("point-=1\n", (lambda : self.__nop()),), \
                    "+":("tape[point]+=1\n",(lambda : self.__nop()),),  \
                    "-":("tape[point]-=1\n", (lambda : self.__nop()),), \
                    ".":("print chr(tape[point]),\n", (lambda : self.__nop()),), \
                    ",":("tape[point] = ord(raw_input())\n", (lambda : self.__nop()),), 
                    "[":("while (tape[point] != 0):\n", (lambda : self.__incr(self,"int_level")),), \
                    "]":("\n",(lambda : self.__decr(self,"int_level")),) \
                    }
        if debug:
            self.commands["#"]=("print str(tape[:10])+\" Pointer val: \"+str(point)\n", (lambda :self.__nop()),)
        self.int_level=0 # Current indentation level of the output python code
        self.indent = "    " # Indentation
        self.cache = []
        
    def __nop(self):
        """
            Do nothing.
        """
        pass
    
    def __incr(self, obj, attr):
        """
            Increment a variable
        """
        setattr(obj, attr, (getattr(obj, attr)+1))
    
    def __decr(self, obj, attr):
        """
            Decrement a variable
        """
        setattr(obj, attr, (getattr(obj, attr)-1))
        
    def process_char(self, input_chr):
        """
            Process a single character and emit the correct Python equivalent
        """
        if input_chr in self.commands:
            # Handle the indent level
            for i in range(self.int_level):
                self.code+=self.indent
            # Add the correct code
            self.code+= self.commands[input_chr][0]
            # Perform the associated housekeeping.
            self.commands[input_chr][1]()
            
    def get_code(self):
        """
            Get the code back
        """
        return self.code
