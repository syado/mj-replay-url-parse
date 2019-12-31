def toHainame(i):
    d = {
        "1": "萬子1",
        "2": "萬子2",
        "3": "萬子3",
        "4": "萬子4",
        "5": "萬子5",
        "6": "萬子6",
        "7": "萬子7",
        "8": "萬子8",
        "9": "萬子9",
        "0": "萬子5赤",
        "a": "索子1",
        "b": "索子2",
        "c": "索子3",
        "d": "索子4",
        "e": "索子5",
        "f": "索子6",
        "g": "索子7",
        "h": "索子8",
        "i": "索子9",
        "-": "索子5赤",
        "j": "筒子1",
        "k": "筒子2",
        "l": "筒子3",
        "m": "筒子4",
        "n": "筒子5",
        "o": "筒子6",
        "p": "筒子7",
        "q": "筒子8",
        "r": "筒子9",
        "s": "筒子5赤",
        "t": "東",
        "u": "南",
        "v": "西",
        "w": "北",
        "x": "白",
        "y": "發",
        "z": "中"
    }
    return d[str(i)]

def toHainames(s):
    return [toHainame(i) for i in s]
        
def get_playerposition(num):
    d = {
        0: "下",
        1: "右",
        2: "上",
        3: "左"
    }
    return d[int(num)]

def get_kyoku(num):
    d = {
        0: "東一局",
        1: "東二局",
        2: "東三局",
        3: "東四局",
        4: "南一局",
        5: "南二局",
        6: "南三局",
        7: "南四局",
    }
    return d[int(num)]

def get_honba(num):
    return str(num)+"本場"

def get_kyoutaku(num):
    return str(num)+"本"

def get_tensu(s,oyaposition):
    l = lambda x: int(x) * 100
    tensu = list(map(l,s.split("_")))
    tensu = tensu[oyaposition:] + tensu[:oyaposition]
    kaze = ["東","南","西","北"]
    d = {}
    for i in range(len(tensu)):
        d[kaze[i]] = tensu[i]
    return d

def get_tehai(s,oyaposition):
    l = lambda x: toHainames(sorted(x))
    tehai_list = list(map(l,s.split("_")))
    tehai_list = tehai_list[oyaposition:] + tehai_list[:oyaposition]
    kaze = ["東","南","西","北"]
    d = {}
    for i in range(len(tehai_list)):
        d[kaze[i]] = tehai_list[i]
    return d

def get_action(s,oyaposition):
    s = list(s)
    al = []
    kaze = ["東","南","西","北"]
    # if oyaposition != 0:
    #     kaze = kaze[4-oyaposition:]+kaze[:-oyaposition]
    # print(kaze)
    sute = True
    kaze_i = 0
    skip = 0
    end = False    
    l = lambda x: toHainame(x)
    for i in range(len(s)):
        if skip > 0:
            skip -= 1
        else:
            skip = 0
            if s[i] == "_":
                a = ["ツモ切り",l(s[i-1])]
                s[i] = s[i-1]
                sute = True
            elif s[i] == "R":
                a = "リーチ"
            elif s[i] == "C":
                a = ["チー",l(s[i-1]),l(s[i+1]),l(s[i+2])]
                skip += 2
                sute = False
            elif s[i] == "P":
                a = ["ポン",l(s[i-1])]
                kaze_i = int(s[i+1])-oyaposition
                skip = 1
                sute = False
            elif s[i] == "K":
                a = ["加槓",l(s[i+1])]
                skip = 1
            elif s[i] == "A":
                a = ["暗槓",l(s[i+1])]
                skip = 1
            elif s[i] == "M":
                a = ["明槓",l(s[i+1])]
                kaze_i = int(s[i+1])-oyaposition
                skip = 1
            elif s[i] == "D":
                a = ["ドラ",l(s[i+1])]
                skip = 1
            elif s[i] == "L":
                a = ["リンシャン",l(s[i+1])]
                skip = 1
            elif s[i] == "U":
                a = ["裏ドラ",l(s[i+1])]
                skip = 1
            elif s[i] == "~":
                end = True
                kaze_i = int(s[i+1])-oyaposition
                if (int(s[i+2],16)-2)%3 == 0:
                    a = "ツモ"
                else:
                    a = "ロン"
                skip += 2                
                sute = False
                    
            elif s[i] == ".":
                a = "流局"
                skip += 1
                end = True
            elif s[i] == "T":
                a = []
                for j in range(len(kaze)):
                    k = kaze[(j-oyaposition)%4]
                    if s[i+1+j] == "0":
                        a.append([k,"ノーテン"])
                    elif s[i+1+j] == "1":
                        a.append([k,"テンパイ"])
                skip += 4
                
            else:
                if sute:
                    sute = False
                    a = ["引く", l(s[i])]
                else:
                    sute = True
                    a = ["捨て", l(s[i])]
            al.append([kaze[kaze_i%4],a])
            if sute and not end:
                kaze_i += 1
    return al

def get_name(s,oyaposition):
    l = lambda x: x
    name_list = list(map(l,s.split("_")))
    name_list = name_list[oyaposition:] + name_list[:oyaposition]
    kaze = ["東","南","西","北"]
    d = {}
    for i in range(len(name_list)):
        d[kaze[i]] = name_list[i]
    return d

def get_test(actions): 
    states = {"東":{},"南":{},"西":{},"北":{}}
    richi_ippatsu = {"東":False,"南":False,"西":False,"北":False}
    jyunme = 0
    kaze_num = {"東":0,"南":1,"西":2,"北":3}
    for i,x in enumerate(actions):
        if x[0] == "東" and actions[i-1][0] != "東":
            jyunme += 1
        if not type(x[1]) == type([]):
            if x[1] in ["ロン","ツモ"]:
                states[x[0]][x[1]] = jyunme
                if richi_ippatsu[x[0]] and states[x[0]]["リーチ"]+1 >= jyunme:
                    states[x[0]]["一発"] = True
            if x[1] == "リーチ":
                states[x[0]]["リーチ"] = jyunme
                richi_ippatsu[x[0]] = True
        else:
            if x[1][0][1] == "槓":
                richi_ippatsu = {"東":False,"南":False,"西":False,"北":False}
                if x[0] != "東" and kaze_num[actions[i-1][0]]<kaze_num[x[0]]:
                    jyunme += 1
            if x[1][0] in ["ポン","チー"]:
                richi_ippatsu = {"東":False,"南":False,"西":False,"北":False}
                if x[0] != "東" and kaze_num[actions[i-1][0]]<kaze_num[x[0]]:
                    jyunme += 1
    return states

def B(mode,num):
    """mode 何桁目か指定
    mode 0 局
    mode 1 本場
    mode 2 供託
    mode 3 親の位置
    mode 9 全てを配列で返す"""
    if mode==0:
        return get_kyoku(num)
    elif mode==1:
        return get_honba(num)
    elif mode==2:
        return get_kyoutaku(num)
    elif mode==3:
        return get_playerposition(num)
    elif mode==9:
        return [get_kyoku(num[0]),
        get_honba(num[1]),
        get_kyoutaku(num[2]),
        get_playerposition(num[3])]
    else:
        raise Exception('Error!')

def T(s,oyaposition):
    return get_tensu(s,oyaposition)

def D(hai):
    return toHainame(hai)

def S(s):
    return [int(s[0]),int(s[1])] 

def H(s,oyaposition):
    return get_tehai(s,oyaposition)

def A(s,oyaposition):
    return get_action(s,oyaposition)

def Z(s):
    return toHainames(s)

def N(s,oyaposition):
    return get_name(s,oyaposition)