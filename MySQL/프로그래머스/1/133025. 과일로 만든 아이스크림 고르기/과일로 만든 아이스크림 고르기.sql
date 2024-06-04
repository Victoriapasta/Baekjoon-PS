-- 코드를 입력하세요
SELECT a.FLAVOR
FROM first_half as a join icecream_info as b
on a.flavor = b.flavor
WHERE TOTAL_ORDER >= 3000 AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER desc;