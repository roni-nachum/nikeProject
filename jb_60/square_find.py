# go over all number from 0 to 10
# find square value
# find where is the first time to square is above 25

for num in range(1,11):
    square = num *num
    print(f'the square value is {square}')
    if (square>25):
        print(f'the value of {num} is above 25')
        break
print(f'the squre value is {square}')