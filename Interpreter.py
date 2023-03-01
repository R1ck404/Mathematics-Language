class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {"print", "log", "write"}

    def interpret(self, code):
        lines = code.split('\n')
        for line in lines:
            if not line.startswith('#'):
                tokens = line.split()
                if tokens:
                    if tokens[0] == "var":
                        if len(tokens) < 4 or tokens[2] != "is":
                            raise SyntaxError("Invalid variable declaration: {}".format(line))
                        self.variables[tokens[1]] = " ".join(tokens[3:])
                    else:
                        variable_name = tokens[0]
                        if variable_name not in self.functions:
                            if variable_name not in self.variables:
                                raise SyntaxError("Undefined variable: {}".format(variable_name))
                            if len(tokens) < 3 or tokens[1] != "is":
                                raise SyntaxError("Invalid assignment statement: {}".format(line))
                            self.variables[variable_name] = " ".join(tokens[2:])

                    if tokens[0] == "print" or tokens[0] == "log" or tokens[0] == "write":
                        if len(tokens) < 2:
                            raise SyntaxError("Invalid print statement: {}".format(line))
                        print(self.variables.get(tokens[1], "Undefined variable: {}".format(tokens[1])))