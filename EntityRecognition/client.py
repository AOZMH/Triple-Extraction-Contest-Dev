from socket import *
import json

# 输入一个句子，构造模型的输入数据，即以字分割，并且用伪标签标注
def build_input(sens):
    slen = len(sens);
    pstr = "";
    sstr = "";
    for i in range(slen-1):
        sstr += sens[i]+'\x02';
    sstr += sens[slen-1];
    for i in range(slen-1):
        pstr += 'O\x02';
    pstr += 'O'
    return sstr+'\t'+pstr+'\n';

# 写入文件
def get_ner(sens):
    fout = open('data/testeval.tsv','w',encoding='utf-8');
    sstr = build_input(sens);
    fout.write('text_a\tlabel\n');
    fout.write(sstr);
    # PaddleNLP本身的问题，需要不止一条数据,这个用于凑数
    fout.write('除^B了^B他^B续^B任^B十^B二^B届^B政^B协^B委^B员^B,^B马^B化^B腾^B,^B雷^B军^B,^B李^B彦^B宏^B也^B被^B推^B选^B为^B新^B一^B届^B全^B国^B人^B大^B代^B表^B或^B全^B国^B政^B协^B委^B员     p-B^Bp-I^Br-B^Bv-B^Bv-I^Bm-B^Bm-I^Bm-I^BORG-B^BORG-I^Bn-B^Bn-I^Bw-B^BPER-B^BPER-I^BPER-I^Bw-B^BPER-B^BPER-I^Bw-B^BPER-B^BPER-I^BPER-I^Bd-B^Bp-B^Bv-B^Bv-I^Bv-B^Ba-B^Bm-B^Bm-I^BORG-B^BORG-I^BORG-I^BORG-I^Bn-B^Bn-I^Bc-B^Bn-B^Bn-I^BORG-B^BORG-I^Bn-B^Bn-I'+'\n');
    fout.close();



# 入口函数
def entry(sens):
    ip_port = ("59.108.48.45",4235);
    back_log = 5;
    buff_size = 1024

    tcp_client = socket();
    tcp_client.connect(ip_port)

    get_ner(sens);
    tcp_client.send(sens.encode("utf-8"));
    data = tcp_client.recv(buff_size);
    print("输入句子: "+sens);
    print("输出结果: "+data.decode('utf-8'));
    tcp_client.close();
    #jsonobj=json.loads(data.decode('utf-8'))
    #jsontext=json.dumps(jsonobj)
    #print(jsontext)
    return data.decode('utf-8');
    #return list2

if __name__ == "__main__":

    entry('张三和李四都是好孩子');
