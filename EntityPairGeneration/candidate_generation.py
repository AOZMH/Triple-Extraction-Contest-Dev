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

def form_relation_candidates(entity_list, relation_dict, output_format='list', text=None):
    # INPUT:    实体数组，形如[[实体（mention），实体类型],...];
    #           关系集合，形如{(sbj, obj):[relation list],...};
    # OUTPUT:   关系候选，形如[[entity_1, entity_2, cand_rel],...].
    #           如果json输出，输出string数组，格式为["[text, entity1, entity2, cand_rel]",...].
    cands = []
    for sbj, obj in product(entity_list, entity_list):
        if sbj == obj:
            continue
        if (sbj[1], obj[1]) in relation_dict:
            cands.append([sbj[0], obj[0], relation_dict[(sbj[1], obj[1])]])
    # 输出为json字符串
    if output_format == 'json':
        assert(text != None), 'text must not be None object if output json format.'
        for i, c in enumerate(cands):
            c.insert(0, text)
            cands[i] = json.dumps(c, ensure_ascii=False)
    else:
        cand_dicts = {}
        cand_dicts['text'] = text
        cand_dicts['pairlist'] = []
        for c in cands:
            cand_dicts['pairlist'].append({'entity1':c[0], 'entity2':c[1], 'relations':c[2]})
        cands = cand_dicts
    return cands

if __name__ == '__main__':
    rd = form_relation_dict("./relation-dict.json")
    test_input = [['陈福才','人物'],['包头稀土高新区经信委主任', '职位'],['包头稀土高新区经信委', '组织机构']]
    text = '包头稀土高新区经信委主任陈福才表示，近期已有10户企业与银行对接，拟贷款9500万元。'
    test_output = form_relation_candidates(test_input, rd, output_format='list', text=text)
    print(test_output)