#! /urs/bin/python
#! encoding: UTF-8

PI350T = 3.14159265358979323846264338327950288
def aprox(n):
  s=0.0
  for i in range(1,n+1):
    xi= (i-0.5)/n
    fxi=4.0/(1+xi**2)  
    s += fxi
  R=1.0/n*s
  return R
  


  
print "%.35g" % PI350T

n= int (raw_input('Introduzca n: '))
m= int (raw_input('Introduzca m: '))
l= [ ]
for i in range(1, m+1):
  api = aprox(n*i)
  l=l+[api]
print l