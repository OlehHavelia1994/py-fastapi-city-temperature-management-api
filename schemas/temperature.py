from pydantic import BaseModel
from datetime import date


class BaseTemperature(BaseModel):
    date_time: date
    temperature: float


class CreateTemperature(BaseTemperature):
    city_id: int


class GetTemperature(BaseTemperature):
    id: int
    city_id: int

    class Config:
        from_attributes = True