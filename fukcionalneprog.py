#kreirati fje koja kvadrira zadati parametar

def square(x):
    return x*x

print(square(4))

#zapisemo u drugi nacin koristeci lambdu fju

square_lambda=lambda x: x * x
print(square_lambda(4))

def build_quadratic_function(a,b,c):
    return lambda x:a*x*x+b*x+c

#f = a*x*x+b*x+c zove se CLOUSURE
f = build_quadratic_function(2,3,-5)   #per a ruhet a = 2,b=3,c=-5
print(f(0))  #f(0)je parmetar x --> 2*0*0+3*0+(-5)=-5
print(f(1)) #f(1)je parametar x --> 2*1*1+3*1+(-5)
print(f(2))
print(build_quadratic_function(3,2,1)(2))


