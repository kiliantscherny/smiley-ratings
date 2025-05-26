## Explore the whole dataset

```sql all_smiley_data
  select * from smileys
```

<DataTable data={all_smiley_data} title="Selected locations" subtitle="Note: this includes all businesess — even those without geolocation coordinates." wrapTitles=true rowShading=true search=true rows=25 >
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