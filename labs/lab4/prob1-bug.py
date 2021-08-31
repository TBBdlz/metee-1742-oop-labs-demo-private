patients = [[70, 1.80], [58, 1.55], [150, 1.7]]


def calculate_bmi(_weight, _height):
    return _weight / (_height * 2)


for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    print(f'Patient\'s BMI is {bmi:.2f}')
