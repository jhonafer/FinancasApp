from datetime import date
from pydantic import BaseModel
from typing import Optional


class SaldoDiarioModel(BaseModel):
    data: date
    valor: float
