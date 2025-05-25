import logging
from datetime import datetime

import duckdb
import pandas as pd
import requests
from bs4 import BeautifulSoup
from colorlog import ColoredFormatter


def setup_logging():
    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler, logging.FileHandler("download.log")],
    )


def download_smiley_excel() -> str:
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
            logging.info(f"Found Excel file URL: {excel_url}")
            excel_response = requests.get(excel_url)
            if excel_response.status_code == 200:
                file_name = f"smiley_{datetime.now().strftime('%Y%m%d')}.xlsx"
                with open(file_name, "wb") as file:
                    file.write(excel_response.content)
                logging.info(f"Excel file downloaded as '{file_name}'")
                return file_name
            else:
                logging.error(
                    f"Failed to download Excel file: {excel_response.status_code}"
                )
        else:
            logging.error("Excel link not found.")
    else:
        logging.error(f"Failed to fetch page: {response.status_code}")
    return None


def excel_to_duckdb(
    excel_file: str, db_path: str = "sources/smiley_data/smiley_data.duckdb"
):
    df = pd.read_excel(excel_file)
    con = duckdb.connect(database=db_path)
    con.register("smiley_df", df)
    try:
        con.execute("CREATE OR REPLACE TABLE smiley_ratings AS SELECT * FROM smiley_df")
        logging.info("Table created successfully.")
    except Exception as e:
        logging.error(f"Error creating table: {e}")
    logging.info(con.execute("SHOW TABLES").fetchdf())
    con.close()


if __name__ == "__main__":
    setup_logging()
    file_name = download_smiley_excel()
    if file_name:
        excel_to_duckdb(file_name)
