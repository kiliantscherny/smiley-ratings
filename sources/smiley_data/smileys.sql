select
    CAST(navnelbnr AS STRING) AS navne_loebenummer,
    CAST(cvrnr AS STRING) AS cvr_nummer,
    CAST(pnr AS STRING) AS produktionsenhedsnummer,
    CAST(brancheKode AS STRING) AS branchekode,
    CAST(branche AS STRING) AS branche,
    CAST(virksomhedstype AS STRING) AS virksomhedstype,
    CAST(navn1 AS STRING) AS navn1,
    CAST(adresse1 AS STRING) AS adresse1,
    CAST(postnr AS STRING) AS postnr,
    CAST(By AS STRING) AS by,
    CAST(seneste_kontrol AS INTEGER) AS seneste_kontrol,
    CAST(seneste_kontrol_dato AS DATE) AS seneste_kontrol_dato,
    CAST(naestseneste_kontrol AS INTEGER) AS naestseneste_kontrol,
    CAST(naestseneste_kontrol_dato AS DATE) AS naestseneste_kontrol_dato,
    CAST(tredjeseneste_kontrol AS INTEGER) AS tredjeseneste_kontrol,
    CAST(tredjeseneste_kontrol_dato AS DATE) AS tredjeseneste_kontrol_dato,
    CAST(fjerdeseneste_kontrol AS INTEGER) AS fjerdeseneste_kontrol,
    CAST(fjerdeseneste_kontrol_dato AS DATE) AS fjerdeseneste_kontrol_dato,
    CAST(URL AS STRING) AS URL,
    CAST(reklame_beskyttelse AS INTEGER) AS reklame_beskyttelse,
    CAST(Elite_Smiley AS INTEGER) AS Elite_Smiley,
    CAST(Geo_Lng AS STRING) AS geo_longitude,
    CAST(Geo_Lat AS STRING) AS geo_latitude,
    CASE
        WHEN seneste_kontrol = 1 THEN '1: 😊'
        WHEN seneste_kontrol = 2 THEN '2: 😐'
        WHEN seneste_kontrol = 3 THEN '3: ☹️'
        WHEN seneste_kontrol = 4 THEN '4: 😡'
    END AS emoji_score,
    CASE
        WHEN naestseneste_kontrol = 1 THEN '1: 😊'
        WHEN naestseneste_kontrol = 2 THEN '2: 😐'
        WHEN naestseneste_kontrol = 3 THEN '3: ☹️'
        WHEN naestseneste_kontrol = 4 THEN '4: 😡'
    END AS previous_emoji_score,
    CASE
        WHEN postnr BETWEEN 0 AND 999 THEN 'Other'
        WHEN postnr BETWEEN 1000 AND 2999 THEN 'Copenhagen'
        WHEN postnr BETWEEN 3000 AND 3699 THEN 'North Zealand'
        WHEN postnr BETWEEN 3700 AND 3799 THEN 'Bornholm'
        WHEN postnr BETWEEN 4000 AND 4999 THEN 'Zealand, Lolland-Falster & Møn'
        WHEN postnr BETWEEN 5000 AND 5999 THEN 'Funen'
        WHEN postnr BETWEEN 6000 AND 9999 THEN 'Jutland'
        ELSE 'Unknown'
    END AS region
from
    smiley_ratings
where seneste_kontrol > 0