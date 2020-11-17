# fname = input('Introduce nombre de archvo:')
# fhandle= open(fname)
fhandle=open('mbox-short.txt')
hour=dict()

for line in fhandle:
    line = line.rstrip()
    wds = line.split()
    # for word in wds:
    #     print(wds)
    if len(wds)<1:
        continue
    if wds[0] != 'From':
        continue
    hrs = wds[5].split(':')
    
    hour[hrs[0]]=hour.get(hrs[0],0)+1

#print(hour)
print(sorted([(k,v)for k,v in hour.items()]))