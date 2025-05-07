from fastapi import FastAPI
import httpx
import asyncio
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


WORLD_BANK_API = "http://api.worldbank.org/v2"

metrics = {
    "GDP": "NY.GDP.MKTP.CD",
    "GDP Growth (%)": "NY.GDP.MKTP.KD.ZG",
    "Population": "SP.POP.TOTL",
    "Life Expectancy": "SP.DYN.LE00.IN",
    "Inflation": "FP.CPI.TOTL.ZG",
    "Net Migration": "SM.POP.NETM",
    "Internet Users (% of population)": "IT.NET.USER.ZS"
}


semaphore = asyncio.Semaphore(100)


async def get_country_codes():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{WORLD_BANK_API}/country?format=json&per_page=300")
        countries = resp.json()[1]
        return [{"name": c["name"], "code": c["id"]} for c in countries if c["region"]["value"] != "Aggregates"]

async def get_indicator(country_code, indicator, year):
    async with semaphore:
        async with httpx.AsyncClient() as client:
            url = f"{WORLD_BANK_API}/country/{country_code}/indicator/{indicator}?date={year}&format=json&per_page=1"
            resp = await client.get(url)
            try:
                return resp.json()[1][0]["value"]
            except Exception as e:
                return {"error": str(e)}


@app.get("/")
async def serve_home():
    return FileResponse("static/index.html")


@app.get("/data")
async def fetch_data(year: str = "2024"):
    countries = await get_country_codes()

    async def fetch_country_data(c):
        data = {"country": c["name"]}
        results = await asyncio.gather(
            *[get_indicator(c["code"], ind, year) for ind in metrics.values()]
        )
        for key, value in zip(metrics.keys(), results):
            data[key] = value
        return data

    tasks = [fetch_country_data(c) for c in countries]
    return await asyncio.gather(*tasks)
