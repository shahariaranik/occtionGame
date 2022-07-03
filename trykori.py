def split_and_join(line):
    a=line.split(" ")
    return a = "-".join(a)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)