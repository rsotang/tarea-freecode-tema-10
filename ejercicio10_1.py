fname = input('Introduce nombre de archvo:')
fhandle= open(fname)
sender=dict()

for line in fhandle:
    line = line.rstrip()
    wds = line.split()
    # for word in wds:
    #     print(wds)
    if len(wds)<1:
        continue
    if wds[0] != 'From':
        continue
    sender[wds[1]]=sender.get(wds[1],0)+1

# print(sender)
# maximo=-1
# keymax=None
# for k,v in sender.items():
#     if v > maximo:
#         maximo =v
#         keymax =k
# print('maximo', keymax,maximo)

#vamos a hacer una versión del programa de diccionarios para hacer lo mismo
tmp=list()
for k,v in sender.items():
    tmp.append((k,v))
tmp=sorted(tmp,reverse=True)
print(tmp[0])