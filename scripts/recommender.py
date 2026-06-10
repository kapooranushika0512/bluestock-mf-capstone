import pandas as pd

# Load scheme performance data
performance = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

print("Available Risk Grades:")
print(performance["risk_grade"].unique())

# User input
risk_appetite = input(
    "Enter Risk Appetite (Low / Moderate / High / Very High / Moderately High): "
).title()

# Recommendations
recommendations = (
    performance[
        performance["risk_grade"] == risk_appetite
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    [
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "aum_crore"
        ]
    ]
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")
print(recommendations.to_string(index=False))

# Save recommendations
recommendations.to_csv(
    "reports/fund_recommendations.csv",
    index=False
)

print("\nRecommendations saved to reports/fund_recommendations.csv")