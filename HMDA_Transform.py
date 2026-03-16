import pandas as pd

cols_needed_detail = [
    "lei",
    "action_taken",
    "activity_year",
    "census_tract",
    "loan_amount",
    "loan_to_value_ratio",
    "interest_rate",
    "property_value",
    "income",
    "debt_to_income_ratio",
    "applicant_age",
]
df_1 = pd.read_csv(
    "state_TX.csv",
    usecols=cols_needed_detail,
    low_memory=False,
)
df_2 = pd.read_csv(
    "state_TX-2.csv",
    usecols=cols_needed_detail,
    low_memory=False,
)
df_3 = pd.read_csv(
    "state_TX-3.csv",
    usecols=cols_needed_detail,
    low_memory=False,
)
df_4 = pd.read_csv(
    "state_TX-4.csv",
    usecols=cols_needed_detail,
    low_memory=False,
)
df_5 = pd.read_csv(
    "state_TX-5.csv",
    usecols=cols_needed_detail,
    low_memory=False,
)

df = pd.concat([df_1, df_2, df_3, df_4, df_5], ignore_index=True)

# To change census_tract datatype
df["census_tract"] = df["census_tract"].astype("Int64")

# To change property_value datatype
df["property_value"] = pd.to_numeric(df["property_value"], errors="coerce").astype(
    "Int64"
)

# To change loan_to_value_ratio datatype
df["loan_to_value_ratio"] = pd.to_numeric(df["loan_to_value_ratio"], errors="coerce").astype("Float64")

# To change interest_rate datatype
df["interest_rate"] = pd.to_numeric(df["interest_rate"], errors="coerce").astype("Float64")

# To change debt_to_income_ratio datatype
df["debt_to_income_ratio"] = pd.to_numeric(df["debt_to_income_ratio"], errors="coerce").astype("Float64")

# To change applicant_age datatype
df["applicant_age"] = pd.to_numeric(df["applicant_age"], errors="coerce").astype("Int64")

df.info()

df.to_parquet("HMDA_5yr_clean.parquet", index=False)
