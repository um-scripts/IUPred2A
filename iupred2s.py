# import requests
#
# with open('147ids.txt') as f:
#     ids = f.readline().strip('\n').split(',')
# for iid in set(ids):
#     print(iid)
#     result=requests.get(f'http://iupred2a.elte.hu/iupred2a/short/{iid}')
#     res=result.text
#     res=res.replace('<pre>','')
#     res=res.replace('</pre>','')
#     with open(f'IUPred_results/{iid}.tsv','w') as file:
#         file.write(res)
#         file.close()
import pandas as pd

# EXTRACT IDRs for curated sites
import pandas as pd

df = pd.read_csv('147-5_142Curated_phosphorylation.csv')
df['pos'] = df['SITE'].apply(lambda x: int(x[1:]))

for i, r in df.iterrows():
    dd = pd.read_csv(f'IUPred_results/{r["UNIPROT"]}.tsv', comment='#', sep=r'\s+', header=None, names=['col1', 'col2', 'col3'])
    df.loc[i, 'V1'] = dd.loc[dd['col1'] == r['pos'], 'col2'].iloc[0]
    df.loc[i, 'V2'] = dd.loc[dd['col1'] == r['pos'], 'col3'].iloc[0]

df.to_csv('out.csv', index=False)

