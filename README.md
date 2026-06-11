# Bluestock Mutual Fund Analytics Platform

## Project Overview
The Bluestock Mutual Fund Analytics Platform is an end-to-end data analytics project designed to analyze the Indian mutual fund industry using historical NAV data, fund performance metrics, SIP inflows, investor transactions, portfolio holdings, and benchmark indices.

The project implements a complete analytics pipeline including data ingestion, ETL processing, exploratory data analysis, performance evaluation, risk analytics, dashboard development, and advanced financial modeling.

## Objectives
- Analyze mutual fund industry trends and growth.
- Evaluate fund performance using financial metrics.
- Study investor behavior and SIP investment patterns.
- Develop interactive dashboards for business insights.
- Perform advanced risk and return analytics.
- Build recommendation and portfolio optimization systems.

## Technology Stack
### Programming
- Python
- SQL

### Libraries
- Pandas
- NumPy
- Matplotlib
- SQLite3

### Visualization
- Tableau

### Development Tools
- Jupyter Notebook
- VS Code
- Git


## Project Structure
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│   ├── Dashboard.pdf
│   ├── Dashboard1_Industry_Overview.png
│   ├── Dashboard2_Fund_Performance.png
│   ├── Dashboard3_Investor_Analytics.png
│   └── Dashboard4_SIP_Market_Trends.png
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_performance_analysis.ipynb
│   ├── 05_advanced_analytics.ipynb
│   ├── 06_monte_carlo_simulation.ipynb
│   └── 07_portfolio_optimization.ipynb
│
├── reports/
│   ├── var_cvar_report.csv
│   ├── fund_recommendations.csv
│   ├── hhi_concentration.csv
│   ├── rolling_sharpe_chart.png
│   ├── monte_carlo_projection.png
│   ├── efficient_frontier.png
│   └── performance_metrics_summary.csv
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── load_to_sqlite.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
│
├── sql/
│
├── run_pipeline.py
├── README.md
└── requirements.txt

## Datasets Used
1. Fund Master Data
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

## ETL Workflow
1. Raw datasets collected and validated.
2. Data cleaning and preprocessing performed.
3. Missing values handled appropriately.
4. Cleaned datasets stored in processed format.
5. Data loaded into SQLite database.
6. Performance metrics calculated.
7. Dashboard datasets prepared.

## Dashboard Pages
### Page 1 – Industry Overview
- Total Industry AUM
- Monthly SIP Inflows
- Active SIP Accounts
- Fund House Comparison

### Page 2 – Fund Performance Analysis
- Sharpe Ratio Analysis
- Alpha vs Beta
- Fund Ranking
- Risk Category Analysis

### Page 3 – Investor Analytics
- Investor Demographics
- Transaction Trends
- Geographic Distribution
- Income Analysis

### Page 4 – SIP & Market Trends
- SIP Growth Trends
- Category Inflows
- Folio Growth
- Market Participation Analysis

## Advanced Analytics
### Historical VaR & CVaR
Measures downside investment risk using historical return distributions.

### Rolling 90-Day Sharpe Ratio
Tracks risk-adjusted performance over time.

### Investor Cohort Analysis
Analyzes investment behavior by investor entry year.

### SIP Continuity Analysis
Identifies potentially at-risk investors based on SIP gaps.

### Fund Recommendation Engine
Provides top fund recommendations based on risk appetite.

### Sector Concentration Analysis
Uses Herfindahl-Hirschman Index (HHI) to evaluate portfolio diversification.

## Bonus Features
### Monte Carlo Simulation
Future NAV projection using stochastic simulations.

### Portfolio Optimization
Efficient Frontier analysis for portfolio allocation.

### Live NAV Fetcher
Automated NAV retrieval system.

### Master Pipeline Automation
Single-command execution using:

bash python run_pipeline.py 

## How to Run
### Install Dependencies
bash pip install -r requirements.txt 

### Run Complete Pipeline
bash python run_pipeline.py 

### Run Individual Scripts
bash python scripts/etl_pipeline.py python scripts/load_to_sqlite.py python scripts/live_nav_fetch.py python scripts/compute_metrics.py python scripts/recommender.py 

## Key Deliverables
- Interactive Tableau Dashboard
- SQLite Database
- ETL Pipeline
- Advanced Analytics Notebook
- Monte Carlo Simulation
- Portfolio Optimization
- Fund Recommendation System
- Final Project Report
- Presentation Deck

## Future Enhancements
- Real-time NAV updates via API.
- Machine learning based fund recommendation.
- Investor churn prediction.
- Web-based dashboard deployment.
- Automated reporting framework.

## Author
Anushika Kapoor

Bluestock Mutual Fund Analytics Capstone Project