/*
Enter your query here.
*/

--method 1
--select distinct city
--from station
--where city like '%a'
--or city like '%e'
--or city like '%i'
--or city like '%o'
--or city like '%u';

--method2

select distinct city
from station
where right(city, 1) in ('a', 'i', 'e', 'o', 'u')