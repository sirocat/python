myClass = []
print("[우리반 명부 관리]")

while True:
    myMenuNumber = int(input("[1] 추가, [2] 출력, [3] 검색, [0] 종료: "))
    
    if myMenuNumber == 1:  # 학생 추가
        newNumber = int(input("학번: "))
        newName = input("이름: ")
        newPhone = input("전화: ")
        student = {'학번': newNumber, '이름': newName, '전화': newPhone}
        myClass.append(student)
        # myClass[studentNumber] = [studentName,studentPhone]
        
    elif myMenuNumber == 2:  # 리스트 출력
        print("================================")
        print(" 학번  | 이름   | 전화번호")
        print("--------------------------------")
        for student in myClass:
            print(student['학번'], " |", student['이름'], "|", student['전화'])
        # for key in myClass.key():
        #     print(f"   {key()} | {myClass.key(0)} | {myClass.key(1)}")    
        print("================================")
        
    elif myMenuNumber == 3:  # 학번으로 검색
        studentNumber = int(input("검색할 학번 입력: "))
        for student in myClass:
            if student['학번'] == studentNumber:
                print("================================")
                print(" 학번  | 이름   | 전화번호")
                print("--------------------------------")
                print(student['학번'], " |", student['이름'],"|", student['전화'])
                print("================================")
                found = True
                break
        if not found:
            print("해당 학번을 찾을 수 없습니다.")
            
    elif myMenuNumber == 0:
        break
        
    else:
       print(f"invalid number")

print("종료합니다.")
