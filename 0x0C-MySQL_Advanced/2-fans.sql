-- 2. Best band ever!
-- SQL script that ranks country origins of bands, ordered by the number of fan
SELECT origin, sum(fans) as nb_fans
    FROM metal_bands
    GROUP by origin
    ORDER BY nb_fans DESC;