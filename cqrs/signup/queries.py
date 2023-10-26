from typing import List
from domain.data.sqlalchemy_models import Signup


class SignupListQuery:
    def __init__(self):
        self._records: List[Signup] = list()

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records


class SignupRecordQuery:
    def __init__(self):
        self._record: Signup = None

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record
