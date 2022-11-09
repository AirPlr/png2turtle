#function that takes duplicate lines of a file and substitutes them with a single line with cycle count
def simple(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    f = open(filename, "w")
    i = 0
    while i < len(lines):
        count = 1
        while i + 1 < len(lines) and lines[i] == lines[i + 1]:
            count += 1
            i += 1
        if count == 1:
            f.write(lines[i])
        else:
            f.write("for _ in range(" + str(count) + "):\n")
            f.write("   "+lines[i])
        i += 1
    f.close()
    