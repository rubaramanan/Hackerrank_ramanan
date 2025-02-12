/*
Enter your query here.
*/

select distinct city
from station
where left(city, 1) not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
or right(city, 1) not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
