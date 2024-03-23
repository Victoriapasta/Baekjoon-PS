
def solution(bandage, health, attacks):
    time = attacks[-1][0]
    nowHP = health
    attackTime = [attack[0] for attack in attacks]
    attackDamage = [attack[1] for attack in attacks]
    
    conSucess = 0
    
    for i in range(time+1):
        # 몬스터가 공격하는 시간 일 때
        if i in attackTime:
            # 연속성공 초기화
            conSucess = 0
            nowHP -= attackDamage[attackTime.index(i)] 
            
            # 체력이 0 이하면 죽고 게임 종료
            if nowHP <= 0:
                return -1
            
            continue
            
        # 붕대감기
        conSucess += 1
        nowHP += bandage[1]
        
        #연속성공 최대로 하면
        if conSucess == bandage[0]:
            nowHP += bandage[2]
            conSucess = 0
            
        # 현재 체력이 최대 체력을 넘을 수 없음
        if nowHP > health:
            nowHP = health
            
    return nowHP