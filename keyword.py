import sys

def get_keyword_num ():
    num = 0
    key_word=['auto','break','case','char','const','continue','default','do','if','while','static','double','else','enum','extern','float','for','goto','int','long','register','return','short','signed','sizeof','struct','switch','typedef','union','unsigned','void','volatile']
    
    store={}  #创建一个字典保存文件中的关键字

    file = open("code.txt","r",encoding='utf-8')  #打开txt格式且编码为UTF-8d的文本
    while(1):
        lines = file.readlines()            #按行读入文件
        for line in lines:      #循环遍历每行的词语并统计个数
            line=line.replace(",","").replace(".","").replace("{"," ").replace("}"," ").replace(":","").replace(";","").replace("?","").replace("("," ").replace(")"," ")
            count = line.split()
            for word in count:
                if len(word) < 2:   #排除单个字的干扰，使得输出结果为词语
                    continue 
                else:
                    store[word] = store.get(word,0)+1    #如果字典里键为word的值存在，则返回键的值并加一，否则，返回0，再加1

        for key in list(store.keys()):      #遍历字典的所有键，如果不是列表里的关键字则删除
            if key not in key_word:
                del store[key]
        
        if not lines:
            break

    for key in store:
        if key in key_word:
            num = num + store[key]            #统计关键词出现次数

    print("total num: ",num)
    print("switch num: ",store['switch'])
    file.close()
    return

if __name__ == "__main__":
    get_keyword_num ()