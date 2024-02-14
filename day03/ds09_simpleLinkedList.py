# file : ds09_simpleLinkedList.py
# desc : 단순연결리스트 전체 구현

# 노드 클래스
class Node():
    data = None # 실제 데이터 변수
    link = None # 다음 노드 지정하는 변수

    def __init__(self) -> None:
        self.data = None #클래스 자신이 self이므로 클래스의 변수에 접근하려면 반드시 self
        self.link = None

def printNodes(start): #start부터 시작해서 끝까지 노드.data 출력
    curr = start # start == head
    if curr == None: return
    while True:
        if curr.link == None:
            print(curr.data)
            break
        else:
            print(curr.data, end = '-->')
            curr = curr.link
def insertNode(find, data):
    global head, prev, curr # 전역변수를 insertNode()에서 사용하겠다고 선언

    if head.data == find:
        node = Node()
        node.data = data
        node.link = head
        head = node
        return
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data == find:
            node = Node()
            node.data = data
            node.link = curr
            prev.link = node
            return
    node = Node() #맨 마지막에 노드 삽입
    node.data = data
    curr.link = node
    return
#노드 삭제함수

def deleteNode(data):
    global head, prev, curr

    if head.data == data:
        curr = head
        head = head.link
        del(curr)
        return
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        
        if curr.data == data:
            prev.link = curr.link
            del(curr)
            return

#노드 검색함수

def findNode(find):
    global head, curr

    curr = head
    if curr.data == find:
        return curr #현재 노드를 리턴해주고 함수탈출
    while curr.link != None:
        curr = curr.link #다음 노드로
        if curr.data == find:
            return curr
    return Node() # 위에 만족 못하면 빈노드 리턴함수 탈출

# 전역변수
head, prev, curr = None, None, None
originData = ['다현', '정연', '쯔위', '사나', '지효']


#메인코드 영역
if __name__ =='__main__':
    node=Node()
    node.data = originData[0] # = 다현
    head = node #head는 node를 가르킴

    for name in originData[1:]:
        prev = node
        node = Node()
        node.data = name
        prev.link = node

# 연결리스트 구성완료
print('최초 구성된 연결리스트')
printNodes(head)

print('노드 추가')
insertNode('다현', '정국')
printNodes(head)

print('중간 노드 삽입')
insertNode('사나','미미')
printNodes(head)

insertNode('재남','알엠')
print('마지막 노드 삽입')
printNodes(head)

# 노드 삭제

deleteNode('정국')
print('맨 앞 노드 삭제')
printNodes(head)

deleteNode('쯔위')
print('중간 노드 삭제')
printNodes(head)

# 노드 검색
fNode = findNode('다현')
printNodes(head)
print (f'찾은 노드: {fNode.data}')

fNode = findNode('쯔위')
printNodes(head)
print (f'찾은 노드: {fNode.data}')

