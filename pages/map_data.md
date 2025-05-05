---
title: Geographic data
---

# Locations of every establishment

## Filters

```sql emoji_score_dropdown
  select distinct emoji_score from smileys
```

<Dropdown
  name=emoji_score_selection
  data={emoji_score_dropdown}
  value=emoji_score
  multiple=true
  selectAllByDefault=true
  >
  <!-- <DropdownOption value="%" valueLabel="All Ratings"/> -->
</Dropdown>

```sql by_city_dropdown
  select distinct by_city from smileys
```

<Dropdown
  name=by_city_selection
  data={by_city_dropdown}
  value=by_city
  multiple=true
  selectAllByDefault=true
  >
</Dropdown>

```sql map_locations
  select *
  from smileys
  where
    seneste_kontrol is not null
    and geo_longitude is not null
    and geo_longitude != 0
    and geo_latitude is not null
    and geo_latitude != 0
    and emoji_score IN ${inputs.emoji_score_selection.value}
    and by_city IN ${inputs.by_city_selection.value}
```

<PointMap
data={map_locations}
lat=geo_latitude
long=geo_longitude  
pointName=navn1
value=emoji_score
colorPalette={['#40eb34', '#ebe234', '#eb9334', '#eb4034']}
showTooltip=true
tooltipType=click
tooltip={[
{id: 'navn1', showColumnName: false, valueClass: 'text-xl font-semibold'},
{id: 'adresse1', fmt: 'id', showColumnName: false, valueClass: 'text-l font-semibold'},
{id: 'postnr', fmt: 'id', showColumnName: false, valueClass: 'text-l font-semibold'},
{id: 'by_city', fmt: 'id', showColumnName: false, valueClass: 'text-l font-semibold'},
{id: 'emoji_score', title: 'Latest rating', fmt: 'id', showColumnName: true, valueClass: 'text-l font-semibold'},
{id: 'URL', showColumnName: false, contentType: 'link', linkLabel: 'Click to see Smiley Report 📋', valueClass: 'font-bold mt-1'}
]}
height=800
/>

<!-- <DataTable data={map_locations}/> -->

# Number of inspections per post code

```sql n_inspections_per_postnr_group
  SELECT
    postnr_group,
    COUNT(*) AS n_records
  FROM
    smileys
  WHERE emoji_score IN ${inputs.emoji_score_selection.value}
  and by_city IN ${inputs.by_city_selection.value}
  -- WHERE
  --   postnr IN ('2800', '7400', '2860', '2300')
  GROUP BY 1
  ORDER BY 2 DESC
```

<AreaMap 
    data={n_inspections_per_postnr_group} 
    areaCol=postnr_group
    geoJsonUrl='postal_codes_dk_full_dissolved.geojson'
    geoId=postal_code
    value=n_records
    height=800
/>
