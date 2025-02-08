/*
Enter your query here.
*/

--select distinct city
--from station
--where city like 'A%'
--or city like 'E%'
--or city like 'I%'
--or city like 'O%'
--or city like 'U%'
--or city like 'a%'
--or city like 'e%'
--or city like 'i%'
--or city like 'o%'
--or city like 'u%';


select distinct city
from station
where left(city, 1) in ('a', 'i', 'e', 'o', 'u', 'A', 'E', 'I', 'O', 'U')