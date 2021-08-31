summation = 0
count = 0
end_input = 0
print('Enter negative integer to exit the program...')
while not end_input:
    try:
        n = int(input('Enter an integer:'))
        summation += n
        count += 1
        if n < 0:
            end_input = 1  # to end while loop
    except ValueError:
        print('Please enter valid integer.')
avg = summation / count
print(f'Average is {avg:.2f}')
