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


def re_api(dat):
    """
    关系识别模型接口
    """
    text = dat['text']
    for ix,itm in enumerate(dat['pairlist']):
        entity1 = itm['entity1']
        entity2 = itm['entity2']
        cand_rel = itm['relations']
        assert(len(cand_rel)>0), "候选关系集为空集!"
        host = '115.27.161.60'
        port = 9303
        client = kbqa_client(host, port)
        res = client.extract_relation(text, entity1, entity2, 1, cand_rel)
        client.stop_client()
        top1_rel = res['Result'][0][0]
        dat['pairlist'][ix]['relation'] = top1_rel
        del dat['pairlist'][ix]['relations']
    
    return dat


if __name__ == "__main__":
    json_obj_input = {'text': '包头稀土高新区经信委主任陈福才表示，近期已有10户企业与银行对接，拟贷款9500万元。', 'pairlist': [{'entity1': '陈福才', 'entity2': '包头稀土高新区经信委主任', 'relations': ['职务']}, {'entity1': '陈福才', 'entity2': '包头稀土高新区经信委', 'relations': ['毕业院校', '任职']}, {'entity1': '包头稀土高新区经信委', 'entity2': '陈福才', 'relations': ['负责人', '创始人', '成员']}]}
    output_json_obj = re_api(json_obj_input)
    #print(output_json_string)
    print(output_json_obj)
