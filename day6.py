numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]
totals=0        #기본값 지정

for items in numbers:       #for를 사용해 list(numbers)의 각 항목을 하나씩 items 변수로 루프
    if type(items) is int:      #리스트의 항목이 자료형이면 totals = 기존 + items(숫자)
        totals = totals + items
print(totals)       #더한 모든값 출력 = 136