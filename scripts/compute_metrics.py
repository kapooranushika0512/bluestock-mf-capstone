import pandas as pd

df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

print("=" * 60)
print("MUTUAL FUND PERFORMANCE METRICS")
print("=" * 60)

top_sharpe = (
    df.sort_values(
        "sharpe_ratio",
        ascending=False
    )
    [["scheme_name", "sharpe_ratio"]]
    .head(5)
)

print("\nTop 5 Funds by Sharpe Ratio")
print(top_sharpe.to_string(index=False))

top_returns = (
    df.sort_values(
        "return_3yr_pct",
        ascending=False
    )
    [["scheme_name", "return_3yr_pct"]]
    .head(5)
)

print("\nTop 5 Funds by 3-Year Return")
print(top_returns.to_string(index=False))

summary = pd.DataFrame({
    "metric": [
        "avg_sharpe_ratio",
        "avg_sortino_ratio",
        "avg_alpha",
        "avg_beta",
        "avg_3yr_return"
    ],
    "value": [
        round(df["sharpe_ratio"].mean(), 2),
        round(df["sortino_ratio"].mean(), 2),
        round(df["alpha"].mean(), 2),
        round(df["beta"].mean(), 2),
        round(df["return_3yr_pct"].mean(), 2)
    ]
})

summary.to_csv(
    "reports/performance_metrics_summary.csv",
    index=False
)

print("\nSaved:")
print("reports/performance_metrics_summary.csv")