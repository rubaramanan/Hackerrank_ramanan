--Select distinct city
--from station
--where left(city, 1) in ('a', 'e', 'i', 'o', 'u')
--and right(city, 1) in ('a', 'e', 'i', 'o', 'u');

Select distinct city
from station
--mysql, oracle, postgres
where regexp_like(city, '^[AEIOUaeiou].*[AEIOUaeiou]$');
--postgres
--WHERE column_name SIMILAR TO '[AEIOUaeiou]%'