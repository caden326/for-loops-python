# 1 - basics print integers from 0 to 150
for i in range(151):
    print(i)

# 2 print all multiples of 5 from 5 to 1000
i = 0

for i in range(5,1005,5):
    print(i)

# 3 Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(101):
    if i % 10 == 0 :
        print("coding dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print(i)


#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
num = 500000
i = sum(range(1, num+1, 2))
print(i)


#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

'''6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
print only the integers that are a multiple of mult.
For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
Create a Python file'''

i = 4
y = 12
mult = 2
for f in range(i, y):
    f % mult == 0
    print (f)
