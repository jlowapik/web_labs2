from collections import defaultdict

def task_1():
    txt = open('input_4.txt')
    n = txt.readlines()

    sizes = defaultdict(int)
    stack = []

    for i in n:
        parts = i.split()
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '/':
                    stack = ['/']
                elif parts[2] == '..':
                    stack.pop()
                else:
                    stack.append(parts[2])
        elif parts[0] == 'dir':
            continue
        else:
            size = int(parts[0])
            for j in range(len(stack)):
                sizes['/'.join(stack[: j + 1])] += size
    res = 0
    for k in sizes.values():
        if k < 100000:
            res += k
    return res


print(task_1())
#1453349