# Function written in 1 line of a code
# accepts any no.of args, but only asa a1 expression

#lambda parameters:expression

sq = lambda x:x*x
add = lambda a,b:a+b
mul = lambda e,f,g:e*f*g
text = lambda fn,ln: fn+" "+ln
age_check = lambda age:True if age>=18 else False

print(sq(5))
print(add(10,11))
print(mul(2,4,6))
print(text("Dinesh","Pinnepalli"))
print(age_check(1))