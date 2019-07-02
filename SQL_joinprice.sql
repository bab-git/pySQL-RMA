select TOP (1000)
	--rm.rmaantrag_id	  	
	--, rm.VERSENDET_AM 
	au.DATUM	
	, au.ARTIKEL_ID
	, au.HERSTELLER_ID
	, au.LIEFERANT_ID
	, au.PARTNER_ID	
	--, SUM (au.UMSATZNETTO) as UMSATZPreis
	, au.UMSATZNETTO
from [STAGING DE].[DWData].[RMAANTRAG] AS rm
join [STAGING DE].[DWData].bestellung AS b on b.nummer = rm.bestellnr
join [STAGING DE].[DWData].bestellposition AS bp on bp.bestellung_id = b.bestellung_id
join [STAGING DE].[DWData].lieferantenartikel AS la on la.lieferantenartikel_id = bp.lieferantenartikel_id and la.artikelnr = rm.artikelnr
join [STAGING DE].[DWData].ARTIKELUMSATZ AS au on au.ARTIKEL_ID = la.ARTIKEL_ID
--join [STAGING DE].DWData.[PARTNER] AS pt on rm.PARTNER_ID = pt.PARTNER_ID
where 
--rm.rmaantrag_id = 8449
au.DATUM	= '2019.01.02'
and au.PARTNER_ID = 5518
--AND HERSTELLER_ID in ('585','20811')
--AND ARTIKELNR IS NULL
/*group by 
	  au.DATUM	
	, au.ARTIKEL_ID
	, au.HERSTELLER_ID	
	, au.PARTNER_ID	
	, au.LIEFERANT_ID
*/
ORDER BY au.PARTNER_ID --DESC
--ORDER BY HERSTELLER_ID --DESC