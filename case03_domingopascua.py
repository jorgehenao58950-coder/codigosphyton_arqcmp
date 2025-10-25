y = int(input("ingrese un año entre 1800y 2001:"))
a = y % 19 # hallar el residuo entre 19 y almacenarlo en a
b = y / 100
c = y % 100
d = b / 4
e = b % 4
g = (8*b + 13) / 25
h = (19*a + b - d - g + 15) / 30
j = c / 4
K = C % 4
M = ((a + 11)*h) / 319
r = (2*e + 2*j - k -h + m + 32) / 7
n = (h - m + r + 90) / 25
p = (h - m + r + n + 19) / 32

print ("en el", y, "la fecha de pascua fue:", p, "en el mes",n)



