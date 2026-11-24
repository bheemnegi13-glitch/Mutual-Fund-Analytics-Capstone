from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project folders
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"
REPORTS = ROOT / "reports"
OUTPUT = REPORTS / "outputs"

OUTPUT.mkdir(parents=True, exist_ok=True)

print("MUTUAL FUND ANALYTICS CAPSTONE")
print("--------------------------------")

# Read all CSV files
dataframes = {}

for file in DATA.glob("*.csv"):
    try:
        df = pd.read_csv(file)
        dataframes[file.stem] = df
        print(f"Loaded: {file.name} | Rows: {len(df)}")
    except Exception as e:
        print(f"Error reading {file.name}: {e}")

if not dataframes:
    print("No CSV files found. Please check the data/raw folder.")
    raise SystemExit

# Dataset summary
summary = []

for name, df in dataframes.items():
    summary.append({
        "Dataset": name,
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    })

summary_df = pd.DataFrame(summary)

# Save Excel report
excel_path = OUTPUT / "Mutual_Fund_Analytics_Report.xlsx"

with pd.ExcelWriter(excel_path) as writer:
    summary_df.to_excel(
        writer, sheet_name="Dataset Summary", index=False
    )

    for name, df in dataframes.items():
        sheet_name = name[:31]
        df.head(1000).to_excel(
            writer, sheet_name=sheet_name, index=False
        )

# Save individual dataset summaries
summary_df.to_csv(
    OUTPUT / "Dataset_Summary.csv", index=False
)

# Create numerical charts
for name, df in dataframes.items():

    numeric_df = df.select_dtypes(include="number")

    for column in numeric_df.columns[:3]:
        plt.figure(figsize=(9, 5))
        numeric_df[column].dropna().hist(bins=20)
        plt.title(f"{name} - {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.tight_layout()

        chart_name = f"{name}_{column}".replace("/", "_")
        plt.savefig(OUTPUT / f"{chart_name}.png")
        plt.close()

print("\nAnalysis completed successfully!")
print("Excel Report:", excel_path)
print("Output Folder:", OUTPUT)
print("\nDataset Summary:")
print(summary_df.to_string(index=False))