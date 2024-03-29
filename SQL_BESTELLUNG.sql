/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) 
	   bes.[BESTELLUNG_ID]
      ,bes.[LIEFERANT_ID]
      ,bes.[PARTNER_ID]
      ,bes.[DATUM]
      ,bes.[NUMMER]
	  , au.MENGE
  FROM [STAGING DE].[DWData].[BESTELLUNG] as bes 
  join [STAGING DE].[DWData].[ARTIKELUMSATZ] as au on au.DATUM = bes.DATUM and au.PARTNER_ID = bes.PARTNER_ID

  -- WHERE NUMMER = '0003407086'
  where au.DATUM = '2019-06-15'
  and au.MENGE > 1
  --and PARTNER_ID = '31484'
  --and PARTNER_ID = '31818'
  order by PARTNER_ID