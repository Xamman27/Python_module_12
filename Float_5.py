while True:
    x = float(input('Enter x coordinates: '))
    y = float(input('Enter y coordinates: '))
    if 0 <= x <= 0.8 and 0 <= y <= 0.8:
        print('Coordinates', int(10 * x), int(10 * y))
        break
    else:
        print('Not correct coordinates, repeat input')