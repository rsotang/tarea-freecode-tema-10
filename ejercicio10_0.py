#este programa cuenta las palabras más comunes en un archivo.txt

fhand = open('mbox-short.txt')
counts = dict()

for line in fhand:
    line=line.rstrip()
    wds = line.split()
    for word in wds :
        counts[word]=counts.get(word,0)+1
lst = list()

#ahora hacemos el algorimto de invertir 
for key, val in counts.items():
    newtuple = (val,key)
    lst.append(newtuple)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print (key,val) #el numeor de palabras a imprimir del diccionario
