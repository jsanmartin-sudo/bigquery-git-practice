import warnings
warnings.filterwarnings("ignore")

from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()

query = """
SELECT * FROM `cl-cda-unidata-prod.DS_PROD_UNI_SSFF.VW_APERTURAS_UNIDATA` LIMIT 10
"""

df = client.query(query).to_dataframe()

print(df.head())