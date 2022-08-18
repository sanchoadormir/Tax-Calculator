# MIT License
#
# Copyright (c) 2022 Sancho Mir a.k.a OvenSausage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
print("OvenSausage presents: ")
print(" ")
print("TAX CALCULATOR")
print(" ")
print("This tax calculator is not completely accurate, but it is a near estimation.")
print("UK ONLY")
z = float(input("Monthly Salary: "))


# no tax
thresh1 = 1047.5
#20% tax
thresh2 = 4189.16
#40% tax
thresh3 = 12500

#untaxed max amount
ti1 = 1047.5
#20% max amount
ti2 = 3141.66
#40% max amount
ti3 = 8310.84

# 0% taxes
if z <= thresh1:
    mon = z
    v = 1
    u = 0
    a = mon * v
    a2 = mon * u
# 20% taxes
elif z <= thresh2:
    mon = z - ti1
    v = 0.8
    u = 0.2
    a = mon * v + ti1
    a2 = mon * u
#40% taxes
elif z <= thresh3:
    mon = z - ti1 - ti2
    v = 0.6
    u = 0.4
    a = mon * v + ti1 + ti2 * 0.8
    a2 = mon * u + ti2 * 0.2
#45% taxes
elif z > thresh3:
    mon = z - ti1 - ti2 - ti3
    v = 0.55
    u = 0.45
    a = mon * v + ti1 + ti2 * 0.8 + ti3 * 0.6
    a2 = mon * u + ti2 * 0.2 + ti3 * 0.4

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
