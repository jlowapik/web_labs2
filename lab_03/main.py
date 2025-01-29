
txt = open('input_3.txt')
n = (txt.readlines())
list_count = []
def task1(a):
    def nums(a):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        lis = []
        for i in a:
            if i in numbers:
                lis.append(i)

        number = lis[0] + lis[-1]
        return number

    for i in n:
        list_count.append(nums(i))
        int_list_count = [int(h) for h in list_count]
    return sum(int_list_count)

def task2(a):
    def nums(a):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        j = a.replace('zero', '0')
        j = j.replace('one', '1')
        j = j.replace('two', '2')
        j = j.replace('three', '3')
        j = j.replace('four', '4')
        j = j.replace('five', '5')
        j = j.replace('six', '6')
        j = j.replace('seven', '7')
        j = j.replace('eight', '8')
        j = j.replace('nine', '9')
        lis = []
        for i in j:
            if i in numbers:
                lis.append(i)

        number = lis[0] + lis[-1]
        return number

    for i in n:
        list_count.append(nums(i))
        int_list_count = [int(h) for h in list_count]
    return sum(int_list_count)
print(task1(n))
#54242
print(task2(n))
#109780