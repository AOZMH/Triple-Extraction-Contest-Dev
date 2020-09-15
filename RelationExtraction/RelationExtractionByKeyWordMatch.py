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
                if relation == relationtype:
                    text=jsontext['text']
                    entity1=obj['subject']
                    entity2=obj['object']
                    result=relation_predicate(text,relations,entity1,entity2)
                    print(jsontext,end=";")
                    print(result)

        line = f.readline()
    f.close()

def test():
    os.getcwd()
    f = open("../data/init-train.txt", "r", encoding="utf8")
    line = f.readline()
    while line:
        jsontext = json.loads(line)
        if len(jsontext['sro_list']) > 0:
            for obj in jsontext['sro_list']:
                relation = obj['relation']
                if relation == '后代':
                    print(jsontext)
        line = f.readline()
    f.close()

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
        line=f.readline()
    if relationname!="":
        return entity1+" <"+relationname+"> "+entity2

    else:
        return "no relation"

if __name__ == '__main__':
    # str="春伦，是黄大年为他的外孙起的中文名字：长春的春，伦敦的伦。"
    # relation=["配偶","后代"]
    # entity1="春伦"
    # entity2="黄大年"
    # relation_predicate(str,relation,entity1,entity2)
    # test()
    test1("后代")