import sys
from Interpreter import Interpreter

def main():
    # Check if filename is provided as command-line argument
    if len(sys.argv) < 2:
        print("Usage: python math_language.py <filename>")
        return

    filename = sys.argv[1]

    # Read code from file
    with open(filename, "r") as file:
        code = file.read()

    interpreter = Interpreter()
    interpreter.interpret(code)

if __name__ == "__main__":
    main()