from operator import index

numbers = [3,5,6,7,12,455,6,78]
cities = {'London', 'Athen', 'NewYork', 'Jerusalem', 'Lod'}

l = len(numbers) # find the length of list
value = numbers[2] # getting the value at index 2
index_of_5 = numbers.index(5) # getting the position of 5 in the list
numbers.append(56) # adding a number to the end of the list.

for number in numbers:
    print(number)
    if (number < 10):
        print(f'{number} found - it less then 10')
        number+=10
        print(f' {number} is the new number')

    if (number%2==0):
        print(f'{number} dived by 2')


cities = {'London', 'Athen', 'NewYork', 'Jerusalem', 'Lod'}
for city in cities:
    print(city)

    print(f'the len it {len(city)}')

    if (city.count('_') > 8):
        print(f'- found at {city}')
        break

prices = [12,45,67,32,34]