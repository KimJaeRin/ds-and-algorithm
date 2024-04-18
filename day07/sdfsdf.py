##함수 선언

def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE -1):
        return True
    else:
        return False
    
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
    
def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print('스택이 꽉 찼습니다.')
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택이 비었습니다.')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택이 비었습니다.')     
    return stack[pop]

##전역변수
SIZE = int(input('스택 크기를 입력하세요 : '))
stack = [None for _ in range (SIZE)]
top = -1

## 메인코드

if __name__ == '__main' :
    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 : ')



    while (select.lower() =='x'):
    
        if select.lower() == 'i':
            data = input('입력할 데이터 : ')
            push(data)
            print(f'스택 상태 :{stack}')
        elif select.lower() == 'e':
            data = pop()
            print(f'추출 데이터 : {data}')    
            print(f'스택 상태 : {stack}')
        elif select.lower() == 'v':
            data = peek()
            print(f'확인된 데이터 : {data}')    
            print(f'스택 상태 : {stack}')      
        else:
            print('입력이 잘못됨')

        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 : ')

    print('프로그램 종료')
