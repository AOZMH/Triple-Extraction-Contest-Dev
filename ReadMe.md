# 铸基计划-信息抽取项目方案

## Step 1
    通过百度paddle进行中文分词，识别实体类型，输出为[实体1，实体类型]数组，
    格式为[JSON],其中JSON格式为{entityname:'F-22轰炸机',entitytype:'武器装备'}
  

## Step 2

    对实体数组进行排列组成，形成实体对数组（结合Table文件，如果两两实体之间没有关系，
    则不形成实体对，否则形成[实体对，可能的关系] 这种类型的数组，例如
    [["报道还提到，4月29日，两架B-1B轰炸机曾从美国本土远程奔赴中国南海参加演习。", "B-1B轰炸机", "美国", ["使用国家", "所属国家"]], ]
    
## Step 3

    对实体对数组进行判断，如果只有一种可能的关系，则为该关系，否则进行关键词判断（需要定义关键词
    列表），输出为[实体对，确定的关系]这种类型的数组，格式如下：
    [['B-1B轰炸机', '美国', '所属国家'], ]


## Step 4

    对Step 3输出的数组，按照比赛要求，封装成相应格式的JSON对象并输出，格式为
    {"text":"第一次、第二次会议分别于2017年、2018年在菲律宾苏比克和中国广州举行。",
    "sro_list":[{"subject":"菲律宾","object":"苏比克","relation":"城市"},
    {"subject":"中国","object":"广州","relation":"城市"}]}
    
    
## 注意事项

    比赛机器只有CPU，没有GPU

    
  
