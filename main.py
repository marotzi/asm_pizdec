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
import os


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

print("λ Ide//")
print("Choose language: Python, C, C++")
inp = input()
if inp.lower() == "python": python()
elif inp.lower() == "c": C()
elif inp.lower() == "c++": CPP()


