# %%
import pandas as p

input_path = "./input/melb_data.csv"

# %%
csv_data = p.read_csv(input_path)
csv_data.describe()  # Display the read values

# %%
round(csv_data.loc[:, "Price"].mean())

# %%
import datetime

year_today = datetime.date.today().year

year_built: p.DataFrame = csv_data.loc[:, "YearBuilt"]
int(year_today - year_built.max())
