from pydantic import BaseModel

class Weather(BaseModel):
    temperature: float
    humidity: float
    pressure: float
    wind_speed: float
    wind_direction: str
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "temperature": 22.5,
                "humidity": 60,
                "pressure": 1012,
                "wind_speed": 5.5,
                "wind_direction": "N",
                "description": "Clear sky"
            }
        }