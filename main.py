import os

def python():
    filename = "lambda.py"
    print("////λ IDE")
    lines = []
    while True:
        line = input()
        if not line: break
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
if inp.lower() == "python": python()
elif inp.lower() == "c": C()
elif inp.lower() == "c++": CPP()


print("λ Ide//")
print("If no compilers installed choose a compiler you want to install if all is installed type N:")
print("Python, C++, C,")
langug = input("")
if langug.lower()== "n":
  choose()
if langug.lower() == "python":
    os.system('brew install python3')
if langug.lower() == "c" or "c++":
    os.system('brew install clang')





