--https://school.programmers.co.kr/learn/courses/30/lessons/273710

SELECT i.ITEM_ID, i.ITEM_NAME
FROM ITEM_INFO i
JOIN ITEM_TREE t ON i.ITEM_ID = t.ITEM_ID
WHERE t.PARENT_ITEM_ID IS NULL
ORDER BY i.ITEM_ID ASC;