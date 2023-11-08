def solution(nums):
    answer = len(nums)//2
    nums_dict = {}
    for i in nums:
        nums_dict[i] = 1
    if len(nums_dict) > answer:
        return answer
    else:
        return len(nums_dict)