#hay que separar las letras de un archivo y luego asignarlas a un diccionario
# luego ordenamos ese diccionario con los métodos tradicionlaes

#lo más complicado parece separar las letras del resto de caracteres 
#en el string
fname=input('Introduce el nombre del archivo: ')
try:
    fhandle= open(fname)
except:
    print('badname')
    quit()

word_count=dict()
letter_count=dict()
temp = list()
counter = 0

for line in fhandle:
    line = line.rstrip()
    line = line.lower()
    wds = line.split()
    
    for word in wds:
        word_count[word]=word_count.get(word,0)+1
        letters=list(word) #el comando list convertia un elemento iterable en una lista de elementos                

        for letter in letters:
            if letter.isalpha() == True:
                letter_count[letter]=letter_count.get(letter,0)+1  
                counter = counter +1   
            else:
                continue  

for k,v in letter_count.items():
    temp.append((v,k))

temp=sorted(temp,reverse=True)
print('Frecuencia listada de letras en el texto')

for v,k in temp:
    print(k,v)

print('Porcentajes de aparicion de cada letra')

for v,k in temp:
    print(k, v*100/counter,'%')

