--https://school.programmers.co.kr/learn/courses/30/lessons/273711

SELECT i.ITEM_ID, i.ITEM_NAME, i.RARITY
FROM ITEM_INFO i
JOIN ITEM_TREE t ON i.ITEM_ID = t.ITEM_ID
JOIN ITEM_INFO rare_items ON rare_items.ITEM_ID = t.PARENT_ITEM_ID
WHERE rare_items.RARITY = 'RARE'
ORDER BY i.ITEM_ID DESC;