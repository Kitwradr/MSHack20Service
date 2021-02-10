import json
from random import seed,randint,choice,sample

orgs = ["C+AI", "E+D", "CFE", "CPE", "Gaming", "Marketing"]
hm_ids = ["23432","35234","32445","23453"]
result = ["Hire", "No Hire"]
skills = [".NET Framework", "C#", "Problem Solving", "Java", "Python", "Scala", ".NET Core", "Angular", "TypeScript", "React", "HTML", "CSS", "System Design", "Azure", "AWS", "Operating system"]

dictA = {}
num_items = 100
num_cands =  10
with open('data.json','w') as outfile:
    for i in range(num_items):
        dictB = {}
        dictB['org'] = choice(orgs)
        dictB['hm_id'] = choice(hm_ids)
        list_candidates = []
        for j in range(num_cands):
            candidate = {}
            candidate["Result"] = choice(result)
            skills_random = sample(skills,randint(4,8))
            skills_candidate = {}
            for skill in skills_random:
                if skill in ["C#",".NET Core", "TypeScript","React"]:
                    skills_candidate[skill] = randint(60,100)
                else:
                    skills_candidate[skill] = randint(0,100)
            candidate["skills"] = skills_candidate
            list_candidates.append(candidate)
        dictB['candidates'] = list_candidates
        json.dump(dictB,outfile)
        outfile.write('\n')











