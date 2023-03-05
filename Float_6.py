while True:
    x = float(input('Enter x coordinates: '))
    y = float(input('Enter y coordinates: '))
    if 0 <= x <= 0.8 and 0 <= y <= 0.8:
        print('Coordinates', int(10 * x), int(10 * y))
        if x * 1000 % 100 != 50:
            corect_x =float((50 - x * 1000 % 100) / 100)
            print('x correct on', corect_x)
        if y * 1000 % 100 != 50:
            corect_y =float((50 - y * 1000 % 100) / 100)
            print('y correct on',corect_y)
        print('Coordinates', int(10 * x), int(10 * y))
        break
    else:
        print('Not correct coordinates, repeat input')