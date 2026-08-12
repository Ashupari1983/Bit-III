l = [2,2,6,6,9,1]
xab = 0
for i in l: xab^=i
print('XOR l result:',xab,'-->',bin(xab))

setbit = xab & -xab
x,y =0,0

for n in l:
    if n & setbit: x ^=n
    else: y ^=n
print("x, y =",x,y)