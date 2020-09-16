import sys,os
import json




def test1(relationtype):
    os.getcwd()
    f = open("../data/init-train.txt", "r", encoding="utf8")
    line = f.readline()
    relations=['后代','配偶']
    while line:
        jsontext = json.loads(line)
        if len(jsontext['sro_list']) > 0:
            for obj in jsontext['sro_list']:
                relation = obj['relation']
                if relation in relationtype:
                    text=jsontext['text']
                    entity1=obj['subject']
                    entity2=obj['object']
                    result=relation_predicate(text,relations,entity1,entity2)
                    print(jsontext,end=";")
                    print(result)

        line = f.readline()
    f.close()

def test(relationtype):
    os.getcwd()
    f = open("../data/init-train.txt", "r", encoding="utf8")
    line = f.readline()
    while line:
        jsontext = json.loads(line)
        if len(jsontext['sro_list']) > 0:
            for obj in jsontext['sro_list']:
                relation = obj['relation']
                if relation in relationtype:
                    print(jsontext)
        line = f.readline()
    f.close()

def relation_predicate_test(obj):
    text=obj["text"]
    pairlist=obj["pairlist"]
    default=[]
    f = open("data/init-train.txt", "r", encoding="utf8")
    line = f.readline()
    while line:
        if line!="":
            default.append(line)
        line = f.readline()
    f.close()
    relationlist=[]
    for tempobj in pairlist:
        entity1=tempobj['entity1']
        entity2=tempobj['entity2']
        relations=tempobj['relations']
        if len(relations)==1:
            obj2={}
            obj2["subject"]=entity1
            obj2["object"]=entity2
            obj2["relation"]=relations[0]
            relationlist.append(obj2)
        elif len(relations)>1:
            resultrelation=""
            for temprelation in relations:
                resultrelation=relation_predicate2(text,temprelation,entity1,entity2)
                if resultrelation!="":
                    obj2 = {}
                    obj2["subject"] = entity1
                    obj2["object"] = entity2
                    obj2["relation"] = resultrelation
                    relationlist.append(obj2)
            if resultrelation=="":
                for temprelation in relations:
                    if temprelation in default:
                        obj2 = {}
                        obj2["subject"] = entity1
                        obj2["object"] = entity2
                        obj2["relation"] = temprelation
                        relationlist.append(obj2)

        else:
            continue
    return relationlist



def relation_predicate(text,relation,entity1,entity2):
    index1=text.find(entity1)
    index2=text.find(entity2)
    minindex=index1
    maxindex=index2
    relationname=""
    if index1>index2:
        minindex=index2
        maxindex=index1
    else:
        minindex=index1
        maxindex=index2

    result=99
    f=open("../data/relation.txt","r",encoding="utf8")
    line=f.readline()
    while line:
        strs=line.split(' ')
        if len(strs)>1:
            key=strs[0]
            num = strs[1]
            tempname = strs[2].replace("\n","")
            if tempname in relation:
                index=text.find(key)
                if index<0:
                    line=f.readline()
                    continue
                else:
                    if num=="1":
                        # 结尾出现
                        if index>maxindex:
                            temp=abs(index-maxindex)
                            if temp<result:
                                result=temp
                                relationname=tempname
                    elif num=="2":
                        # 开头出现
                        if index<minindex:
                            temp=abs(minindex-index)
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="3":
                        # 开头和结尾出现
                        if index<minindex or index>maxindex:
                            temp=min(abs(minindex-index),abs(maxindex-index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="4":
                        # 开头与中间出现
                        if index<minindex or (index>minindex and index<maxindex):
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="5":
                        # 中间出现
                        if index>minindex and index<maxindex:
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="6":
                        # 中间和结尾出现
                        if index>minindex:
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="7":
                        if abs(maxindex-minindex-len(entity1))<2 or abs(maxindex-minindex-len(entity2))<2:
                            temp=min(abs(maxindex-minindex-len(entity1)),abs(maxindex-minindex-len(entity2)))
                            if temp<result:
                                result=temp
                                relationname=tempname
                    elif num=="8":
                        if (index2<index1) and (index>minindex and index<maxindex):
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="9":
                        if (index2<index1) and (index>minindex):
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
        line=f.readline()
    if relationname!="":
        return entity1+" <"+relationname+"> "+entity2

    else:
        return "no relation"

def relation_predicate2(text,relation,entity1,entity2):
    index1=text.find(entity1)
    index2=text.find(entity2)
    minindex=index1
    maxindex=index2
    relationname=""
    if index1>index2:
        minindex=index2
        maxindex=index1
    else:
        minindex=index1
        maxindex=index2

    result=99
    f=open("data/relation.txt","r",encoding="utf8")
    line=f.readline()
    while line:
        strs=line.split(' ')
        if len(strs)>1:
            key=strs[0]
            num = strs[1]
            tempname = strs[2].replace("\n","")
            if tempname in relation:
                index=text.find(key)
                if index<0:
                    line=f.readline()
                    continue
                else:
                    if num=="1":
                        # 结尾出现
                        if index>maxindex:
                            temp=abs(indx-maxindex)
                            if temp<result:
                                result=temp
                                relationname=tempname
                    elif num=="2":
                        # 开头出现
                        if index<minindex:
                            temp=abs(minindex-index)
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="3":
                        # 开头和结尾出现
                        if index<minindex or index>maxindex:
                            temp=min(abs(minindex-index),abs(maxindex-index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="4":
                        # 开头与中间出现
                        if index<minindex or (index>minindex and index<maxindex):
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="5":
                        # 中间出现
                        if index>minindex and index<maxindex:
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="6":
                        # 中间和结尾出现
                        if index>minindex:
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="7":
                        if abs(maxindex-minindex-len(entity1))<2 or abs(maxindex-minindex-len(entity2))<2:
                            temp=min(abs(maxindex-minindex-len(entity1)),abs(maxindex-minindex-len(entity2)))
                            if temp<result:
                                result=temp
                                relationname=tempname
                    elif num=="8":
                        if (index2<index1) and (index>minindex and index<maxindex):
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
                    elif num=="9":
                        if (index2<index1) and (index>minindex):
                            temp = min(abs(minindex - index), abs(maxindex - index))
                            if temp < result:
                                result = temp
                                relationname = tempname
        line=f.readline()
    return relationname

if __name__ == '__main__':
    # str="春伦，是黄大年为他的外孙起的中文名字：长春的春，伦敦的伦。"
    # relation=["配偶","后代"]
    # entity1="春伦"
    # entity2="黄大年"
    # relation_predicate(str,relation,entity1,entity2)
    # test()
    # test1("后代")
    test(["毕业院校"])