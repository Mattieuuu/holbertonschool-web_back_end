-- Old school band: list bands with Glam rock as main style by longevity up to 2024
-- Compute lifespan using formed and split; treat NULL or 0 split as still active in 2024
SELECT band_name, IFNULL(NULLIF(split, 0), 2024) - formed AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC, band_name;
