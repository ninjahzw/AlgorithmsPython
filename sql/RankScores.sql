/*
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. 
Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
*/


-- Solution: NOTE sub-query doesn't need to have order by.
-- 1) first select all distinct scores.
-- 2) then apply a cross product on the original table and the tmp table on condition of tmp.score>ori.score and group by id
-- 3) count the number of tmp scores as the rank of current id group.
-- NOTE the usage of group by and count ()
select s.score Score, count(tmp.score) Rank from Scores s,
(
select distinct score from Scores
) as tmp 
where tmp.score >= s.score group by s.id order by score desc
