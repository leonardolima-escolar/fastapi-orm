from cqrs.signup.handlers import IQueryHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.signup.queries import SignupListQuery, SignupRecordQuery
from sqlalchemy.orm import Session


class ListSignupQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)
        self.query: SignupListQuery = SignupListQuery()

    async def handle(self) -> SignupListQuery:
        data = self.repo.get_all_signup()
        self.query.records = data
        return self.query


class RecordSignupQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)
        self.query: SignupRecordQuery = SignupRecordQuery()

    async def handle(self, id) -> SignupListQuery:
        data = self.repo.get_signup(id)
        self.query.record = data
        return self.query
