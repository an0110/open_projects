from pprint import pprint

sum = 0
# rat - per year
rate = 1.06

# monthly deposit
monthly = 250

## duration, in months
duration = 12*30


for i in range(duration):
    print(sum)
    sum = sum + monthly + monthly*rate/12

    print ("\t" + str(sum))
    print("\t" + str(sum-monthly))
    if (i+1) % 12 == 0:
        print ("-"*50)


print ("*"*50)
print (monthly*duration)
print (sum)
print (sum - monthly*duration)






