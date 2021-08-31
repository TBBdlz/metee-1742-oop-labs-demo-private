patients = [[70, 1.80], [58, 1.55], [150, 1.7]]


def calculate_bmi(_weight, _height):
    return _weight / (_height * _height)


for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(weight, height)
    print(f'Patient\'s BMI is {bmi:.2f}')
