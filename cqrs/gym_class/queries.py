from typing import List
from domain.data.sqlalchemy_models import Gym_Class


class GymClassListQuery:
    def __init__(self):
        self._records: List[Gym_Class] = list()

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records


class GymClassRecordQuery:
    def __init__(self):
        self._record: Gym_Class = None

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record
