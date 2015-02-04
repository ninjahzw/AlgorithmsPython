/*
The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+

Idea:
NOTE that this looks like 'group by' should be used, but actuallhy group by is a aggregate function, it can't be used on operate on each group.
*/

select D.Name as Department, E.Name as Employee, E.Salary as Salary 
  from Employee E, Department D
  where (select count(distinct(Salary)) from Employee 
             -- in (0, 1, 2)or < 3
             where DepartmentId = E.DepartmentId and Salary > E.Salary) in (0, 1, 2)
        -- Join operation
        and E.DepartmentId = D.Id;
