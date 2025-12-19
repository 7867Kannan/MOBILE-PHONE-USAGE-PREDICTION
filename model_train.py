import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# READ EXCEL FILE
df = pd.read_excel("mobile_usage_dates_3000.csv.xlsx")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Group per day
daily = df.groupby("Date").agg(
    Total_Minutes=("Usage_Minutes", "sum"),
    Social_Min=("Category", lambda x: (x=="Social").sum()*10),
    Study_Min=("Category", lambda x: (x=="Study").sum()*10),
    Entertainment_Min=("Category", lambda x: (x=="Entertainment").sum()*10),
    Gaming_Min=("Category", lambda x: (x=="Gaming").sum()*10)
)

# Label logic
def classify(total):
    if total < 180:
        return 0
    elif total <= 300:
        return 1
    else:
        return 2

daily["Label"] = daily["Total_Minutes"].apply(classify)

X = daily[["Total_Minutes","Social_Min","Study_Min","Entertainment_Min","Gaming_Min"]]
y = daily["Label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "addiction_model.pkl")

print(" Model training complete! addiction_model.pkl saved.")
