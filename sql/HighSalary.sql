/*
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.

NOTE second highest salary does not mean the second element in sorted order, so we should apply 'distinct' in some solution!
*/

-- Solution 1 NOT GOOD
SELECT IFNULL((select e1.salary from Employee e1 where 1 = (select count(e2.salary) from Employee e2 where e2.id <> e1.id and e2.salary > e1.salary) limit 1),null)

-- Solution 2 Same as Solution 1 but more simpler.  NOTE use distinct
SELECT IFNULL((select e1.salary from Employee e1 where 1 = (select count(distinct e2.salary) from Employee e2 where e2.salary > e1.salary) limit 1),null)

-- Solution 3, NOTE use distinct
SELECT IFNULL((select distinct e.salary from Employee e order by salary desc limit 1,1),null)

-- Solution 4, NOTE no distinct!
SELECT IFNULL((select max(e1.salary) from Employee e1 where e1.salary < (select max(e2.salary) from Employee e2)),null)




/*
Stretch 2 to N

Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

Same concern as last problem.
*/

-- Solution 1, Simple, strite straight forward, efficient solution.
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M=N-1;
  RETURN (
    # Write your MySQL query statement below
    select distinct salary from Employee e order by salary desc limit M, 1
  );
END


-- Solution 2, I thought it could be better, but not.
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    select distinct e1.salary from Employee e1 where N-1 = (select count(salary) from (select distinct e3.salary from Employee e3) tmp where tmp.salary > e1.salary)
  );
END

-- Solution 3, function body same as previous solutions. NOTE must have distinct here. 
-- NOTE to gurantee only one column returned we for the outter query we either use distinct or use limit 1 (in this case I use limit 1 which is more efficient!)
-- NOTE the usage of distinct of subquery
select e1.salary from Employee e1 where N-1 = (select count(distinct e3.salary) from Employee e3 where e3.salary > e1.salary) limit 1
