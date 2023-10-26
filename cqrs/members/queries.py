from typing import List
from domain.data.sqlalchemy_models import Profile_Members


class ProfileMemberListQuery:
    def __init__(self):
        self._records: List[Profile_Members] = list()

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records


class ProfileMemberRecordQuery:
    def __init__(self):
        self._record: Profile_Members = None

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record
