--SELECT TOP(1000) *
SELECT COUNT (*)
--FROM SYS.sysobjects
FROM INFORMATION_SCHEMA.TABLES
WHERE 
TABLE_CATALOG = 'STAGING DE'
--xtype = 'U'
AND 
--name = 'ARTIKELUMSATZ'
TABLE_SCHEMA = 'DWData'
