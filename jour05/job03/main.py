def draw_triangle(height):
    for i in range(height):
        if i == 0:
            spaces = ' ' * (height - 1)
            print(spaces +'/\ ')
        elif i == height - 1:
            print('/' + '_' * (2 * height - 2) + '\ ')
        else:
            spaces = ' ' * (height - i - 1)
            print(spaces + '/' + ' ' * (2* i - 0) + '\ ')

draw_triangle(5)