from typing import List
from domain.data.sqlalchemy_models import Login


class LoginListQuery:
    def __init__(self):
        self._records: List[Login] = list()

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records


class LoginRecordQuery:
    def __init__(self):
        self._record: Login = None

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record
