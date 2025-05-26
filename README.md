<h1 align="center"><img src="static/smileys-logo.png" alt="tipscout logo" width=300></h1>
<h2 align="center"> 😊 Danish Smiley Ratings </h2>
<p align="center"> Visualizing food safety ratings in Denmark.</p>
<p align="center"><a href="https://github.com/kiliantscherny/smiley-ratings/actions/workflows/deploy.yml"><img src="https://github.com/kiliantscherny/smiley-ratings/actions/workflows/deploy.yml/badge.svg" alt="Deployment status"></a>
<a href="https://img.shields.io/badge/Duckdb-000000?style=for-the-badge&logo=Duckdb&logoColor=yellow"><img src="https://img.shields.io/badge/Duckdb-000000?style=for-the-badge&logo=Duckdb&logoColor=yellow" alt="pre-commit" style="max-width:100%;"></a>
<a href="https://img.shields.io/github/stars/kiliantscherny/smiley-ratings"><img src="https://img.shields.io/github/stars/kiliantscherny/smiley-ratings" alt="GitHub stars"></a></p>

## ℹ️ About this project
### Smileys: what they're all about
This project's purpose is to retrieve the food safety ratings of every food retail business in Denmark 🇩🇰. Denmark uses a system called the "Smiley system" to rate food retail businesses on their compliance with food safety laws.

The system is easy to understand: a smiley (🙂) is what you want. Businesses which don't fully comply with the regulations will be given a 😐, a ☹️ or even a 😡, with additional repercussions like fines or being forced to close. This system is designed to protect consumers from harm and ensure a high standard of food safety nationwide.

### The Smiley data
The full data of the results of inspections is [publicly available](https://www.findsmiley.dk/Statistik/Smiley_data/Sider/default.aspx) from the Danish government in XML or Excel format – in this project I am using the `.xlsx` file.

The data contains, among other things, the top-level result of the inspection (as well as the second-, third- and fourth-last inspections) as well as a link to a web page with all of the historical reports for the business. The data is updated at least daily, with new inspection reports being appended to the existing results.

I have created this project in order to:
1. Provide some interesting insights into Smiley ratings throughout Denmark
2. Show how you can build fully-fledged data project with a few simple (and entirely free) tools like Evidence and DuckDB

## ✳️ Getting started

Head straight to the **[static website](https://kiliantscherny.github.io/smiley-ratings/)** to read more about Fødevarestyrelsen's ([The Danish Veterinary and Food Administration](https://www.findsmiley.dk/English/Pages/FrontPage.aspx)) "Smiley" ratings scheme for retail food businesses.

>[!NOTE]
>As this is a static website with a lot of queries and elements, it might take a few seconds for the web page to render with all the visualizations.

Here you can learn about the context of the data, read some key takeaways and explore a map of Denmark with all[^1] the retail food establishments and their ratings.

## ⚙️ Tech stack

This project is built using:
- [Evidence](https://evidence.dev/): BI tool for visualization
- [DuckDB](https://duckdb.org/): in-memory analytical database
- [GitHub Actions](https://github.com/features/actions): orchestrator, deployment

## ⤵️ Data source

The data is freely available from [Fødevarestyrelsen's website](https://www.findsmiley.dk/Statistik/Smiley_data/Sider/default.aspx).

The report is refreshed once per day at 09:00 UTC with the latest data from the source.

## 👐 See also

If you enjoyed exploring this project, check out Anders Bruun Nørring's https://smileydata.dk/, which also does a great job of providing insights into this data.


[^1]: One of the limitations of the dataset is that only a portion of the rows are geocoded (i.e. they have geographic coordinates for the address supplied). Cleaning the data to geocode the missing coordinates is possible with tools like [geopy](https://github.com/geopy/geopy), but this can take a while with the rate limits of the API as a free user
