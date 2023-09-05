def solution(players, callings):
    dic = { }
    for i in range(len(players)):
        dic[players[i]] = i
    
    for name in callings:
        current = dic[name]
        
        dic[name] -= 1
        dic[players[current - 1]] += 1
        
        players[current], players[current - 1] = players[current - 1], name
        
    return players