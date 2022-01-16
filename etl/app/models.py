from pydantic import BaseModel, Field
from typing import List, Optional


class Break(BaseModel):
    id: str = Field(description="Break UUID")
    start: int = Field(description="Break start as Unix timestamp in milliseconds")
    finish: int = Field(description="Break finish as Unix timestamp in milliseconds")
    paid: bool = Field(description="Indicates whether break is paid or not")


class Allowance(BaseModel):
    id: str = Field(description="Allowance UUID")
    value: float = Field(description="Allowance value")
    cost: float = Field(description="Allowance cost")


class AwardInterpretation(BaseModel):
    id: str = Field(description="Award interpretation UUID")
    date: str = Field(description="Award interpretation date in YYYY-MM-DD format")
    units: float = Field(description="Award interpretation units")
    cost: float = Field(description="Award interpretation cost")


class Shift(BaseModel):
    id: str = Field(description="Shift UUID")
    date: str = Field(description="Shift start date in YYYY-MM-DD format")
    start: int = Field(description="Shift start as Unix timestamp in milliseconds")
    finish: int = Field(description="Shift finish as Unix timestamp in milliseconds")
    breaks: List[Break] = Field([], description="List of breaks during shift")
    allowances: List[Allowance] = Field([], description="List of allowances during shift")
    award_interpretations: List[AwardInterpretation] = Field([], description="List of shift award interpretations")
    cost: Optional[float] = Field(0, description="Shift total cost")


class KPI(BaseModel):
    name: str = Field(description="KPI name")
    value: float = Field(description="KPI value")


class EtlRequest(BaseModel):
    results: List[Shift] = Field([], description="Shifts list")

    class Config:
        schema_extra = {
            "example": {
                "results": [
                    {
                        "id": "0438ff1e-5160-4cdf-bc18-2d84b96f556d",
                        "date": "2021-01-01",
                        "start": 1609484400000,
                        "finish": 1609527600000,
                        "breaks": [
                            {
                                "id": "c1ccfad9-50f6-417d-a52e-afb0d18f6763",
                                "start": 1609498800000,
                                "finish": 1609502400000,
                                "paid": False,
                            }
                        ],
                        "allowances": [
                            {
                                "id": "7cf3d3a8-1ac1-4616-afa8-dcf3ae4b0474",
                                "value": 1.0,
                                "cost": 11.8,
                            },
                            {
                                "id": "76fa2b79-a4ad-4a5d-8fc1-ef19cdc3d7af",
                                "value": 1.0,
                                "cost": 15.0,
                            },
                        ],
                        "award_interpretations": [
                            {
                                "id": "81b2430d-60be-40b0-ba66-b736027e4572",
                                "date": "2021-01-01",
                                "units": 1.0,
                                "cost": 8.43,
                            }
                        ],
                    }
                ],
            }
        }
