from typing import List
from pydantic import BaseModel

from app.models import Shift, Break, Allowance, AwardInterpretation, KPI


def bulk_insert(table: str, rows: List[BaseModel], shift: Shift = None) -> str:
    """
    :param table: Name of SQL table on which bulk insertion should be performed,
    should be one of 'shifts', 'breaks', 'allowances', 'award_interpretations' or 'kpis'
    :param rows: List of objects representing rows that should bo stored in the db
    :return: SQL bulk insert command for storing provided data
    """
    if not rows:
        return None
    return "insert into %s %s values %s on conflict do nothing;" \
           % (table, COLUMN_VALUES[table], ",".join([INSERT_COMMANDS[table](row, sh=shift) for row in rows]))


def _shift_insert(shf: Shift, **kwargs) -> str:
    """
    :param shf: Shift data needed to bo stored in the db
    :return: Value part of SQL insert command for saving shift data
    """
    return "('%s', '%s', to_timestamp(cast(%s/1000 as bigint))::date, to_timestamp(cast(%s/1000 as bigint))::date, %s)" \
           % (shf.id, shf.date, shf.start, shf.finish, shf.cost)


def _break_insert(br: Break, **kwargs) -> str:
    """
    :param br: Break data needed to bo stored in the db
    :param sh: Corresponding Shift data
    :return: Value part of SQL insert command for saving break data
    """
    return "('%s','%s',to_timestamp(cast(%s/1000 as bigint))::date,to_timestamp(cast(%s/1000 as bigint))::date,%s)" \
           % (br.id, kwargs['sh'].id, br.start, br.finish, 'true' if br.paid else 'false')


def _allowance_insert(al: Allowance, **kwargs) -> str:
    """
    :param al: Allowance data needed to bo stored in the db
    :param sh: Corresponding Shift data
    :return: Value part of SQL insert command for saving allowance data
    """
    return "('%s','%s',%s,%s)" % (al.id, kwargs['sh'].id, al.value, al.cost)


def _award_interpretation_insert(aw: AwardInterpretation, **kwargs) -> str:
    """
    :param aw: Award interpretation data needed to bo stored in the db
    :param sh: Corresponding Shift data
    :return: Value part of SQL insert command for saving award interpretation data
    """
    return "('%s','%s','%s',%s,%s)" % (aw.id, kwargs['sh'].id, aw.date, aw.units, aw.cost)


def _kpi_insert(kpi: KPI, **kwargs) -> str:
    """
    :param kpi: KPI data needed to be stored in the db
    :return: Value part of SQL insert command for saving KPI
    """
    return "('%s', current_timestamp, %s)" % (kpi.name, kpi.value)


COLUMN_VALUES = {
    "shifts": "",
    "breaks": "",
    "allowances": "",
    "award_interpretations": "",
    "kpis": "(kpi_name, kpi_date, kpi_value)"
}

INSERT_COMMANDS = {
    "shifts": _shift_insert,
    "breaks": _break_insert,
    "allowances": _allowance_insert,
    "award_interpretations": _award_interpretation_insert,
    "kpis": _kpi_insert
}

