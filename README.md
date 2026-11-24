# Mutual Fund Analytics Capstone

## Objective
Analyze mutual fund schemes, performance, investor transactions, SIP trends, fund-house AUM, folio growth, portfolio holdings, NAV history and benchmark indices.

## Dataset inventory
The `data/raw` folder contains the 10 CSV datasets supplied for the capstone:
1. Fund master
2. NAV history
3. AUM by fund house
4. Monthly SIP inflows
5. Category inflows
6. Industry folio count
7. Scheme performance
8. Investor transactions
9. Portfolio holdings
10. Benchmark indices

## Tools
- Python
- Pandas
- CSV datasets
- SQL (next project stage)
- Power BI (dashboard stage)

## Run the analysis
1. Open this folder in PyCharm.
2. Install dependencies in the PyCharm terminal:
   `python -m pip install pandas`
3. Run:
   `python src/analyze.py`

The script writes summary CSV files into `outputs/`.

## Important
This is an educational analytics project, not investment advice. Results depend on the supplied datasets. Check data definitions and date coverage before drawing conclusions.
