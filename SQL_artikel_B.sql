/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [ARTIKEL_ID]
      ,[ARTIKELNR]
      ,[BEZEICHNUNG]
      ,[CREATED]
      ,[LAST_UPDATE]
      ,[EAN_CODE]
      ,[HERSTELLER_ID]
      ,[HERSTELLERARTIKELNR]
      ,[INAKTIV]
      ,[WARENGRUPPE_ID]
      ,[TOP_WG]
      ,[CONTENT_EXISTS]
  FROM [STAGING DE].[DWData].[ARTIKEL]
  where HERSTELLER_ID in ('585','20811')
  order by ARTIKEL_ID