# NAV Auto-Fetch Scheduler

This scheduler automatically executes the NAV ingestion script every weekday at 8 PM.

## Cron Schedule

```cron
0 20 * * 1-5 /usr/bin/python3 /Users/anushikakapoor/bluestock_mf_capstone/scripts/live_nav_fetch.py
```

## Purpose

- Automatically fetch latest NAV data
- Reduce manual intervention
- Keep mutual fund analytics database up to date

## Expected Output

- Updated NAV CSV files
- Refreshed analytics datasets
- Ready for dashboard refresh