DROP VIEW IF EXISTS public.geo_parkeervakken;

DROP VIEW IF EXISTS bv.geo_parkeervakken;

DROP VIEW IF EXISTS bv.geo_parkeervakken_reserveringen;

SELECT UpdateGeometrySRID('bv', 'parkeervakken', 'geom', 0);
