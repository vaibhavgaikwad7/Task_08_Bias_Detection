import json, time, random
prompts=json.load(open('../prompts/prompts.json'))
log=[]
for p in prompts:
    for i in range(3):
        log.append({'prompt':p['prompt'],'response':'MOCK RESPONSE'})
json.dump(log, open('../results/experiment_log.json','w'), indent=2)
