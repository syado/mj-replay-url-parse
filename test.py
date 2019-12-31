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
# print("アクション:",mjParse.A(o["A"][0],OYA))
print("アクション")
import pprint
pprint.pprint(mjParse.A(o["A"][0],OYA))

print("Z-----")
print("山牌:",mjParse.Z(o["Z"][0]))

print("N-----")
print("名前:",mjParse.N(o["N"][0],OYA))