a,b = 7,7

print('== XOR Operator ==')
print('n^n:',a^b)
print('n^0:',a^0)
print('Equal(XOR):',a^b == 0)

arr = [4,2,2,4,7]
result = 0
for x in arr: result = result^x
print('XOR',arr,'=',result)

pair = [2,2,6,6,9,1]
xab = 0
for x in pair: xab^=x
print('XOR pair result:',xab,'-->',bin(xab))

setbit = xab & -xab
x,y =0,0

for n in pair:
    if n & setbit: x ^=n
    else: y ^=n
print("x, y =",x,y)