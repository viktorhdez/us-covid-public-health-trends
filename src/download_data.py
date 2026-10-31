"""Download the raw COVID-19 data files into data/raw/."""
from pathlib import Path
from urllib.request import urlretrieve

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

SOURCES = {
    "time_series_covid19_deaths_US.csv": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv",
    "time_series_covid19_confirmed_US.csv": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv",
    "us_state_vaccinations.csv": "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv",
}

RAW_DIR.mkdir(parents=True, exist_ok=True)

for filename, url in SOURCES.items():
    target = RAW_DIR / filename
    if target.exists():
        print(f"File {filename} is already downloaded")
        continue
    print(f"Downloading {filename}...")
    urlretrieve(url, target)
    print(f"    saved {target.stat().st_size / 1e6:.1f} MB")
    