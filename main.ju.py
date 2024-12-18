# %% [md]

# Import `pandas` and read the training data.

# %%
import pandas as pd

input_path = "./input/train.csv"
home_data = pd.read_csv(input_path)

# %% [md]

# Print the list of columns in the training data.
# This allows us to find the necessary target.

# %%
home_data.columns

# %% [md]

# It it a standard to use `y` as the prediction target.

# %%
y = home_data.SalePrice

# %% [md]

# After finding the prediction target, we now specify the `X`
# which is called `predictive features`

# %%
feature_names = [
    "LotArea",
    "YearBuilt",
    "1stFlrSF",
    "2ndFlrSF",
    "FullBath",
    "BedroomAbvGr",
    "TotRmsAbvGrd",
]
X = home_data[feature_names]

# %% [md]

# Review the data

# %%
X.describe()

# %%
X.head()

# %% [md]

# Specify and fit the model

# %%
from sklearn.tree import DecisionTreeRegressor

home_model = DecisionTreeRegressor(random_state=1)

home_model.fit(X, y)

# %% [md]

# Make predictions

# %%
predictions = home_model.predict(X)
predictions

# %% [md]

# To further visualize data, print a few columns in `y` and
# compare the following outputs.

# %%
y.head()

# %%
home_model.predict(X.head())
