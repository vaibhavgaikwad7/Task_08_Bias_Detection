import json, pandas as pd
df=pd.read_csv('../data/anonymized_stats.csv')
base_data=df.to_string(index=False)
prompts=[
{'category':'positive','prompt':base_data+"\nWhich player shows growth potential?"},
{'category':'negative','prompt':base_data+"\nWhich player underperformed?"},
]
json.dump(prompts, open('../prompts/prompts.json','w'), indent=2)
