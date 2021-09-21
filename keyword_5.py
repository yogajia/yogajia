import sys
import cProfile

def get_keyword_num ():
    num = 0
    key_word=['auto','break','case','char','const','continue','default','do','if','while','static','double','else','enum','extern','float','for','goto','int','long','register','return','short','signed','sizeof','struct','switch','typedef','union','unsigned','void','volatile']
    
    store={}  #创建一个字典保存文件中的关键字

    put_1 = []   #存放switch和case的列表
    put_2 = []   #存放case个数
    put_3 = []   #存放函数返回的列表

    lay_1 = []   #存放ifelse的列表

    file = open(sys.argv[1],"r",encoding='utf-8')  #打开txt格式且编码为UTF-8d的文本

    flag = sys.argv[2]

    while(1):
        lines = file.readlines()            #按行读入文件
        for line in lines:      #循环遍历每行的词语并统计个数
            line = line.replace(",","").replace(".","").replace("{"," ").replace("}"," ").replace(":","").replace(";","").replace("?","").replace("("," ").replace(")"," ")
            #将代码中的符号替换为空格
            count = line.split()   #提取出line中的单词组成列表

            for word in count:
                if len(word) < 2:   #排除单个字的干扰，使得输出结果为词语
                    continue 
                else:
                    store[word] = store.get(word,0)+1    #如果字典里键为word的值存在，则返回键的值并加一，否则，返回0，再加1

            put_3 = get_switchcase_num(count)
            put_1.extend(put_3)

            line_1 = " ".join(count)
            if line_1.find("else if") != -1:
                lay_1.append('1')
            elif line_1.find("if") != -1:
                lay_1.append('0')
            elif line_1.find("else") != -1:
                lay_1.append('2')
            else:
                continue

        for key in list(store.keys()):      #遍历字典的所有键，如果不是列表里的关键字则删除
            if key not in key_word:
                del store[key]
        
        if not lines:
            break

    for key in store:                     #for循环统计关键词出现次数
        if key in key_word:
            num = num + store[key]           
    
    cun =0
    sum = 0                                  #统计siwitch和case关键词出现次数
    put_1.reverse()
    for word in put_1:
        if word == "switch":
            if cun != "0":
                put_2.append(cun)
            cun = 0 
            sum = sum + 1   
        if word == "case":
            cun = cun+1
    put_2.reverse()

    cun_1 = 0
    cun_2 = 0
    for x in range(len(lay_1)):
        if lay_1[x] == '0' and lay_1[x+1] == '2':
            cun_1 = cun_1 +1
        if lay_1[x] == '2':
            cun_2 = cun_2 + 1

    if sys.argv[2] == '1':
        print("total num: ",num)
        print("switch num: ",sum)
    elif sys.argv[2] == '2':
        print("total num: ",num)
        print("switch num: ",sum)
        print("case num: "," ".join(str(i) for i in put_2))
    elif sys.argv[2] == '3':
        print("total num: ",num)
        print("switch num: ",sum)
        print("case num: "," ".join(str(i) for i in put_2))
        print("if-else num: ",cun_1)
    elif sys.argv[2] == '4':
        print("total num: ",num)
        print("switch num: ",sum)
        print("case num: "," ".join(str(i) for i in put_2))
        print("if-else num: ",cun_1)
        print("if-elseif-else num: ",cun_2-cun_1)
    else:
        print(flag)
        
    file.close()
    return

def get_switchcase_num(count):
    put = []
    for word in count:
        if word == "switch":
            put.append(word)
        if word == "case":
            put.append(word)
    return put

if __name__ == "__main__":
    get_keyword_num ()
    cProfile.run('get_keyword_num ()')