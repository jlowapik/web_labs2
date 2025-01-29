txt = open('input_2.txt')
n = (txt.readlines())

def task1(j):
    safe = 0
    def inorder(j):
        safe_check = 0
        x = 0
        for i in range(len(j) - 1):
            if j[x] < j[x+1]:
                x += 1
        if len(j) - 1 == x:
            safe_check += 1
        return safe_check

    def disorder(j):
        safe_check = 0
        x = 0
        for i in range(len(j) - 1):
            if j[x] > j[x+1]:
                x += 1
        if len(j) - 1 == x:
            safe_check += 1
        return safe_check

    def check_order(j):
        if inorder(j) or disorder(j) == 1:
            ordercheck = 1
            return ordercheck
        else:
            ordercheck = 0
            return ordercheck

    def diff_check(j):
        x = 0
        diff_count = 0
        for i in range(len(j) - 1):
            diff = abs(j[x] - j[x+1])
            x += 1
            if diff > 0 and diff < 4:
                diff_count += 1
        if diff_count == len(j) - 1:
            diffcheck = 1
            return diffcheck
        else:
            diffcheck = 0
            return diffcheck

    for i in n:
        x = i.split()
        int_x = [int(h) for h in x]
        if diff_check(int_x) == 1 and check_order(int_x) == 1:
            safe += 1
    return safe


print(task1(n))
#218

