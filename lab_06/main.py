
def task_01():
    txt = open('input_6.txt')
    n = txt.readlines()

    def condition(a):
        first = second = 0
        for i in a:
            if i == 'A':
                first = 1
            elif i == 'B':
                first = 2
            elif i == 'C':
                first = 3
            if i == 'X':
                second = 1
            elif i == 'Y':
                second = 2
            elif i == 'Z':
                second = 3


        if second - first == 0:
            return 'draw', second
        elif second - first == -2 or 1:
            return 'win', second
        elif second - first == 2 or -1:
            return 'lose', second



    def main(n):
        total_sum = 0
        for i in n:
            res, second = condition(i)
            if res == 'win':
                total_sum += (6 + second)
            elif res == 'draw':
                total_sum += (3 + second)
            elif res == 'lose':
                total_sum += second
        print(total_sum)
    main(n)

task_01()
#18239
