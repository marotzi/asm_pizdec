import os
import time

def python():
    filename = "lambda.py"
    print("////λ IDE")
    lines = []
    while True:
        line = input()
        if not line: break #полный пиздец бляяяяяя
        lines.append(line)
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    os.system('python3 lambda.py')

def C():
    filename = "lambda.c"
    print("////λ IDE")
    lines = []
    while True:
        line = input()
        if not line: break
        lines.append(line)
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    os.system('clang lambda.c -o lambda && ./lambda')
 


def CPP():
    filename = "lambda.cpp"
    print("////λ IDE")
    lines = []
    while True:
        line = input()
        if not line: break
        lines.append(line)
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    os.system('clang lambda.cpp -o lambda && ./lambda')

def choose():
    print("Choose language: Python, C, C++")
    inp = input()
    if inp.lower() == "python":
        python()
    elif inp.lower() == "c":
        C()
    elif inp.lower() == "c++":
        CPP()

def begin():
    print("λ Ide//")
    asd = input("")
    config = "lambda.txt"
    
    if asd == "choose lang":
        choose()
    elif asd == "inst_comp - propertiesetc":
        print("If no compilers installed choose a compiler you want to install if all is installed type N:")
        print("Python, C++, C,")
        if asd.lower() == "python":
            os.system('brew install python3')
            time.sleep(7)
            os.system('y')
            time.sleep(45)
            print("is installed!")
        elif asd.lower() == "c" or asd.lower() == "c++":
            os.system('brew install clang')
            time.sleep(15)
            print("is installed!")
        else:
            print("error via installing")
    elif asd == "y":
        os.chdir('configs&brainfuckingstuff')
        with open(config, "w") as f:
            if "language add: java" in config:
                os.system('brew install java')
    elif asd == "n" or asd == "N":
        choose()
    elif asd.lower() == "show_config":
        with open(config, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    elif asd.lower() == "edit config":
        edit = input("")
        with open(config, "a") as file:
            file.write(edit)
    else:
        print("error via editing config")

begin()