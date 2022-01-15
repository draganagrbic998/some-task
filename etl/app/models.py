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
    id: str = Field(description="AwardInterpretation UUID")
    date: str = Field(description="Award interpretation date in YYYY-MM-DD format")
    units: float = Field(description="AwardInterpretation units")
    cost: float = Field(description="AwardInterpretation cost")


class Shift(BaseModel):
    id: str = Field(description="Shift UUID")
    date: str = Field(description="Shift start date in YYYY-MM-DD format")
    start: int = Field(description="Shift start as Unix timestamp in milliseconds")
    finish: int = Field(description="Shift finish as Unix timestamp in milliseconds")
    breaks: List[Break] = Field([], description="List of breaks during shift")
    allowances: List[Allowance] = Field(
        [], description="List of allowances during shift"
    )
    award_interpretations: List[AwardInterpretation] = Field(
        [], description="List of shift award interpretations"
    )
    cost: Optional[float] = Field(0, description="Shift total cost")


class EtlRequest(BaseModel):
    results: List[Shift] = Field([], description="Shifts data")
