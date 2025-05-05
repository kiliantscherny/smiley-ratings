---
title: Danish Smiley Ratings
---

**A standard for food and beverage safety for businesses in Denmark**

# What is the "Smiley" system?

Taken from [The Danish Veterinary and Food Administration website](https://www.findsmiley.dk/English/Pages/FrontPage.aspx):

> "In October 2023, the new smiley label was implemented. The smiley label, showing the three latest inspection results, must be displayed for consumers to read, before they decide to enter a shop or a restaurant for example. The smiley scheme was implemented in 2001. The three different smileys signal how well a food establishment complies with food regulations."

> "The Smiley scheme shows how well shops, restaurants and other businesses that sell food to consumers comply with the legal requirements for handling food. The scheme therefore makes it easy for consumers to find companies that have food safety under control. At the same time, the smiley scheme makes it easy for companies to show how well they are complying with the rules."

# The Smiley data

The data about food inspections is publicly available from the Administration's website [here](https://www.findsmiley.dk/Statistik/Smiley_data/Sider/default.aspx) as an Excel (`.xlsx`) file.

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

There are **<Value data={smileys_with_rating} column=n_businesses fmt="num0"/>** businesses in Denmark with Smiley ratings.

<Grid cols=2>
    <BarChart
        data={count_by_rating}
        x=emoji_score
        y=n_establishments
        labels=true
        xAxisLabels=true
        sort=false
      xAxisTitle="Rating"
      yAxisTitle="Number of establishments"
    />
    <BarChart
        data={count_by_region}
        series=emoji_score
        x=region
        y=n_establishments
        labels=true
        xAxisLabels=true
        sort=false
      xAxisTitle="Rating"
      yAxisTitle="Number of establishments"
    />
    <!-- <ECharts config={
        {
            tooltip: {
                formatter: '{b}: {c} ({d}%)'
            },
          series: [
            {
              type: 'pie',
              radius: ['40%', '70%'],
              data: [...donut_data],
            }
          ]
          }
        }
    /> -->
</Grid>

```sql list_smileys_with_rating
  select * from smileys where seneste_kontrol is not null limit 10
```

<DataTable data={smileys_with_rating} />

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
{id: 'by', fmt: 'id', showColumnName: false, valueClass: 'text-l font-semibold'},
{id: 'emoji_score', title: 'Latest rating', fmt: 'id', showColumnName: true, valueClass: 'text-l font-semibold'},
{id: 'URL', showColumnName: false, contentType: 'link', linkLabel: 'Click to see Smiley Report 📋', valueClass: 'font-bold mt-1'}
]}
height=800
/>

<DataTable data={map_locations}/>

# Winners and Losers since the previous Smiley rating

Which businesses have got better since their last check and which have got worse? **Note: a lower number is better!**

```sql losers
  select
    navn1 AS name,
    emoji_score,
    previous_emoji_score,
    cast(seneste_kontrol AS INTEGER) - cast(naestseneste_kontrol AS INTEGER) AS score_delta
  from
    smileys
  where
    score_delta > 0
  order by
    score_delta DESC
```

```sql winners
  select
    navn1 AS name,
    emoji_score,
    previous_emoji_score,
    cast(seneste_kontrol AS INTEGER) - cast(naestseneste_kontrol AS INTEGER) AS score_delta
  from
    smileys
  where
    score_delta < 0
  order by
    score_delta ASC
```

<Grid cols=2>
<DataTable data={winners} title="👍 Biggest winners since previous Smiley check">
	<Column id=name />
	<Column id=emoji_score />
	<Column id=previous_emoji_score />
  <Column id=score_delta contentType=delta fmt=num0 title="Change" downIsGood=true/>
</DataTable>

<DataTable data={losers} title="👎 Biggest losers since previous Smiley check">
	<Column id=name />
	<Column id=emoji_score />
	<Column id=previous_emoji_score />
  <Column id=score_delta contentType=delta fmt=num0 title="Change" downIsGood=true/>
</DataTable>
</Grid>
