/*
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

IDea:
NOTE this is a typical SELF JOIN problem!
*/

-- Solution 1
select e1.name from Employee e1 left join Employee e2 on e1.managerid = e2.id where e1.salary > e2.salary

-- Solution 2
select e1.name from Employee e1 left join Employee e2 on e1.managerid = e2.id where e1.salary > e2.salary
