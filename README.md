<h1 align="center"><img src="static/smileys-logo.png" alt="tipscout logo" width=300></h1>
<h2 align="center"> Danish Smiley Ratings </h2>
<p align="center"> Visualizing food safety ratings in Denmark.</p>
<p align="center"><a href="https://github.com/kiliantscherny/smiley-ratings/actions/workflows/deploy.yml"><img src="https://github.com/kiliantscherny/smiley-ratings/actions/workflows/deploy.yml/badge.svg" alt="See it on Streamlit now"></a></p>

## ✳️ Using this project

Head straight to the **[static website](https://kiliantscherny.github.io/smiley-ratings/)** to read all about Fødevarestyrelsen's "Smiley" ratings scheme for retail food businesses.

Here you can learn about the context of the data, read some key takeaways and explore a map of Denmark with all[^1] the retail food establishments and their ratings.

## ⚙️ Tech stack

This project is built using:
- [Evidence](https://evidence.dev/): BI tool for visualization
- [DuckDB](https://duckdb.org/): in-memory analytical database
- [GitHub Actions](https://github.com/features/actions): orchestrator, deployment

## ⤵️ Data source

The data is freely available from [Fødevarestyrelsen's website](https://www.findsmiley.dk/Statistik/Smiley_data/Sider/default.aspx).

[^1]: One of the limitations of the dataset is that only a portion of the rows are geocoded (i.e. they have geographic coordinates for the address supplied). Cleaning the data to geocode the missing coordinates is possible with tools like [geopy](https://github.com/geopy/geopy), but this can take a while with the rate limits of the API as a free user
