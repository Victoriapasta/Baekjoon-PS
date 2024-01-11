def solution(progresses, speeds):
    answer = []
    while progresses:
        temp = 0
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            temp += 1
            if not progresses:
                break
                
        if temp:
            answer.append(temp)
        
    return answer