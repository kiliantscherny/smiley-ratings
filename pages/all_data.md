---
title: Smiley ratings full data
full_width: true
---

## Explore the whole dataset

```sql all_smiley_data
  select * from smileys
  where smiley_score IN ${inputs.smiley_score_selection.value}
    and by_city IN ${inputs.city_selection.value}
    and region IN ${inputs.region_selection.value}
    and score_change IN ${inputs.score_change_selection.value}
```

## Filters

```sql smiley_score_dropdown
    select distinct smiley_score from smileys
```

```sql by_city_dropdown
    select distinct by_city from smileys
```

```sql region_dropdown
    select distinct region from smileys
```

```sql score_change_dropdown
    select distinct score_change from smileys
```

<Grid cols=2>
<Dropdown
    name=smiley_score_selection
    data={smiley_score_dropdown}
    value=smiley_score
    multiple=true
    selectAllByDefault=true
    >
</Dropdown>

<Dropdown
    name=city_selection
    data={by_city_dropdown}
    value=by_city
    multiple=true
    selectAllByDefault=true
    >
</Dropdown>

<Dropdown
    name=region_selection
    data={region_dropdown}
    value=region
    multiple=true
    selectAllByDefault=true
    >
</Dropdown>

<Dropdown
    name=score_change_selection
    data={score_change_dropdown}
    value=score_change
    multiple=true
    selectAllByDefault=true
    >
</Dropdown>
</Grid>

<DataTable data={all_smiley_data} title="Selected locations" subtitle="Note: this includes all businesess — even those without geolocation coordinates." wrapTitles=true rowShading=true search=true rows=10 >
	<Column id=navn1 title="Establishment name" />
	<Column id=adresse1 title="Address" />
	<Column id=postnr title="Post Code" />
	<Column id=by_city title="Town/City" />
	<Column id=smiley_score />
	<Column id=previous_smiley_score />
	<Column id=seneste_kontrol_dato title="Last inspection date" fmt="fulldate" />
    <Column id=score_delta contentType=delta fmt=num0 title="Change" downIsGood=true chip=true/>
    <Column id=URL contentType=link title="Report link" linkLabel="View Smiley report →"/>
</DataTable>