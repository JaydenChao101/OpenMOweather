import aiohttp
import xml.etree.ElementTree as ET
from typing import Literal

async def get_weather(lang: Literal["e","c","p"] = "e") -> ET.Element:
    """Fetches weather data from an external API.
    https://xml.smg.gov.mo/c_actualweather.xml is the source of the weather data.
    """
    url = f"https://xml.smg.gov.mo/{lang}_actualweather.xml"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                root = ET.fromstring(data)
                return root
            else:
                raise Exception(f"Failed to fetch weather data: {response.status}")


async def get_radar_chart() -> dict:
    """Fetches radar chart data from an external API.
    https://cms.smg.gov.mo/zh_TW/api/imageseries/MTSAT is the source of the radar chart data.
    """
    url = "https://cms.smg.gov.mo/zh_TW/api/imageseries/MTSAT"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                raise Exception(f"Failed to fetch radar chart data: {response.status}")

async def get_lighting_location() -> dict:
    """Fetches lightning location data from an external API.
    https://cms.smg.gov.mo/zh_TW/api/imageseries/llis10 is the source of the lightning location data.
    """
    url = "https://cms.smg.gov.mo/zh_TW/api/imageseries/llis10"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                raise Exception(f"Failed to fetch lightning location data: {response.status}")

async def day_7_forecast(lang: Literal["e","c","p"] = "e") -> ET.Element:
    """Fetches 7-day weather forecast data from an external API.
    https://xml.smg.gov.mo/c_7daysforecast.xml is the source of the 7-day weather forecast data.
    """
    url = f"https://xml.smg.gov.mo/{lang}_7daysforecast.xml"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                root = ET.fromstring(data)
                return root
            else:
                raise Exception(f"Failed to fetch 7-day forecast data: {response.status}")