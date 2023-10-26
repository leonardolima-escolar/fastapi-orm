from cqrs.login.handlers import IQueryHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.login.queries import LoginListQuery, LoginRecordQuery
from sqlalchemy.orm import Session


class ListLoginQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)
        self.query: LoginListQuery = LoginListQuery()

    async def handle(self) -> LoginListQuery:
        data = self.repo.get_all_login()
        self.query.records = data
        return self.query


class RecordLoginQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)
        self.query: LoginRecordQuery = LoginRecordQuery()

    async def handle(self, id) -> LoginListQuery:
        data = self.repo.get_login(id)
        self.query.record = data
        return self.query
