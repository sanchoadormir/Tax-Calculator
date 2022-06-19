import matplotlib.pyplot as plt
print("This tax calculator is only accurate in the event that you pay tax in the UK and your monthly salary is less than 4189 pounds")
z = float(input("Monthly Salary: "))
if z <= 1047.5:
    v = 1
    u = 0
elif z <= 4189.16:
    v = 0.8
    u = 0.2
else:
    v = 0
    u = 0
    print("I told you it wouldn't work")
a = z * v
b = a + a
c = b + a
d = c + a
e = d + a
f = e + a
g = f + a
h = g + a
i = h + a
j = i + a
k = j + a
l = k + a

a2 = z * u
b2 = a2 + a2
c2 = b2 + a2
d2 = c2 + a2
e2 = d2 + a2
f2 = e2 + a2
g2 = f2 + a2
h2 = g2 + a2
i2 = h2 + a2
j2 = i2 + a2
k2 = j2 + a2
l2 = k2 + a2


x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [a,b,c,d,e,f,g,h,i,j,k,l]

x2 = [1,2,3,4,5,6,7,8,9,10,11,12]
y2 = [a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2]

print("   ")
print("SAVINGS")
print("1st month: ")
print(a)
print("2nd month: ")
print(b)
print("3rd month: ")
print(c)
print("4th month: ")
print(d)
print("5th month: ")
print(e)
print("6th month: ")
print(f)
print("7th month: ")
print(g)
print("8th month: ")
print(h)
print("9th month: ")
print(i)
print("10th month: ")
print(j)
print("11th month: ")
print(k)
print("12th month: ")
print(l)

print("   ")
print("Taxed Income")
print("1st month: ")
print(a2)
print("2nd month: ")
print(b2)
print("3rd month: ")
print(c2)
print("4th month: ")
print(d2)
print("5th month: ")
print(e2)
print("6th month: ")
print(f2)
print("7th month: ")
print(g2)
print("8th month: ")
print(h2)
print("9th month: ")
print(i2)
print("10th month: ")
print(j2)
print("11th month: ")
print(k2)
print("12th month: ")
print(l2)

plt.plot(x, y, color="green", marker='o', markerfacecolor='blue', markersize=3, label="Savings")
plt.plot(x2, y2, color="red", marker='o', markerfacecolor='yellow', markersize=3, label="Taxed")
plt.xlabel('time - months')
plt.ylabel('money - pounds')
plt.title('Yearly Income')
plt.legend
plt.show()

