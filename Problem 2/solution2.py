
#This is just a quick and dirty trick
#If you look carefully in Fibonnacci pattern,
#After every 5th value the 6th value will have +1 digit position
#For example 1, 2, 3, 5, 8
#            _  _  _  _  _  =   single digit
#            13, 21, 34, 55, 89
#            __  __  __  __  __ = double digit
#
#From the question we deduce that it has to be less than 4 000 000 
#So 4 000 000 is 7 digits, so 7*5 35                


def solution(max_val, pattern_iteration): 
    n1 , n2 = 0 , 1
    count, total = 0, 0

    while count < pattern_iteration:
        nth = n1 + n2
        #update values

        if nth%2 == 0 :
            if nth < max_val:
                total+= nth
        n1 = n2
        n2 = nth
        count += 1
    print(total)

solution(4000000, 35) 