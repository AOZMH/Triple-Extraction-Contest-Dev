import json
def test():
    list=[]
    list.append(["a","b"])
    list.append(["b","c"])
    list.append(["d","c"])
    return list

if __name__ == '__main__':
    list=test()
    text=json.dumps(list)
    print(list)
    list2=json.loads(text)
    print(list2)
