def solution(num_list):
    answer = 0
    sum1 = 1
    sum2 = 0
    for i in num_list:
        sum1 *= i
        sum2 += i
        

    if sum1 < sum2*sum2:
        return 1
    else:
        return answer