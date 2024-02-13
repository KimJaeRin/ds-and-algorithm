##file : ds05_orderedList.py


def printPoly(p_x):
    term = len(p_x) -1   #최고차장 숫자 = 배열길이 -1
    polyStr = 'p(x) = '

    for i in range(len(p_x)):
        coef = p_x[i]   #계수

        if (coef>= 0):
            polyStr +="+"
        polyStr += str(coef) + 'x^ ' + str (term) + ''
        term -= 1
        
    return polyStr

def calcPoly(xVal,p_x):
    retValue = 0
    term = len(p_x) -1    #최고차할 숫자 = 배열길이 - 1

    for i in range(len(px)) :
        coef = p_x[i]   #계수
        retValue += coef * xVal ** term
        term -= 1

    return retValue

#전역변수 선언
px = [7,-4,0,5]     

##메인코드

if __name__=='__main__':

    pStr = printPoly(px)
    print(pStr)

    xValue = int(input('X 값 --> '))

    pxValue = calcPoly(xValue,px)
    print(pxValue)

