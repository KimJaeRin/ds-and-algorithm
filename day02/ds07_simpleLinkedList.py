# file : ds07_simpleLinkedList.ipynb
# desc : 단순 연결 리스트 일반 구현

memory = [] #컴퓨터 메모리를 유사구성
#head = node
head, curr, prev = None, None, None  #일반 변수

# 연결 리스트 노드 클래스
class Node():
    # data, link 두 개의 멤버변수 존재
    # 생성자 추가
    def __init__(self, name) -> None:
        self.data = name
        self.link = None

def printNodes(start):
    curr = start
    if curr == None: return # 함수를 빠져나감
    print(curr.data, end = ' --> ')
    while curr.link != None:
        curr = curr.link # 내 노드 다음의 노드가 current가 된다
        print(curr.data, end=' --> ')
    print() # enter 추가

dataArray = ['다현','정연','쯔위','사나','지효']

#메인 시작
if __name__=='__main__':
    node = Node(dataArray[0]) #'다현' 데이터 담은 노드 생성
    head = node #첫번째 값을 head가 가리킴
    memory.append(node) #가짜 메모리에 집어넣음

    for data in dataArray[1:]: #두번째 노드부터 끝까지
        prev = node
        node = Node(data) #정연부터 들어감
        prev.link = node
        memory.append(node)

    printNodes(head)
