def solution(n):
    sum_multiple = 0
    counter = 1
    while counter < n:
        if counter%15 == 0 or counter%3 == 0 or counter%5 == 0:
            sum_multiple = sum_multiple + counter
        counter+=1
    print(sum_multiple)

solution(1000)