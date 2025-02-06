/*
Enter your query here.
*/
/*
Enter your query here.
*/
with required as(
    select
        city,
        length(city) as city_length
    from station
),
    ranked as(
    select *,
        row_number() over (order by city_length asc, city asc) as first_alp,
        row_number() over (order by city_length desc, city desc) as last_alp
    from required
)

select
    city,
    city_length
from ranked
where first_alp=1 or last_alp=1;

