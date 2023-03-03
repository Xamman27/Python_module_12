weight = int(input('Your weight: '))
height = float(input('Your height (mertres): '))
ibm = round(weight / (height ** 2), 2)
if ibm < 18.5:
    print('ibm =', ibm, 'Your weight is too small')
elif 18.5 < ibm < 25:
    print('ibm =', ibm, 'Your weight is normal')
elif 25 < ibm < 30:
    print('ibm =', ibm, 'Your are overweight')
else:
    print('ibm =', ibm, 'Your are obese')