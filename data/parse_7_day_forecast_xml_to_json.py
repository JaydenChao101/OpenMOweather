import xml.etree.ElementTree as ET
from typing import Union

def parse_7_day_forecast_xml_to_json(xml_input: Union[str, ET.Element]) -> list[dict]:
    # Accept ElementTree.Element or XML string
    if isinstance(xml_input, ET.Element):
        root = xml_input
    else:
        root = ET.fromstring(xml_input)

    forecast_list = []

    for weather in root.findall(".//WeatherForecast"):
        date = weather.findtext("ValidFor")
        day_of_week = weather.findtext("c_DayOfWeek")
        description = weather.findtext("WeatherDescription")

        # 提取氣溫（高、低）
        temps = weather.findall("Temperature")
        temp_high = next((int(t.findtext("Value")) for t in temps if t.findtext("Type") == "1"), None)
        temp_low = next((int(t.findtext("Value")) for t in temps if t.findtext("Type") == "2"), None)

        # 提取濕度（高、低）
        humidities = weather.findall("Humidity")
        humidity_high = next((int(h.findtext("Value")) for h in humidities if h.findtext("Type") == "1"), None)
        humidity_low = next((int(h.findtext("Value")) for h in humidities if h.findtext("Type") == "2"), None)

        forecast_list.append({
            "date": date,
            "day_of_week": day_of_week,
            "temp_high": temp_high,
            "temp_low": temp_low,
            "humidity_high": humidity_high,
            "humidity_low": humidity_low,
            "description": description,
        })

    return forecast_list
