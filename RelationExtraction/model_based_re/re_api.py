import socket
import json

class kbqa_client():
    
    def __init__(self, host_ip, port):
        super(kbqa_client, self).__init__()
        self.conn = socket.socket()
        self.host = host_ip
        self.port = port
        self.conn.connect((self.host, self.port))

    def extract_nodes(self, ques):
        # Extract all nodes in ques (a string)
        # Returns a list of nodes, each resembles: [node, type_of_node, position_in_ques]

        msg = {}
        msg['type'] = 'NC'
        msg['sent'] = ques
        
        self.conn.send(json.dumps(msg).encode('utf-8'))
        nodes = self.conn.recv(5120).decode()
        return json.loads(nodes)

    def extract_relation(self, ques, mention1, mention2, K, cand_rel=[]):
        # Select the most probable relation between mention 1&2 in ques
        # Selection is done from candidate relations.
        # If candidates are not provided, the selection is performed on all relations appeared in CCKS-2019-CKBQA dataset
        
        msg = {}
        msg['type'] = 'RE'
        msg['ques'] = ques
        msg['m1'] = mention1
        msg['m2'] = mention2
        msg['cand_rel'] = cand_rel
        msg['K'] = K
        self.conn.send(json.dumps(msg).encode('utf-8'))
        topk_rel = self.conn.recv(10000).decode()
        return eval(topk_rel)

    def stop_client(self):
        self.conn.close()


def re_api(json_string):
    """
    输入为string形式，可以通过json.dumps(json_obj)生成；之所以用string交互是为了跨语言/平台兼容，输入后通过json.loads转换、解析json参数
    参数格式为[text, entity1, entity2, cand_rel]，分别为需要抽取信息的文本、文本中识别出的两个实体、这两个实体之间的候选关系
    E.g. json_string = "[\"报道还提到，4月29日，两架B-1B轰炸机曾从美国本土远程奔赴中国南海参加演习。\", \"B-1B轰炸机\", \"美国\", [\"使用国家\", \"所属国家\"]]"

    输出为[entity1, entity2, top_1_relation]，通过json.dumps以string格式输出
    """
    dat = json.loads(json_string)
    ret = []
    for text, entity1, entity2, cand_rel in dat:
        assert(len(cand_rel)>0), "候选关系集为空集!"
        host = '115.27.161.60'
        port = 9303
        client = kbqa_client(host, port)
        res = client.extract_relation(text, entity1, entity2, 1, cand_rel)
        client.stop_client()
        top1_rel = res['Result'][0][0]
        ret.append([entity1, entity2, top1_rel])
    
    return json.dumps(ret)


if __name__ == "__main__":
    json_string = "[[\"报道还提到，4月29日，两架B-1B轰炸机曾从美国本土远程奔赴中国南海参加演习。\", \"B-1B轰炸机\", \"美国\", [\"使用国家\", \"所属国家\"]]]"
    output_json_string = re_api(json_string)
    #print(output_json_string)
    print(json.loads(output_json_string))
