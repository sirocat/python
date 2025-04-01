myUnit = input("단위를 입력하시오. [CcFfQq]: ")
my_Temperature = float(input("기온을 입력하시오. [숫자]: "))
myResult = 0.0

if(myUnit == 'C' or myUnit == 'c'):
    myResult = (my_Temperature * 9/5) + 32
    print(f"변환한 온도는 화씨 {myResult}도 입니다.")
elif(myUnit == 'F' or myUnit == 'f'):
    myResult = (my_Temperature - 32) * 5/9
    print(f"변환한 온도는 섭씨 {myResult}도 입니다.")
elif(myUnit == 'Q' or myUnit == 'q'):
    pass
else:
    print("C, F 또는 Q를 입력하세요.")

    
print("202530231 정주호")




