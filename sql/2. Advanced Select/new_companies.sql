SELECT 
    e.company_code,
    c.founder,
    e.lm,
    e.sm,
    e.m,
    e.ec
FROM (
    SELECT 
        company_code,
        COUNT(DISTINCT lead_manager_code) AS lm,
        COUNT(DISTINCT senior_manager_code) AS sm,
        COUNT(DISTINCT manager_code) AS m,
        COUNT(DISTINCT employee_code) AS ec
    FROM employee
    GROUP BY company_code
) e
JOIN company c 
ON e.company_code = c.company_code
ORDER BY e.company_code;
