/*
The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
*/


-- NOTE can not handle two employees on a same dept have same salary.
select d.name, e.name, max(e.salary) from Department d join Employee e on e.DepartmentId = d.Id group by d.Id
-- GOT: (only output the first one.)
/*
Input:  {"headers": {"Employee": ["Id", "Name", "Salary", "DepartmentId"], "Department": ["Id", "Name"]}, "rows": {"Employee": [[1, "Joe", 60000, 1], [4, "Max", 60000, 1]], "Department": [[1, "IT"]]}}
Output: {"headers": ["name", "name", "max(e.salary)"], "values": [["IT", "Joe", 60000]]}
Expected:   {"headers": ["Department", "Employee", "Salary"], "values": [["IT", "Joe", 60000], ["IT", "Max", 60000]]}
*/
-- the following solution yields same error to the previous one
select t.dName, e1.name, t.sal from (select max(e.salary) sal, d.Id dId, d.Name dName from Department d join Employee e on e.DepartmentId = d.Id group by d.Id) t, Employee e1 where t.dId = e1.DepartmentId and e1.Salary = t.sal group by t.dId

-- Correct Solution:
/*
Idea:
Create a tmp table t, calculate max salary for each department. then join table t with employee
and choose people whose salary is equal to department max.
NOTE we do not need group by again, because the condition: t.dId = e1.DepartmentId
can satisfy 'each employee to specific department' conditoon.
*/
select t.dName, e1.name, e1.Salary from (select max(e.salary) sal, d.Id dId, d.Name dName from Department d join Employee e on e.DepartmentId = d.Id group by d.Id) t, Employee e1 where t.dId = e1.DepartmentId and e1.Salary = t.sal

/*
NOTE !! IMPORTANT
The following approach use same approach to other similiar problems!!
*/
SELECT d1.Name, e1.Name, e1.Salary FROM Employee e1 JOIN Department d1 ON e1.DepartmentId = d1.Id WHERE 0 = (SELECT COUNT(DISTINCT e2.Salary) FROM Employee e2 WHERE e2.DepartmentId = e1.DepartmentId and e2.Salary > e1.Salary)
/*
NOTE concerning Group by:
mysql> select * from reserves;
+-----+-----+---------------------+
| sid | bid | day                 |
+-----+-----+---------------------+
|  22 | 101 | 1998-10-10 00:00:00 |
|  22 | 102 | 1998-10-10 00:00:00 |
|  22 | 104 | 1998-10-07 00:00:00 |
|  22 | 104 | 1998-10-08 00:00:00 |
|  31 | 102 | 1998-11-10 00:00:00 |
|  31 | 103 | 1998-11-06 00:00:00 |
|  31 | 104 | 1998-11-12 00:00:00 |
|  64 | 101 | 1998-09-05 00:00:00 |
|  64 | 102 | 1998-09-08 00:00:00 |
|  74 | 103 | 1998-09-08 00:00:00 |
+-----+-----+---------------------+
10 rows in set (0.00 sec)

mysql> select sid, bid from reserves r group by sid;  ## NOTE it will not report error! instead it returns first bid of each group
+-----+-----+
| sid | bid |
+-----+-----+
|  22 | 101 |
|  31 | 102 |
|  64 | 101 |
|  74 | 103 |
+-----+-----+
4 rows in set (0.00 sec)

http://stackoverflow.com/questions/16327954/sql-using-group-by-and-having-clause
*/























