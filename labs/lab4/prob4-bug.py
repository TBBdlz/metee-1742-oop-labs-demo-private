sum = 0
count = 0
end_input = 0
while not end_input:
    n = int(input('Enter an integer:'))
    sum += n
    count += 1
    avg = sum / count
print(f'Average is {avg}')