-- List all bands with Glam rock as their main style, ranked by longevity up to 2024
SELECT band_name, (IFNULL(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
 