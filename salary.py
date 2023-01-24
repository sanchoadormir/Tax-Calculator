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
print("It is important to note that this script is not completely accurate and it is only a near estimation. ")
print("The tax laws and regulations are subject to change, and this script may not be updated accordingly. ")
print("It is recommended to consult with a professional tax advisor before making any financial decisions.")
print("UK ONLY")

salary = int(input("Input your gross Salary: "))
years = int(input("How many years do you want to track: "))


# threshold of untaxed income
notax = 12570
#threshold at 20% tax
thresh2 = 50270
#threshold at 40% tax
thresh3 = 150000
#threshold at 45% tax
# anything above £150000 is at 45% tax

#tax of 2nd threshold
thresh2_tax = thresh2 * 0.2
#salary of 2nd threshold
thresh2_sal = thresh2 * 0.8
#tax of 3rd threshold
thresh3_tax = thresh3 * 0.4
#salary of 3rd threshold
thresh3_sal = thresh3 * 0.6


# 0% taxes
if salary <= notax:
    final_salary = salary
    a = final_salary 
    a2 = 0
# 20% taxes
elif salary <= thresh2:
    final_salary = salary - notax
    a = final_salary * 0.8 + notax
    a2 = final_salary * 0.2
#40% taxes
elif salary <= thresh3:
    final_salary = salary - notax - thresh2
    a = final_salary * 0.6 + notax + thresh2_sal
    a2 = final_salary * 0.4 + thresh2_tax
#45% taxes
elif salary > thresh3:
    final_salary = salary - notax - thresh2 - thresh3
    a = final_salary * 0.55 + notax + thresh2_sal + thresh3_sal
    a2 = final_salary * 0.45 + thresh2_tax + thresh3_tax

x = 1
for i in range(years):
    print("Year: ",x," Net income: £",x * a," Tax paid: £", x * a2)
    x = x+1