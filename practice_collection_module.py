
from collections import deque
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
from collections import namedtuple
deque_list = deque()
for i in range(5):
    deque_list.appendleft(i)

print(deque_list)
deque_list.rotate(2)
print(deque_list)

d= dict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

def sort_by_key(t):
    return t[0]

for k, v in OrderedDict(sorted(d.items(),key=sort_by_key)).items():
    print(k,v)

s = [("yellow",1),("blue",2),("yellow",3),("blue",4),("red",1)]
d = defaultdict(list)
#d = dict()
print(d)
d["first"]
d["wow"] =102

print(d)


for k,v in s:
    d[k].append(v)

print(d.items())

# defaultDict 사용법은
#https://dongdongfather.tistory.com/69
#참고하자

#이케 출력! 아하 아예 별 값을 안주면 디폴트로 입력형태or 입력값을 줘버리는구나
#defaultdict(<class 'list'>, {})
#defaultdict(<class 'list'>, {'first': [], 'wow': 102})
#dict_items([('first', []), ('wow', 102), ('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])



#counter
text = "Hello alal aaaaaaaaaaaaaaaaaaaa i am taehun jijijijijiji"
c = Counter(text)
print(c,c['a'])
print(list(c.elements()))
#파이썬 기본연산(논리연산 사칙연산..)이 가능.



#namedtuple

Point = namedtuple('Point',['x','y'])#해당 튜플의 이름과 원소들의 이름

p = Point(1,2)
p2 = Point(1,4)

print(p, p2)
print(p2.x,p2.y)
print(p[0],p[1])
