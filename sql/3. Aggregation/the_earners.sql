--select e.earnings, count(*)
--from (select employee_id, (salary*months) as earnings
--from employee) as e
--group by earnings
--having e.earnings=(select max(salary*months) from employee);

SELECT MONTHS*SALARY AS earnings, COUNT(*)
FROM employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;