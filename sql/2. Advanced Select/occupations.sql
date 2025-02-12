WITH doctor AS (
    SELECT name, ROW_NUMBER() OVER () AS rn
    FROM occupations
    WHERE occupation = 'Doctor'
    order by name
),
professor AS (
    SELECT name, ROW_NUMBER() OVER () AS rn
    FROM occupations
    WHERE occupation = 'Professor'
    order by name
),
singer AS (
    SELECT name, ROW_NUMBER() OVER () AS rn
    FROM occupations
    WHERE occupation = 'Singer'
    order by name
),
actor AS (
    SELECT name, ROW_NUMBER() OVER () AS rn
    FROM occupations
    WHERE occupation = 'Actor'
    order by name
)
SELECT d.name AS Doctor, p.name AS Professor, s.name AS Singer, a.name AS Actor
FROM doctor d
LEFT JOIN professor p ON d.rn = p.rn
LEFT JOIN singer s ON d.rn = s.rn
LEFT JOIN actor a ON d.rn = a.rn

union

SELECT d.name AS Doctor, p.name AS Professor, s.name AS Singer, a.name AS Actor
FROM professor p
LEFT JOIN doctor d ON d.rn = p.rn
LEFT JOIN singer s ON p.rn = s.rn
LEFT JOIN actor a ON p.rn = a.rn

union

SELECT d.name AS Doctor, p.name AS Professor, s.name AS Singer, a.name AS Actor
FROM singer s
LEFT JOIN doctor d ON d.rn = s.rn
LEFT JOIN professor p ON p.rn = s.rn
LEFT JOIN actor a ON s.rn = a.rn

union

SELECT d.name AS Doctor, p.name AS Professor, s.name AS Singer, a.name AS Actor
FROM actor a
LEFT JOIN doctor d ON d.rn = a.rn
LEFT JOIN singer s ON a.rn = s.rn
LEFT JOIN professor p ON p.rn = a.rn

