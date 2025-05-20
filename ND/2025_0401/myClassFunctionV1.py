myClass = []

def printHeader():
    print("================================")
    print(" 학번  | 이름   | 전화번호")
    print(" NO    | name   |  phone  ")
    print("--------------------------------")

def printFooter():
    print("================================")

print("[우리반 명부 관리]")

while True:
    myMenuNumber = int(input("[1] 추가, [2] 출력, [3] 검색, [0] 종료: "))
    
    if myMenuNumber == 1:  # 학생 추가
        newNumber = int(input("학번: "))
        newName = input("이름: ")
        newPhone = input("전화: ")
        student = {'학번': newNumber, '이름': newName, '전화': newPhone}
        myClass.append(student)
        
    elif myMenuNumber == 2:  # 리스트 출력
        printHeader()
        for student in myClass:
            print(student['학번'], " |", student['이름'], "|", student['전화'])
        printFooter()
        
    elif myMenuNumber == 3:  # 학번으로 검색
        studentNumber = int(input("검색할 학번 입력: "))
        found = False  # 검색 결과 초기화
        for student in myClass:
            if student['학번'] == studentNumber:
                printHeader()
                print(student['학번'], " |", student['이름'], "|", student['전화'])
                printFooter()
                found = True
                break
        if not found:
            print("해당 학번을 찾을 수 없습니다.")
            
    elif myMenuNumber == 0:
        break
        
    else:
        print("invalid number")

print("종료합니다.")
