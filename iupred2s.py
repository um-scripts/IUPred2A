import requests

with open('147ids.txt') as f:
    ids = f.readline().strip('\n').split(',')
for iid in set(ids):
    print(iid)
    result=requests.get(f'http://iupred2a.elte.hu/iupred2a/short/{iid}')
    res=result.text
    res=res.replace('<pre>','')
    res=res.replace('</pre>','')
    with open(f'IUPred_results/{iid}.tsv','w') as file:
        file.write(res)
        file.close()

