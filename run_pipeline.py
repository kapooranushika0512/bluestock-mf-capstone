import subprocess

scripts = [
    "scripts/etl_pipeline.py",
    "scripts/load_to_sqlite.py",
    "scripts/live_nav_fetch.py",
    "scripts/compute_metrics.py",
    "scripts/recommender.py"
]

print("=" * 60)
print("BLUESTOCK MUTUAL FUND ANALYTICS PLATFORM")
print("=" * 60)

for script in scripts:

    print(f"\nRunning {script}...")

    try:
        subprocess.run(
            ["python", script],
            check=True
        )

        print(f"{script} completed successfully.")

    except Exception as e:

        print(f"Error while running {script}")
        print(e)

print("\nPipeline execution completed.")