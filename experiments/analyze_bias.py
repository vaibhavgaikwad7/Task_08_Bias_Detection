import json, pandas as pd
log=json.load(open('../results/experiment_log.json'))
df=pd.DataFrame(log)
df.to_csv('../analysis/analysis.csv',index=False)
