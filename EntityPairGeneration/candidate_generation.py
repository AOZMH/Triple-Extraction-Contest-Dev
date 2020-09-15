import json
from itertools import product

def form_relation_dict(raw_file):
    relation_dict = {}
    with open(raw_file, "r", encoding='utf-8') as f:
        data = json.load(f)
        for entry in data:
            if (entry['subject'], entry['object']) not in relation_dict:
                relation_dict[(entry['subject'], entry['object'])] = [entry['relation']]
            else:
                relation_dict[(entry['subject'], entry['object'])].append(entry['relation'])
    return relation_dict

def form_relation_candidates(entity_list, relation_dict):
    # INPUT:    实体数组，形如[[实体（mention），实体类型],...];
    #           关系集合，形如{(sbj, obj):[relation list],...};
    # OUTPUT:   关系候选，形如[[实体对（一个像上面格式的pair），关系候选（一个list）],...].
    cands = []
    for sbj, obj in product(entity_list, entity_list):
        if sbj == obj:
            continue
        if (sbj[1], obj[1]) in relation_dict:
            cands.append([[sbj, obj], relation_dict[(sbj[1], obj[1])]])
    return cands

if __name__ == '__main__':
    rd = form_relation_dict("./relation-dict.json")
    test_input = [['B1B轰炸机','武器装备'],['美国', '国家']]
    test_output = form_relation_candidates(test_input, rd)
    print(test_output)