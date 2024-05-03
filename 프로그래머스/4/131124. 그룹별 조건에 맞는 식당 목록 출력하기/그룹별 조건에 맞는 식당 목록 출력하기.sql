-- 코드를 입력하세요
SELECT B.MEMBER_NAME, A.REVIEW_TEXT,
       DATE_FORMAT(A.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW A
JOIN MEMBER_PROFILE B
ON A.MEMBER_ID = B.MEMBER_ID
WHERE A.MEMBER_ID = (SELECT MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     ORDER BY COUNT(*) DESC LIMIT 1)
ORDER BY REVIEW_DATE, REVIEW_TEXT