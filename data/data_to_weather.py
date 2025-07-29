# parse_weather.py
import xml.etree.ElementTree as ET

def parse_weather_reports(macao_xml: ET.Element) -> list:
    """從 XML 根元素解析所有 WeatherReport，並轉換為結構化的 JSON 列表。"""
    weather_reports = []
    # 找到所有 WeatherReport 元素
    for report in macao_xml.findall('.//WeatherReport'):
        station_element = report.find('station')
        if station_element is not None:
            station_data = {
                "station_code": station_element.get('code'),
                "station_name": station_element.findtext('stationname', default='N/A'),
                "record_time": station_element.findtext('RecordTime', default='N/A')
            }

            # --- 解析各種天氣參數 ---
            # 溫度 (當前/最高/最低)
            temp_element = station_element.find('Temperature')
            if temp_element is not None:
                station_data["temperature"] = {
                    "value": temp_element.findtext('Value', default=None),
                    "unit": temp_element.findtext('MeasureUnit', default='N/A'),
                    "description": "當前溫度"
                }
            temp_max_element = station_element.find('Temperature_daily_max')
            if temp_max_element is not None:
                station_data["temperature_max"] = {
                    "value": temp_max_element.findtext('Value', default=None),
                    "unit": temp_max_element.findtext('MeasureUnit', default='N/A'),
                    "description": "當日最高溫度"
                }
            temp_min_element = station_element.find('Temperature_daily_min')
            if temp_min_element is not None:
                station_data["temperature_min"] = {
                    "value": temp_min_element.findtext('Value', default=None),
                    "unit": temp_min_element.findtext('MeasureUnit', default='N/A'),
                    "description": "當日最低溫度"
                }

            # 濕度
            humidity_element = station_element.find('Humidity')
            if humidity_element is not None:
                station_data["humidity"] = {
                    "value": humidity_element.findtext('Value', default=None),
                    "unit": humidity_element.findtext('MeasureUnit', default='N/A'),
                    "description": "相對濕度"
                }

            # 露點
            dewpoint_element = station_element.find('DewPoint')
            if dewpoint_element is not None:
                station_data["dew_point"] = {
                    "value": dewpoint_element.findtext('Value', default=None),
                    "unit": dewpoint_element.findtext('MeasureUnit', default='N/A'),
                    "description": "露點溫度"
                }

            # 風速與風 gust
            wind_speed_element = station_element.find('WindSpeed')
            if wind_speed_element is not None:
                station_data["wind_speed"] = {
                    "value": wind_speed_element.findtext('Value', default=None),
                    "unit": wind_speed_element.findtext('MeasureUnit', default='N/A'),
                    "description": "風速"
                }
            wind_gust_element = station_element.find('WindGust')
            if wind_gust_element is not None:
                station_data["wind_gust"] = {
                    "value": wind_gust_element.findtext('Value', default=None),
                    "unit": wind_gust_element.findtext('MeasureUnit', default='N/A'),
                    "description": "最大風速 (陣風)"
                }

            # 風向
            wind_dir_element = station_element.find('WindDirection')
            if wind_dir_element is not None:
                station_data["wind_direction"] = {
                    "direction_code": wind_dir_element.findtext('Value', default=None), # 例如 SW
                    "direction_degrees": wind_dir_element.findtext('Degree', default=None), # 例如 225
                    "description": wind_dir_element.findtext('WindDescription', default='N/A'), # 例如 西南
                    "unit": wind_dir_element.findtext('MeasureUnit', default='N/A')
                }

            # 降雨量 (有多種類型，這裡選取主要的)
            # Type 3: Hourly, Type 4: Daily, Type 5: Cumulative
            rainfall_data = {}
            for rainfall_element in station_element.findall('Rainfall'):
                rain_type = rainfall_element.findtext('Type', default='unknown')
                rain_value = rainfall_element.findtext('Value', default=None)
                rain_unit = rainfall_element.findtext('MeasureUnit', default='N/A')
                if rain_type == '3':
                    rainfall_data["hourly"] = {"value": rain_value, "unit": rain_unit, "description": "小時降雨量"}
                elif rain_type == '4':
                    rainfall_data["daily"] = {"value": rain_value, "unit": rain_unit, "description": "當日降雨量"}
                elif rain_type == '5':
                    rainfall_data["cumulative"] = {"value": rain_value, "unit": rain_unit, "description": "累積降雨量"}
            if rainfall_data:
                 station_data["rainfall"] = rainfall_data

            # 氣壓
            msl_pressure_element = station_element.find('MeanSeaLevelPressure')
            if msl_pressure_element is not None:
                station_data["mean_sea_level_pressure"] = {
                    "value": msl_pressure_element.findtext('Value', default=None),
                    "unit": msl_pressure_element.findtext('MeasureUnit', default='N/A'),
                    "description": "平均海平面氣壓"
                }
            station_pressure_element = station_element.find('StationPressure')
            if station_pressure_element is not None:
                station_data["station_pressure"] = {
                    "value": station_pressure_element.findtext('Value', default=None),
                    "unit": station_pressure_element.findtext('MeasureUnit', default='N/A'),
                    "description": "測站氣壓"
                }

            weather_reports.append(station_data)

    #final_json = json.dumps(weather_reports, indent=4, ensure_ascii=False)
    return weather_reports