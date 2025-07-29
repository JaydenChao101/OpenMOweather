from fastapi import FastAPI
from API.get import get_weather, get_radar_chart, get_lighting_location, day_7_forecast
from data.data_to_weather import parse_weather_reports
from data.parse_7_day_forecast_xml_to_json import parse_7_day_forecast_xml_to_json

app = FastAPI()


@app.get("/weather")
async def weather():
    """Get current weather data."""
    try:
        xml_data = await get_weather()
        return parse_weather_reports(xml_data)
    except Exception as e:
        return {"error": str(e)}


@app.get("/radar-chart")
async def radar_chart():
    """Get radar chart data."""
    try:
        return await get_radar_chart()
    except Exception as e:
        return {"error": str(e)}


@app.get("/lighting-location")
async def lightning_location():
    """Get lightning location data."""
    try:
        return await get_lighting_location()
    except Exception as e:
        return {"error": str(e)}


@app.get("/7-day-forecast")
async def seven_day_forecast():
    """Get 7-day weather forecast."""
    try:
        xml_data = await day_7_forecast()
        return parse_7_day_forecast_xml_to_json(xml_data)
    except Exception as e:
        return {"error": str(e)}