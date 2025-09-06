from jb_60.function_example.avg_calc import summery

#exec.1

mails = ['a@abc.com', 'a@abccom''adfdfd.com']
for mail in mails:
    if '@' in mail and '.' in mail:
        print(f'{mail} is valid')
    else:
        print(f'{mail} invalid')



#exec.2

nums = [23, 34, -12, 33, -33]
summery_pos = 0
summery_neg = 0
for num in nums:
    if (num>0):
        summery_pos += num
        print(f'{num} value is more than 0')
        summery_pos = summery_pos+num
    else:
        print(f'{num} value is less than 0')
        summery_neg = summery_neg+num


nums = [33, 11, 22, 10, 14, 34]
even_num = 0
odd_num = 0
for num in nums:
    if (num % 2 ==0):
        print(f'{num} value is even')
        even_num = even_num+num
    else:
        print(f'{num} value is odd')
        odd_num = odd_num+num



