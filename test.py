from urllib.parse import urlparse,parse_qs
import mjParse

url=input("url>> ")
url_parse = urlparse(url)
o = parse_qs(url_parse.query)

OYA = 0
print("B-----")
print(mjParse.B(0,o["B"][0][0]),end=" ")
print(mjParse.B(1,o["B"][0][1]),end=" ")
print("供託:",mjParse.B(2,o["B"][0][2]),end=" ")
print("親:",mjParse.B(3,o["B"][0][3]))
print(mjParse.B(9,o["B"][0]))
OYA = int(o["B"][0][3])

print("T-----")
print(mjParse.T(o["T"][0],OYA))

print("D-----")
print("ドラ:",mjParse.D(o["D"][0]))

print("S-----")
print("サイコロ:",mjParse.S(o["S"][0]))

print("H-----")
print("配牌:")
for key,vales in mjParse.H(o["H"][0],OYA).items():
    print(key,vales)

print("A-----")
print("アクション:",mjParse.A(o["A"][0],OYA))
# print("アクション")
import pprint
# pprint.pprint(mjParse.A(o["A"][0],OYA))

print("Z-----")
print("山牌:",mjParse.Z(o["Z"][0]))

print("N-----")
print("名前:",mjParse.N(o["N"][0],OYA))

states = {"東":{},"南":{},"西":{},"北":{}}
richi_ippatsu = {"東":False,"南":False,"西":False,"北":False}
jyunme = 0
actions = mjParse.A(o["A"][0],OYA)
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
                print("a")
        if x[1][0] in ["ポン","チー"]:
            richi_ippatsu = {"東":False,"南":False,"西":False,"北":False}
            if x[0] != "東" and kaze_num[actions[i-1][0]]<kaze_num[x[0]]:
                jyunme += 1
                print("b")
    print(jyunme,x)
print(states)