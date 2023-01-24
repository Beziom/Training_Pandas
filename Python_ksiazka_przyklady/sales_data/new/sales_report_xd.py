from pathlib import Path
import pandas as pd
this_dir = Path(__file__).resolve().parent
parts = []

for path in (this_dir/"sales_data").rglob("*.xls*"):
    print(f"Reading {path.name}")
    part = pd.read_excel(path,index_col="id_transakcji")
    parts.append(part)
    
df= pd.concat(parts)
df
