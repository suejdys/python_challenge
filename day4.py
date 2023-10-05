playing = True

while playing:      #True일때 계속 반복
    first_num = int(input("choose a number:\n"))    #첫번째 수 입력
    second_num = int(input("choose a another one:\n"))  #두번째 수 입력
    ops = input("choose an operation:\n    Options are: +, - , * or /.\n    Write 'exit' to finish.\n") #연산자 또는 exit 입력
    if ops == "+":      #연산자가 +이면 덧셈결과 출력
        print(first_num + second_num)
    elif ops == "-":    #연산자가 -이면 뺄셈결과 출력
        print(first_num - second_num)
    elif ops == "*":    #연산자가 *이면 곱셈결과 출력
        print(first_num * second_num)
    elif ops == "/":    #연산자가 /이면 나눗셈결과 출력
        print(first_num / second_num)
    else:               #다 아니면 종료
        playing = False
    