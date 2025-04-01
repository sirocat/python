totalNumber1 = 0
myUnit = 0

totalNumber1 = int(input("준비한 기념품 총량을 입력하시오. [숫자]: "))
myUnit = int(input("박스의 규격을 정하시오. [숫자]: "))

numPackage = 0
numNonePackage = 0

numPackage = totalNumber1 // myUnit
numNonePackage = totalNumber1 % myUnit


print(f"꾸러미는 {int(numPackage)}개이고 남는 짜투리는 {int(numNonePackage)}개 입니다.")

print("202530231 정주호")




