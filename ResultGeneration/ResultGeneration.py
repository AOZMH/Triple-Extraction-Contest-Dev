import json
def ResultGeneration(text:str,list):
    jsonobj={}
    jsonobj["text"]=text
    jsonobj["sro_list"]=list
    print(json.dumps(jsonobj,ensure_ascii=False))


if __name__ == '__main__':
    list=[]
    temp={}
    temp["subject"]="菲律宾"
    temp["object"]="苏比克"
    temp["relation"]="城市"
    list.append(temp)
    text="第一次、第二次会议分别于2017年、2018年在菲律宾苏比克和中国广州举行"
    ResultGeneration(text,list)