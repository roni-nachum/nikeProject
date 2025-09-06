
is_pass= True
counter = 0

#example of while in case of False (by not)
while not (is_pass):
    print('The value of is pass is True')
    counter+=1 #(counter = counter+1), example of adding value
    if (counter==5):
        is_pass =True
        continue
    if (counter>10):
        break