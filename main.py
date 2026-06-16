#!/usr/bin/env python3

import os
import time
import pickle
import sys

def python():
    filename = "lambda.py"
    savefile = "lambda_last.pkl"
    print("////λ IDE")
    lines = []
    while True:
        line = input()
        if not line:
            break
        if line == "load-last":
            if os.path.exists(savefile):
                with open(savefile, "rb") as file:
                    last_code = pickle.load(file)
                lines = last_code.splitlines()
                print("Loaded last session.")
            else:
                print("No saved session found.")
            break
        lines.append(line)

    if not lines and os.path.exists(savefile):
        with open(savefile, "rb") as file:
            last_code = pickle.load(file)
        lines = last_code.splitlines()

    if lines:
        code = "\n".join(lines)
        with open(filename, "w") as f:
            f.write(code)
        with open(savefile, "wb") as file:
            pickle.dump(code, file)
        os.system('python3 lambda.py')
    else:
        print("No code to run.")
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
def winclang():
    os.system('pip install clang')
    time.sleep(7)
    time.sleep(2)
    print("is installed!")

def begin():
    print("λ Ide//")
    config = "lambda.txt"
    while True:
        asd = input("")

        if asd == "choose lang":
            choose()
        elif asd == "inst_comp - propertiesetc":
            print("If no compilers installed choose a compiler you want to install if all is installed type N:")
            print("Python, C++, C,")
            if asd.lower() == "python":
                 if sys.platform == "darwin":
                    os.system('brew install python3')
                    time.sleep(7)
                    os.system('y')
                    time.sleep(45)
                    print("is installed!")
                 if sys.platform == "win32":
                    win()
                    def win():
                        os.system('pip install python')
                        time.sleep(7)
                        time.sleep(2)
                        print("is installed!")
                    def tux():
                        os.system('sudo apt install python')
                        time.sleep(7)
                        time.sleep(2)
                        print("is installed!")
            elif asd.lower() == "c" or asd.lower() == "c++":
              if sys.platform == "darwin":
                os.system('brew install clang')
                time.sleep(15)
                print("is installed!")
            if sys.platform == "win32":
               winclang()
            elif sys.platform == "Linux":
                os.system('sudo apt install clang')
                time.sleep(7)
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
            time.sleep(2)
            print("File edited")
        elif asd.lower() == "exit":
            break
        #/////
    print("Exiting IDE.")
    
begin()
  