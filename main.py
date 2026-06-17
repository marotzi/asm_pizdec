#!/usr/bin/env python3

import os
import time
import pickle
import sys

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

def python():
    filename = "lambda.py"
    print(f"{YELLOW}////λ IDE{RESET}")
    lines = []
    while True:
        line = input()
        if not line: break 
        lines.append(line)
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    while filename == True:
        with open("lambda.py", "wb") as file:
            pickle.dump('lambda.py', file)
    if os.path.exists:
     os.system('python3 lambda.py')
    if line == "load-last":
        pickle.load('lambda.py')
        filename.read()
        print(filename)
def C():
    filename = "lambda.c"
    print(f"{YELLOW}////λ IDE{RESET}")
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
    print(f"{YELLOW}////λ IDE{RESET}")
    lines = []
    while True:
        line = input()
        if not line: break
        lines.append(line)
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    os.system('clang lambda.cpp -o lambda && ./lambda')

def choose():
    print(f"{RED}Choose language: Python, C, C++{RESET}")
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
    print("\033[44m\033[37m\033[2J", end="")
    print(f"{YELLOW}λ Ide//{RESET}")
    config = "lambda.txt"
    while True:
        asd = input("")

        if asd == "choose lang":
            choose()
        if asd == "clear screen":
            print("\033[A\033[K", end="") 
        elif asd == "inst_comp - propertiesetc":
            print("If no compilers installed choose a compiler you want to install if all is installed type N:")
            print(f"{GREEN}Python,{BLUE} C++, {CYAN}C,{RESET}")
            if asd.lower() == "python":
                 if sys.platform == "darwin":
                    os.system('brew install python3')
                    time.sleep(7)
                    os.system('y')
                    time.sleep(45)
                    print(f"{YELLOW}is installed!{RESET}")
                 if sys.platform == "win32":
                    win()
                    def win():
                        os.system('pip install python')
                        time.sleep(7)
                        time.sleep(2)
                        print(f"{YELLOW}is installed!{RESET}")
                    def tux():
                        os.system('sudo apt install python')
                        time.sleep(7)
                        time.sleep(2)
                        print(f"{YELLOW}is installed!{RESET}")
            elif asd.lower() == "c" or asd.lower() == "c++":
              if sys.platform == "darwin":
                os.system('brew install clang')
                time.sleep(15)
                print(f"{YELLOW}is installed!{RESET}")
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
  