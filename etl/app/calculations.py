import numpy as np
from typing import List
from datetime import datetime

from app.models import Shift, KPI


def get_kpi_statistic(shifts: List[Shift]) -> List[KPI]:
    """
    :param shifts: List of shifts data
    :return: KPI statistic values
    """
    return [
        KPI(name='mean_break_length_in_minutes', value=_calculate_mean_break_length_in_minutes(shifts)),
        KPI(name='mean_shift_cost', value=_calculate_mean_shift_cost(shifts)),
        KPI(name='max_allowance_cost_14d', value=_calculate_max_allowance_cost_14d(shifts)),
        KPI(name='max_break_free_shift_period_in_days', value=_calculate_max_break_free_shift_period_in_days(shifts)),
        KPI(name='min_shift_length_in_hours', value=_calculate_min_shift_length_in_hours(shifts)),
        KPI(name='total_number_of_paid_breaks', value=_calculate_total_number_of_paid_breaks(shifts))
    ]


def _calculate_mean_break_length_in_minutes(shifts: List[Shift]) -> float:
    """
    :param shifts: List of shifts data
    :return: Mean shift break time in minutes (breaks.start and breaks.finish).
    """
    return np.mean([np.mean(list(map(lambda br: br.finish - br.start, shift.breaks)) or [0]) for shift in shifts] or [0]) / 1000.0 / 60


def _calculate_mean_shift_cost(shifts: List[Shift]) -> float:
    """
    :param shifts: List of shifts data
    :return: Mean shift cost (shifts.cost).
    """
    return np.mean(list(map(lambda shift: shift.cost, shifts)) or [0]) / 1.0


def _calculate_max_allowance_cost_14d(shifts: List[Shift]) -> float:
    """
    :param shifts: List of shifts data
    :return: Max allowance cost in the last 14 days (allowances.cost).
    """
    shifts_14d = list(filter(lambda shift: (datetime.now() - datetime.strptime(shift.date, '%Y-%m-%d')).days <= 14, shifts))
    return np.max([np.max(list(map(lambda allowance: allowance.cost, shift.allowances)) or [0]) for shift in shifts_14d] or [0])


def _calculate_max_break_free_shift_period_in_days(shifts: List[Shift]) -> float:
    """
    :param shifts: List of shifts data
    :return: Longest period in days when consecutive shifts did not have breaks.
    """

    periods = []
    before_date = None

    for index, shift in enumerate(shifts):
        if len(shift.breaks) <= 0 and not before_date:
            before_date = shift.date
        if len(shift.breaks) > 0 or index == len(shifts) - 1:
            if before_date:
                periods.append((datetime.strptime(shift.date, '%Y-%m-%d') - datetime.strptime(before_date, '%Y-%m-%d')).days)
            before_date = None

    return np.max(periods or [0])


def _calculate_min_shift_length_in_hours(shifts: List[Shift]) -> float:
    """
    :param shifts: List of shifts data
    :return: Shortest shift duration (shift.start and shift.finish).
    """
    return np.min(list(map(lambda shift: shift.finish - shift.start, shifts)) or [0]) / 1000.0 / 60 / 60


def _calculate_total_number_of_paid_breaks(shifts: List[Shift]) -> int:
    """
    :param shifts: List of shifts data
    :return: Total number of paid shift breaks (breaks.is_paid).
    """
    return int(np.sum([len(list(filter(lambda br: br.paid, shift.breaks))) for shift in shifts]))
