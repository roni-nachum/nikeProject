from jb_60.function_example.utils import utils

utils_instance=utils()

num1 = 1
num2 = 10
num3 = 27
utils_instance.print_between_number(num1,num2 )
print('###############')
utils_instance.print_between_number(num3, num2)
print('###########')

utils_instance.print_between_number(num3,num1)
