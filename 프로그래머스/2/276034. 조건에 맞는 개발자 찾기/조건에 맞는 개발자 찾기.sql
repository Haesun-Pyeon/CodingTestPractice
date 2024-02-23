select ID, EMAIL, FIRST_NAME, LAST_NAME
from developers
where (substr(bin(skill_code >> (select length(bin(code))-1 from skillcodes where name like 'Python')), -1, 1) or substr(bin(skill_code >> (select length(bin(code))-1 from skillcodes where name like 'C#')), -1, 1)) like 1
ORDER BY ID