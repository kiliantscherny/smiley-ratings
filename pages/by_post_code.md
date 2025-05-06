---
title: Post codes
---

# Number of inspections per post code

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

```sql n_inspections_per_postnr_group
  SELECT
    postnr_group,
    by_city,
    COUNT(*) AS n_records
  FROM
    smileys
  WHERE emoji_score IN ${inputs.emoji_score_selection.value}
  and by_city IN ${inputs.by_city_selection.value}
  GROUP BY 1, 2
  ORDER BY 3 DESC
```

<AreaMap 
    data={n_inspections_per_postnr_group} 
    areaCol=postnr_group
    geoJsonUrl='/postal_codes_dk_full_deduped_simplified_10pct.geojson'
    geoId=postal_code
    value=n_records
    height=800
/>