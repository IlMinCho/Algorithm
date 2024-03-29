--https://school.programmers.co.kr/learn/courses/30/lessons/276034

SELECT a.ID, a.EMAIL, a.FIRST_NAME, a.LAST_NAME
FROM DEVELOPERS a
WHERE a.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python')
    OR a.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')
ORDER BY a.ID ASC;