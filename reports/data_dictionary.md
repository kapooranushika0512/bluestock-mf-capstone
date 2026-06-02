# Data Dictionary

## 1. Fund Master Dataset (01_fund_master.csv)

| Column | Data Type | Description |
|----------|------------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Name of mutual fund scheme |
| category | Text | Equity, Debt, Hybrid etc. |
| sub_category | Text | Large Cap, Mid Cap, Small Cap etc. |
| plan | Text | Direct or Regular |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Annual expense ratio (%) |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP investment |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk classification |
| sebi_category_code | Text | SEBI category code |

Source: AMFI India

---

## 2. NAV History Dataset (02_nav_history.csv)

| Column | Data Type | Description |
|----------|------------|-------------|
| amfi_code | Integer | Fund scheme identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

Source: Historical NAV Records

---

## 3. Investor Transactions Dataset (08_investor_transactions.csv)

| Column | Data Type | Description |
|----------|------------|-------------|
| investor_id | Text | Unique investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Fund identifier |
| transaction_type | Text | SIP, Lumpsum, Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | Tier 1, Tier 2, Tier 3 |
| age_group | Text | Investor age segment |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income in lakhs |
| payment_mode | Text | UPI, Mandate, Net Banking etc. |
| kyc_status | Text | KYC verification status |

Source: Simulated Investor Activity Dataset

---

## 4. Scheme Performance Dataset (07_scheme_performance.csv)

| Column | Data Type | Description |
|----------|------------|-------------|
| amfi_code | Integer | Scheme identifier |
| scheme_name | Text | Scheme name |
| fund_house | Text | Fund house |
| category | Text | Fund category |
| plan | Text | Direct/Regular |
| return_1yr_pct | Float | One year return (%) |
| return_3yr_pct | Float | Three year return (%) |
| return_5yr_pct | Float | Five year return (%) |
| benchmark_3yr_pct | Float | Benchmark return |
| alpha | Float | Alpha measure |
| beta | Float | Beta measure |
| sharpe_ratio | Float | Risk-adjusted return |
| sortino_ratio | Float | Downside risk metric |
| std_dev_ann_pct | Float | Annualized volatility |
| max_drawdown_pct | Float | Maximum drawdown |
| aum_crore | Float | Assets under management |
| expense_ratio_pct | Float | Expense ratio |
| morningstar_rating | Integer | Morningstar rating |
| risk_grade | Text | Risk grade |

Source: Simulated Mutual Fund Performance Dataset