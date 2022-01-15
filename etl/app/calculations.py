import numpy as np
from typing import List
from datetime import datetime

from app.models import Shift

def calculate_mean_break_length_in_minutes(shifts: List[Shift]) -> float:
    return np.mean([np.mean(list(map(lambda br: br.finish - br.start, shift.breaks)) or [0]) for shift in shifts] or [0]) / 1000 / 60


def calculate_mean_shift_cost(shifts: List[Shift]) -> float:
    return np.mean(list(map(lambda shift: shift.cost, shifts)) or [0]) / 1


def calculate_max_allowance_cost_14d(shifts: List[Shift]) -> float:
    shifts_14d = list(filter(lambda shift: (datetime.now() - datetime.strptime(shift.date, '%Y-%m-%d')).days <= 14, shifts))
    return np.max([np.max(list(map(lambda allowance: allowance.cost, shift.allowances)) or [0]) for shift in shifts_14d] or [0])


def calculate_min_shift_length_in_hours(shifts: List[Shift]) -> float:
    return np.min(list(map(lambda shift: shift.finish - shift.start, shifts)) or [0]) / 1000 / 60 / 60


def calculate_total_number_of_paid_breaks(shifts: List[Shift]) -> int:
    return int(np.sum([len(list(filter(lambda br: br.paid, shift.breaks))) for shift in shifts]))
