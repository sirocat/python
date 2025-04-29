print("정수 2개를 입력하시오")
myNum1 = int(input("첫번째 정수 : "))
myNum2 = int(input("두번째 정수 : "))

if(myNum1 == 0 or myNum2 == 0):
    print("프로그램을 종료합니다.")
else:
    myFactorial1 = 1
    myFactorial2 = 1
    for i in range(2,myNum1+1):
        myFactorial1 *=i
    for i in range(2,myNum2+1):
        myFactorial2 *=i
    print(f"두 정수의 팩토리얼은 각각 {myFactorial1}, {myFactorial2}")

    if(myFactorial1<myFactorial2):
        print(f"두 팩토리얼의 차(절대값)는 {myFactorial2-myFactorial1}")
    else:
        print(f"두 팩토리얼의 차(절대값)는 {myFactorial1-myFactorial2}")
