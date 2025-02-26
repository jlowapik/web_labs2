
def task_01():

    def condition(a):
        my_dict = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
        one, two = a.split()
        first = my_dict.get(one)
        second = my_dict.get(two)

        if second - first == 0:
            return 'draw', second
        elif second - first == -2 or 1:
            return 'win', second
        elif second - first == 2 or -1:
            return 'lose', second

    def main():
        txt = open('input_6.txt')
        n = txt.readlines()
        total_sum = 0
        result = {'win': 6, 'draw': 3, 'lose': 0}
        for i in n:
            res, second = condition(i)
            total_sum += (result.get(res) + second)
        print(total_sum)
    main()

task_01()
#18239
