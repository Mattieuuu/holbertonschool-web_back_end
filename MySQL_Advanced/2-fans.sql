-- Rank band origins by total number of fans
-- Aggregate fans by country and sort from most to least fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
