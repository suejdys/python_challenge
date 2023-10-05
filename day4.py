playing = True

while playing:      #True일때 계속 반복
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input("Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n")
    if operation == "+":      #연산자가 +이면 덧셈결과 출력
        print(a + b)
    elif operation == "-":    #연산자가 -이면 뺄셈결과 출력
        print(a - b)
    elif operation == "*":    #연산자가 *이면 곱셈결과 출력
        print(a * b)
    elif operation == "/":    #연산자가 /이면 나눗셈결과 출력
        print(a / b)
    else:               #다 아니면 종료
        playing = False

    