from urllib import parse, request
import json
def test(textmod):
    textmod = parse.urlencode(textmod)
    # 输出内容:user=admin&password=admin
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    url = 'http://39.99.170.154:8000/api/'
    req = request.Request(url='%s%s%s' % (url, '?', textmod), headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    #print(res)
    # 输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'

    result=res.decode(encoding='utf-8')
    # 输出内容:登录成功
    return result


if __name__ == '__main__':
    # print("这是测试程序")
    # result=max(3,4,45)
    # print(result)
    # textmod = {'text': '中国首都是北京'}
    # result=test(textmod)
    # print(result)
    text='["陈福才", "人物"], ["包头稀土高新区经信委主任", "职位"], ["包头稀土高新区经信委", "组织机构"]'

    obj=json.loads(text)
    print(obj)