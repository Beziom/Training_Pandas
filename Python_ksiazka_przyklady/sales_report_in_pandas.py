from pathlib import Path
import pandas as pd

# Path(__file__)
# resolve().parent
# this_dir/filename
# rglob()

"Checking actual directory"
this_dir = Path(__file__).resolve().parent
parts = []

"Reading all files with .xlsx extension"
for path in (this_dir/"sales_data").rglob("*.xlsx*"):
    print(f"Reading {path.name}")
    part = pd.read_excel(path, index_col="id_transakcji",date_parser="data_transakcji")
    parts.append(part)
    
df = pd.concat(parts)
pivot = pd.pivot_table(df,index="data_transakcji", columns="sklep",values="kwota",aggfunc="sum")
pivot.info()
summary = pivot.resample("M").sum()
summary.index.name= "Miesiąc"

summary.to_excel(this_dir/"sales_report_in_pandas.xlsx")