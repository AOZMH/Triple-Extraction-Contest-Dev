import sys,os
import json

if __name__ == '__main__':
    os.getcwd()
    f=open("../data/init-train.txt","r",encoding="utf8")
    line=f.readline()
    while line:
        jsontext=json.loads(line)
        if len(jsontext['sro_list'])>0:
            for obj in jsontext['sro_list']:
                relation=obj['relation']
                if relation=='配偶':
                    print(jsontext)
        line=f.readline()
    f.close()


def relation_predicate():

    return 0