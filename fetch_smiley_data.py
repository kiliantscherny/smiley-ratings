from datetime import datetime

import duckdb
import pandas as pd
import requests
from bs4 import BeautifulSoup
from loguru import logger


def download_smiley_excel() -> str:
    logger.debug("Checking website for Excel file link...")
    page_url = "https://www.findsmiley.dk/Statistik/Smiley_data/Sider/default.aspx"
    response = requests.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        link = soup.find(
            "a",
            class_="external-url",
            string=lambda text: "Smiley-data som Excel" in text if text else False,
        )

        if link and link["href"]:
            excel_url = link["href"]
            logger.success(f"Found Excel file URL: {excel_url}")
            excel_response = requests.get(excel_url)
            if excel_response.status_code == 200:
                file_name = f"smiley_{datetime.now().strftime('%Y%m%d')}.xlsx"
                with open(file_name, "wb") as file:
                    file.write(excel_response.content)
                logger.info(f"Excel file downloaded as '{file_name}'")
                return file_name
            else:
                logger.error(
                    f"Failed to download Excel file: {excel_response.status_code}"
                )
        else:
            logger.critical("Excel link not found.")
    else:
        logger.critical(f"Failed to fetch page: {response.status_code}")
    return None


def excel_to_duckdb(
    excel_file: str, db_path: str = "sources/smiley_data/smiley_data.duckdb"
) -> None:
    logger.debug("Converting Excel to Pandas dataframe...")
    df = pd.read_excel(excel_file)
    logger.debug("Creating DuckDB table from dataframe...")
    con = duckdb.connect(database=db_path)
    con.register("smiley_df", df)
    try:
        con.execute("CREATE OR REPLACE TABLE smiley_ratings AS SELECT * FROM smiley_df")
        logger.success("Table created successfully.")
        logger.info("Tables in database:")
        logger.info(con.execute("SHOW TABLES").fetchdf())
    except Exception as e:
        logger.critical(f"Error creating table: {e}")
    con.close()


if __name__ == "__main__":
    file_name = download_smiley_excel()
    if file_name:
        excel_to_duckdb(file_name)
