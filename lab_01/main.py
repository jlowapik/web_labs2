from itertools import count

txt = open('input_1.txt')
n = (txt.readlines())
def task1(a):
    left_column = []
    right_column = []
    for i in a:
        x = i.split()
        left_column.append(x[0])
        right_column.append(x[1])

    int_right_column = [int(h) for h in right_column]
    int_left_column = [int(h) for h in left_column]

    def result(k, l):
        result_column = []
        while len(k) > 0:
            res = abs(min(k) - min(l))
            result_column.append(res)
            k.remove(min(k))
            l.remove(min(l))
        return sum(result_column)
    return result(int_left_column, int_right_column)

def task2(a):
    left_column = []
    right_column = []
    for i in a:
        x = i.split()
        left_column.append(x[0])
        right_column.append(x[1])

    int_right_column = [int(h) for h in right_column]
    int_left_column = [int(h) for h in left_column]

    def result(k, l):
        lis = []
        for i in k:
            abc = l.count(i)
            g = i * abc
            lis.append(g)
        return sum(lis)
    return result(int_left_column, int_right_column)


print(task1(n))
#1660292
print(task2(n))
#22776016