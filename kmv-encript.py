# -*- coding: utf-8 -*-'''
"""l = [1,2,3,5,7,11]
le = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ra = len(le)
r = len(l)
print(r)
print(ra)
for n in range(0,r):
	print(l[n])
"""
nu = []
p = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
letra=[]
ltu = []
lt = [0,1,2,3,4,5,6,7,8,9]
contra = []
m = len(p)
cd = len(lt)

nu.append(m)
ltu.append(cd)

for l in range(1,m+1):
	nu.append(m+l)

for l in range(1,cd+1):
	ltu.append(cd+l)

print(nu)
print(ltu)
palabra=raw_input()

rs = str(palabra)

g = len(rs)

for t in rs:
	for k in range(0,m):
		if t == p[k]:
			letra.append(nu[k])
			"""print(letra)"""
	for k in range(0,cd):
		if k == lt[k]:
			letra.append(ltu[k])
			
print(letra)

print("Esto es para la contra")
s = len(letra)

d = letra[0]

for h in range(0,s):
	d = d * letra[h]

contra.append(d)
print(contra)

raw_input()