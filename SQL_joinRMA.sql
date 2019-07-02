select 
	--rm.rmaantrag_id
	  rm.artikelnr
	, rm.partner_id
	, rm.VERSENDET_AM 
	, rm.LIEFERANT_ID
	, COUNT (rm.RMAANTRAG_ID) As Menge
	, la.HERSTELLER	
	, bp.preis
	, ar.ARTIKEL_ID
	, ar.HERSTELLER_ID	
	, ar.BEZEICHNUNG as artikel
	, pt.SUCHNAME as PARTNER
--, bp.menge
from [STAGING DE].[DWData].[RMAANTRAG] AS rm
join [STAGING DE].[DWData].bestellung AS b on b.nummer = rm.bestellnr
join [STAGING DE].[DWData].bestellposition AS bp on bp.bestellung_id = b.bestellung_id
join [STAGING DE].[DWData].lieferantenartikel AS la on la.lieferantenartikel_id = bp.lieferantenartikel_id and la.artikelnr = rm.artikelnr
join [STAGING DE].[DWData].ARTIKEL AS ar on ar.ARTIKEL_ID = la.ARTIKEL_ID
join [STAGING DE].DWData.[PARTNER] AS pt on rm.PARTNER_ID = pt.PARTNER_ID
where 
--rm.rmaantrag_id = 8449
rm.VERSENDET_AM >= '2019.01.01'
--AND HERSTELLER_ID in ('585','20811')
--AND ARTIKELNR IS NULL
rm.PARTNER_ID = 31982
group by 
	  rm.artikelnr
	, rm.partner_id
	, rm.VERSENDET_AM 
	, bp.preis
	, rm.LIEFERANT_ID
	, la.HERSTELLER	
	, ar.HERSTELLER_ID
	, pt.SUCHNAME
	, ar.BEZEICHNUNG
	, ar.ARTIKEL_ID
--ORDER BY rm.VERSENDET_AM --DESC
ORDER BY HERSTELLER_ID --DESC