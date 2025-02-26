

def task_1():
    def is_possible(game_data):

        for data in game_data:
            for item in data.split(','):
                count, color = item.strip().split(' ')
                count = int(count)

                if color == 'red':
                    if count > 12:
                        return False
                elif color == 'green':
                    if count > 13:
                        return False
                elif color == 'blue':
                    if count > 14:
                        return False

        return True


    def main():
        lis = []
        txt = open('input_5.txt')
        games = (txt.readlines())


        for game in games:
            game_id, game_data = game.split(": ")
            game_id = int(game_id.split()[1])
            game_sets = game_data.split(";")

            if is_possible(game_sets):
                lis.append(game_id)

        print(sum(lis))

    main()

def task_2():
    def power(game_data):
        max_red = max_green = max_blue = 0
        for set_data in game_data:
            for item in set_data.split(','):
                count, color = item.strip().split(' ')
                count = int(count)

                if color == 'red':
                    max_red = max(max_red, count)
                elif color == 'green':
                    max_green = max(max_green, count)
                elif color == 'blue':
                    max_blue = max(max_blue, count)

        return max_red, max_green, max_blue

    def main():

        txt = open('input_5.txt')
        games = (txt.readlines())

        total_sum = 0

        for game in games:
            game_id, game_data = game.split(": ")
            game_id = int(game_id.split()[1])
            game_sets = game_data.split(";")
            red, green, blue = power(game_sets)
            game_power = red * green * blue
            total_sum += game_power

        print(total_sum)

    main()

task_1()
#190
task_2()
#69110