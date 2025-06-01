-- with p_values as(
--     select distinct(p)
--     from bst
-- ),

select n,
    case
        when p is null then 'Root'
        when n in (select distinct(p)
    from bst) then 'Inner'
        else 'Leaf'
    end as stat
from bst
order by n;