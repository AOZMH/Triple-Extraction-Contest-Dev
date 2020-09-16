import json
import sys
import ast
import time
# sys.path.append("/home/public/ieRace/models/PaddleNLP/")
# sys.path.append("/home/public/ieRace/models/PaddleNLP/lexical_analysis")
# sys.path.append("/home/public/ieRace/models/PaddleNLP/shared_modules")
# from lexical_analysis import *
from EntityRecognition.client import entry

from EntityPairGeneration import candidate_generation
from RelationExtraction import RelationExtractionByKeyWordMatch
from ResultGeneration import ResultGeneration


def predict(text:str):
    #step 1
    entity_list1 = entry(text);
    print("Step 1 -----------------------")
    print(entity_list1)
    #step 2
    rd = candidate_generation.form_relation_dict("EntityPairGeneration/relation-dict.json")
    test_input = ast.literal_eval(entity_list1)
    # test_input = [['陈福才', '人物'], ['包头稀土高新区经信委主任', '职位'], ['包头稀土高新区经信委', '组织机构']]
    # text = '包头稀土高新区经信委主任陈福才表示，近期已有10户企业与银行对接，拟贷款9500万元。'
    test_output = candidate_generation.form_relation_candidates(test_input, rd, output_format='list', text=text)
    print("Step 2 -----------------------")
    print(test_output)
    #测试一下
    #step 3
    relationlist= RelationExtractionByKeyWordMatch.relation_predicate_test(test_output)
    print("Step 3 -----------------------")
    print(relationlist)
    #Step 4
    result=ResultGeneration.ResultGeneration(text,relationlist)
    print("Step 4 -----------------------")
    print(result)
    return result

if __name__ == '__main__':
    # result={}
    # result['text']="张俊一家三口都是驻村干部，张俊在普安县九峰街道云庄村，妻子蒋冬梅在普安县南湖街道大湾村，儿子张力宇在镇宁县简嘎乡喜妹村"
    # result1={}
    # result1['entity1']='张俊'
    # result1['entity2']='蒋冬梅'
    # relations=['配偶','后代']
    # result1['relations']=relations
    # list=[]
    # list.append(result1)
    text="张俊一家三口都是驻村干部，张俊在普安县九峰街道云庄村，妻子蒋冬梅在普安县南湖街道大湾村，儿子张力宇在镇宁县简嘎乡喜妹村"
    predict(text)

