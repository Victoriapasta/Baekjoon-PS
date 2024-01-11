def solution(a, b):
    answer = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = b
    if a >= 2:
        for i in range(a):
            days += months[i]
        
    return answer[days%7]