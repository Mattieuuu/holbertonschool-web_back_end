-- List Glam rock bands ranked by longevity up to year 2024
-- Compute lifespan from formed year to split year, or 2024 if still active
SELECT band_name, IFNULL(split, 2024) - formed AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
