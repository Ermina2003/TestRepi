#Izračunati prosjek studenata sa prve godine studije. Za studente se čuva ime i prezime, 
#broj indeksa, godina studija, trenutni prosjek
#● Za svaki film je poznat naziv, broj pozitivnih komenatara za taj film i broj negativnih komentara 
#za taj film. 
#○ Vaš zadatak je da kreirate program koji štampa naziv filma sa najviše pozitivnih komentara.
#○ Vratiti informacije o filmu koji počinje za zadatim terminom term.
#○ Vaš zadatak je da kreirate program kojim pronalazite film koji ima najbolji odnos između 
#pozitivnih i negativnih komentara. 
#Primjer: Za [{‘naziv’:’The Godfather’, ‘br_pozitivni’:1000,’br_negativni’:10}, {‘naziv’:’The 
#Pianist’, ‘br_pozitivni’:500,’br_negativni’: 30}, {‘naziv’:’A Beautiful Mind’, 
#‘br_pozitivni’:600,’br_negativni’: 45}] treba da štampa The Godfather


lista_filmova = [{"naziv":"The Godfather", "br_pozitivni":1000,"br_negativni":10},
                 {"naziv":"The Pianist", "br_pozitivni":500,"br_negativni": 30}, 
                 {"naziv":"A Beautiful Mind", "br_pozitivni":600,"br_negativni": 45}]

#Da kreiramo prgram koji stampa naziv filma sa najvise pozitivnih komentara

max_film = {}
max_value = 0
for film in lista_filmova:
    if film ["br_pozitivni"] > max_value:
        max_value = film["br_pozitivni"]
        max_film = film
print(max_film)


#zadatak da kreiramo 
term ="The"
for film in lista_filmova:
    if film["naziv"].startswith(term):
        print(film)

