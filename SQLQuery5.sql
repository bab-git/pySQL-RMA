/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [BESTELLUNG_ID]
      ,[LIEFERANT_ID]
      ,[PARTNER_ID]
      ,[DATUM]
      ,[NUMMER]
  FROM [STAGING DE].[DWData].[BESTELLUNG]
  where DATUM = '2019-06-15'
  and PARTNER_ID = 6453
  --order by PARTNER_ID
