#Razvojite parne brojeve bez petlje koristeci lambdu fju

def even_check(num):
    if num % 2 ==0:
        return True
    else:
        return False 
#Menyra shkurt
def even_check_short(num):
    return num%2==0

even_check_lambda = lambda num: num%2 ==0


#za niz brojeva da razvojimi parne brojeve koristeci FILTER

l =[2,5,7,8,10]
even_elements=list(filter (even_check_lambda,l))  #prvi parametar je lamda fja, a drugi paramtar je lista kroz koji ulazi
print(even_elements)  #ako konvertujemo u list onda cemo dobiti parne brojeve

#svaki element povecajte sa 1
add_one=lambda num:num+1
#print(add_one(5)) uvecava sa 1
increased_elements = list(map(add_one,even_elements)) #prvi parametar fja a drugi lista nelt
print(increased_elements) #Moramo da konvertujemo opet u listu da bismo dobili

"""increased_elements=list(map(lambda  um:num + 1,))
print(increased_elements) menyra e shkurt"""

#Data je lista gradova koja se sastoji od torki,svaka torka ima 2 elementa(ime grada ,temperatura trenutna u celsius),
#za svaki grad konvertuje temperaturu u drugu skalu koja se koristi  sledecoj formulu (9/5*temp_c+32)


cities_temp_c = [("Podgorcia",20),("Niksic",18),("Budva",21),("Cetinje",14)]
cities_temp_c=map(lambda elem:(elem[0],(9/5)*elem[1]+32),cities_temp_c)  #prvi argument je fja,i marrim me indexa
print(list(cities_temp_c))

#data su dvije liste,kreirati  koristeci funkcionalne  programiranje,
#tako da rezultat bude nova lista koja se sastoji od zbira elemenata sa odgovarajuci pozicija.
l1 = [1,2,3]
l2 = [2,4,5]

l3 =map(lambda x,y : x+y,l1,l2)
print(list(l3))

#Data je lista elemenata ,odrediti sumiranje

from functools import reduce
a = [1,2,3,4]

suma = reduce (lambda x,y:x+y,a)
print(suma)




                



 
