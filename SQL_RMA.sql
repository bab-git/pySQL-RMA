/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) *
  FROM [STAGING DE].[DWData].[RMAANTRAG]
  --WHERE 
  --[VERSENDET_AM] >= '2019.01.01'
  --AND ARTIKELNR IS NULL
  --  Group by
--		BESTELLNR
--		, ARTIKELNR
		--, RMAANTRAG_ID
--  Having
		--COUNT (*)>1
ORDER BY BESTELLNR DESC