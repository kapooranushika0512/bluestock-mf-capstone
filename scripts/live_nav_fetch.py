import requests
import pandas as pd
from pathlib import Path

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

save_dir = Path("data/raw")

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url, timeout=30)

        if response.status_code == 200:

            data = response.json()

            if "data" in data:

                nav_df = pd.DataFrame(data["data"])

                nav_df.to_csv(
                    save_dir / f"{name}_live_nav.csv",
                    index=False
                )

                print(f"Saved {name}")

            else:
                print(f"No NAV data for {name}")

        else:
            print(f"Failed {name} - Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error for {name}: {e}")