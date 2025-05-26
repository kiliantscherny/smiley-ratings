---
title: Danish Smiley Ratings
---

<LastRefreshed/>

**A standard for food and beverage safety for businesses in Denmark**

<Accordion class="text-black py-2 px-6 rounded-md bg-green-100">

<AccordionItem title="💡 Curious about what the data below is about? Open me to find out all about the Smiley system">

# About the "Smiley" system

<Grid cols=2 gapSize=md>

  <Group>

      <Details title="What is the Smiley system?" open=true>

      The Smiley system is a **food safety inspection system** in Denmark. It is designed to help consumers make informed choices about the food establishments they visit. The system uses a smiley face rating to indicate the level of compliance with food safety regulations (you can see them and what they mean on the right).
      
      </Details>

      <Details title="How does it work?" open=true>

      The smiley is determined by the **worst result.** <Info description="If the establishment scores a 1 in most categories but a 4 in one, the final score would be 4." color="primary" />

      At each inspection a number of areas are checked, and assigned a result (1 - 4). All results and remarks of the inspector are published on the inspection report. The smiley for the inspection is determined by the worst of the results.

      Establishments not complying with regulations will get follow-up inspections, paid by the establishment.

      </Details>

      <Details title="How is it used?" open=true>

      Taken from [The Danish Veterinary and Food Administration website](https://www.findsmiley.dk/English/Pages/FrontPage.aspx):

      > "In October 2023, the new smiley label was implemented. The smiley label, showing the three latest inspection results, must be displayed for consumers to read, before they decide to enter a shop or a restaurant for example. The smiley scheme was implemented in 2001. The three different smileys signal how well a food establishment complies with food regulations."

      > "The Smiley scheme shows how well shops, restaurants and other businesses that sell food to consumers comply with the legal requirements for handling food. The scheme therefore makes it easy for consumers to find companies that have food safety under control. At the same time, the smiley scheme makes it easy for companies to show how well they are complying with the rules."
      
      </Details>

  </Group>
  <Group>

      ## The Smiley data

      The data about food inspections is publicly available from the Administration's website [here](https://www.findsmiley.dk/Statistik/Smiley_data/Sider/default.aspx) as an Excel (`.xlsx`) file.

      ## The Smileys

      <Tabs fullWidth=false>
          <Tab label="Smiley with happy mouth">
            <Image 
                url="https://foedevarestyrelsen.dk/Media/638210466368269699/kontrolsmiley%20glad%20mund.jpg"
                description="Smiley with happy mouth: No comments"
                height=200
            />
            <strong>Smiley with happy mouth</strong>
            <br>
            Companies which receive a report rating of 1 receive this score. This indicates no remarks from the inspector.
          </Tab>
          <Tab label="Smiley with a straight mouth">
            <Image 
                url="https://foedevarestyrelsen.dk/Media/638210466368996486/kontrolsmiley%20lige%20mund.jpg"
                description="Smiley with a straight mouth: Warning, injunction, ban or daily fines"
                height=200
            />
            <strong>Smiley with a straight mouth</strong>
            <br>
            Companies which receive a report rating of 2 or 3 receive this score. These may receive reprimands, injunctions, prohibitions or fines.
          </Tab>
          <Tab label="Smiley with a sour mouth">
            <Image 
                url="https://foedevarestyrelsen.dk/Media/638210466370402874/kontrolsmiley%20sur%20mund.jpg"
                description="Smiley with a sour mouth; Fine, police report, quarantine, authorization or registration revoked"
                height=200
            />
            <strong>Smiley with a sour mouth</strong>
            <br>
            Companies which receive a report rating of 4 receive this score. These may receive a fix notice, police report, company quarantine, authorization or have their registration revoked.
          </Tab>
      </Tabs>
    <Group>

      ## Example of a Smiley report

      <Embed url="https://drive.google.com/file/d/1oHE3hQBmPA_K7S6N71VzIafgyNOW7uma/preview"/>

    </Group>
  </Group>
</Grid>

</AccordionItem>
</Accordion>


# Key stats on Smileys in Denmark

```sql smileys_with_rating
  select count(*) as n_businesses from smileys
```

```sql count_by_rating
  select
    seneste_kontrol,
    CAST(seneste_kontrol AS STRING) AS seneste_kontrol_string,
    emoji_score,
    count(*) AS n_establishments
  from smileys
  where seneste_kontrol is not null
  group by 1, 2, 3
  order by 1 asc
```

```sql count_by_region
  select
    region,
    emoji_score,
    count(*) AS n_establishments
  from smileys
  where seneste_kontrol is not null
  group by 1, 2
  order by 2 ASC, 3 DESC
```

```sql count_by_day
  select
    seneste_kontrol_dato,
    count(*) AS n_inspections
  from smileys
  where seneste_kontrol is not null
    and seneste_kontrol_dato >= CURRENT_DATE - INTERVAL 12 MONTH
  group by 1
  order by 1 desc
```

```sql max_date
select max(seneste_kontrol_dato) as latest_inspection_date from smileys
```

```sql count_by_virksomhedstype
  select
    virksomhedstype,
    count(*) AS n_inspections
  from smileys
  where seneste_kontrol is not null
  group by 1
```

```sql sankey_source
    select
      virksomhedstype as source,
      emoji_score as target,
      count(*) as count
    from smileys
    where emoji_score is not null
      and emoji_score != ''
    group by source, target;
    order by target asc
```

### There are **<Value data={smileys_with_rating} column=n_businesses fmt="num0"/>** businesses in Denmark with Smiley ratings, with the last inspection happening on **<Value data={max_date} column=latest_inspection_date fmt="fulldate"/>**.

<Grid cols=2>
    <BarChart
      data={count_by_rating}
      x=emoji_score
      y=n_establishments
      labels=true
      xAxisLabels=true
      sort=false
      colorPalette={['#098205', '#ebe234', '#eb9334', '#eb4034']}
      xAxisTitle="Rating"
      title="Count of ratings by score given"
      subtitle="How many businesses received each rating in the latest reports?"
    />
    <BarChart
      data={count_by_region}
      series=emoji_score
      x=region
      y=n_establishments
      labels=true
      xAxisLabels=true
      sort=false
      swapXY=true
      colorPalette={['#098205', '#ebe234', '#eb9334', '#eb4034']}
      xAxisTitle="Rating"
      title="Count of ratings by region in Denmark"
      subtitle="How many ratings were given out in each region?"
    />
    <CalendarHeatmap 
    data={count_by_day}
    date=seneste_kontrol_dato
    value=n_inspections
    title="Heatmap of inspections per day"
    subtitle="How many inspections were carried out each day in the last 12 months?"
    colorScale={['#098205', '#73a71c', '#c4cb2b', '#ebe234', '#ebbd34', '#eba034', '#eb8434', '#eb6934', '#eb4f34', '#eb4034']}
    />
    <SankeyDiagram
    data={sankey_source}
    title="Sankey diagram of ratings per company type"
    subtitle="The results per 'virksomhedstype' (company type)"
    sourceCol=source
    targetCol=target
    valueCol=count
    linkColor=gradient
    colorPalette={['#a1a1a1', '#098205', '#292929', '#ebe234', '#eb9334', '#eb4034']}
    />
</Grid>

# Winners and Losers since the previous Smiley rating

Which businesses have got better since their last check and which have got worse? **Note: a lower number is better**

```sql losers
  select
    navn1 AS name,
    by_city AS city,
    emoji_score,
    previous_emoji_score AS previous_score,
    seneste_kontrol_dato AS last_inpsection_date,
    score_delta
  from
    smileys
  where
    score_delta > 0
  order by
    score_delta DESC, last_inpsection_date DESC
  limit 10
```

```sql winners
  select
    navn1 AS name,
    by_city AS city,
    emoji_score,
    previous_emoji_score AS previous_score,
    seneste_kontrol_dato AS last_inpsection_date,
    score_delta
  from
    smileys
  where
    score_delta < 0
  order by
    score_delta ASC, last_inpsection_date DESC
  limit 10
```

<Grid cols=2>
<DataTable data={winners} title="📈 Top 10 winners since previous Smiley check" wrapTitles=true rowShading=true sortable=false>
	<Column id=name wrap=true/>
	<Column id=city wrap=true/>
	<Column id=emoji_score wrap=true/>
	<Column id=previous_score wrap=true/>
	<Column id=last_inpsection_date fmt="longdate" wrap=true/>
  <Column id=score_delta contentType=delta fmt=num0 title="Change" downIsGood=true chip=true wrap=true/>
</DataTable>

<DataTable data={losers} title="📉 Top 10 losers since previous Smiley check" wrapTitles=true rowShading=true sortable=false>
	<Column id=name wrap=true/>
  <Column id=city wrap=true/>
	<Column id=emoji_score wrap=true/>
	<Column id=previous_score wrap=true/>
  <Column id=last_inpsection_date fmt="longdate" wrap=true/>
  <Column id=score_delta contentType=delta fmt=num0 title="Change" downIsGood=true chip=true wrap=true/>
</DataTable>
</Grid>

# Inspection results per week

How many results there were each week for each inspection score in the last 12 months.

```sql inspections_per_day
  select
    DATE_TRUNC('WEEK', seneste_kontrol_dato) AS latest_inpsection_week,
    seneste_kontrol,
    COUNT(*) AS n_results
  from
    smileys
  where
      seneste_kontrol_dato >= CURRENT_DATE - INTERVAL 12 MONTH
  group by
    1, 2
  order by
    1 desc
```

<LineChart 
    data={inspections_per_day}
    x=latest_inpsection_week
    y=n_results 
    yAxisTitle="Number of inspection results"
    series=seneste_kontrol
    handleMissing=zero
    markers=true
    markerShape=emptyCircle
    markerSize=5
    colorPalette={['#098205', '#ebe234', '#eb9334', '#eb4034']}
/>

# Locations of every establishment

Where each establishment is located, based on the latitude and longitude fields provided in the dataset. **Note: these are not verified and _can_ be imprecise or altogether incorrect.**

```sql map_locations
  select
    navn1,
    emoji_score,
    previous_emoji_score,
    score_delta,
    geo_latitude,
    geo_longitude,
    adresse1,
    postnr,
    by_city,
    region,
    URL,
    seneste_kontrol_dato,
    score_change
  from smileys
  where
    geo_longitude is not null
    and geo_longitude != 0
    and geo_latitude is not null
    and geo_latitude != 0
    and emoji_score IN ${inputs.emoji_score_selection.value}
    and by_city IN ${inputs.city_selection.value}
    and region IN ${inputs.region_selection.value}
    and score_change IN ${inputs.score_change_selection.value}
```

```sql count_with_coordinates
  select
    count_if(geo_latitude is not null and geo_longitude is not null and geo_latitude != 0 and geo_longitude != 0) AS n_with_coords,
    count(*) as total_records,
    (count_if(geo_latitude is not null)/count(*)) as pct_with_coords
  from smileys
  where emoji_score IN ${inputs.emoji_score_selection.value}
    and by_city IN ${inputs.city_selection.value}
    and region IN ${inputs.region_selection.value}
    and score_change IN ${inputs.score_change_selection.value}
```

## Filters

```sql emoji_score_dropdown
  select distinct emoji_score from smileys
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

<Grid cols=4>
<Dropdown
  name=emoji_score_selection
  data={emoji_score_dropdown}
  value=emoji_score
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

<Alert status="info">
There are <strong> <Value data={count_with_coordinates} column=n_with_coords fmt="num0"/> </strong> businesses with geolocation data available out of <strong> <Value data={count_with_coordinates} column=total_records fmt="num0"/> </strong> with inspection results (<strong> <Value data={count_with_coordinates} column=pct_with_coords fmt="pct"/> </strong>). Only these are shown below.<Info description="Filling in the geolocation data for the remaining establishments requires geocoding using external services, which is possible, but very time consuming and not guaranteed to yield results each time." color="primary"/>
</Alert>

<PointMap
data={map_locations}
lat=geo_latitude
long=geo_longitude  
pointName=navn1
value=emoji_score
colorPalette={['#098205', '#ebe234', '#eb9334', '#eb4034']}
showTooltip=true
tooltipType=click
tooltip={[
{id: 'navn1', showColumnName: false, valueClass: 'text-xl font-semibold'},
{id: 'adresse1', fmt: 'id', showColumnName: false, valueClass: 'text-l font-semibold'},
{id: 'postnr', fmt: 'id', showColumnName: false, valueClass: 'text-l font-semibold'},
{id: 'by_city', fmt: 'id', showColumnName: false, valueClass: 'text-l font-semibold'},
{id: 'region', fmt: 'id', showColumnName: false, valueClass: 'text-l font-semibold'},
{id: 'seneste_kontrol_dato', title: 'Last inspection date', fmt: 'fulldate', showColumnName: true, valueClass: 'text-l font-semibold'},
{id: 'emoji_score', title: 'Latest rating', fmt: 'id', showColumnName: true, valueClass: 'text-l font-semibold'},
{id: 'score_change', fmt: 'id', title: 'Score change since last inspection', showColumnName: true, valueClass: 'text-l font-semibold'},
{id: 'URL', showColumnName: false, contentType: 'link', linkLabel: 'Click to see Smiley Report 📋', valueClass: 'font-bold mt-1'}
]}
height=800
/>

```sql all_smiley_data
  select * from smileys
```

<DataTable data={all_smiley_data} title="Selected locations" subtitle="Note: this includes all businesess — even those without geolocation coordinates." wrapTitles=true rowShading=true search=true rows=25 sort="seneste_kontrol_dato desc">
	<Column id=navn1 title="Establishment name" />
	<Column id=adresse1 title="Address" />
	<Column id=postnr title="Post Code" />
	<Column id=by_city title="Town/City" />
	<Column id=emoji_score />
	<Column id=previous_emoji_score />
	<Column id=seneste_kontrol_dato title="Last inspection date" fmt="fulldate" />
  <Column id=score_delta contentType=delta fmt=num0 title="Change" downIsGood=true chip=true/>
  <Column id=URL contentType=link linkLabel="View Smiley report →"/>
</DataTable>
