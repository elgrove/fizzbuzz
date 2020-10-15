# if numbers is divisible by 3 print 'fizz'
#, by 5 print 'buzz', by both print 'fizzbuzz'

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print(str(n) + ' - fizzbuzz')
    elif n % 3 == 0:
        print(str(n) + ' - fizz')
    elif n % 5 == 0:
        print(str(n) + ' - buzz')
    else:
        print(str(n))

for n in range(1,101):
    fizzbuzz(n)
