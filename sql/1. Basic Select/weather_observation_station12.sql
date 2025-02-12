/*
Enter your query here.
*/

select distinct city
from station
where not regexp_like(city, '^[AEIOUaeiou]')
and not regexp_like(city, '[AEIOUaeiou]$')
