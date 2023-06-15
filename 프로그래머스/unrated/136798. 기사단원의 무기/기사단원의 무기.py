def Divisor(n):
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
                
    return len(divisorsList)

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        temp = Divisor(i)
        if temp > limit:
            temp = power
        answer += temp
        
    return answer