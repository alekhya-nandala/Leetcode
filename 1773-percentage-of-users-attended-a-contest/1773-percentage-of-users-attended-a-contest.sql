# Write your MySQL query statement below
select contest_id,Round(Count(Distinct user_id)*100/(SELECT COUNT(*) FROM Users),2) as percentage from Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;