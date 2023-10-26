from cqrs.gym_class.handlers import IQueryHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.gym_class.queries import GymClassListQuery, GymClassRecordQuery
from sqlalchemy.orm import Session


class ListGymClassQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)
        self.query: GymClassListQuery = GymClassListQuery()

    async def handle(self) -> GymClassListQuery:
        data = self.repo.get_all_gym_class()
        self.query.records = data
        return self.query


class RecordGymClassQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)
        self.query: GymClassRecordQuery = GymClassRecordQuery()

    async def handle(self, id) -> GymClassListQuery:
        data = self.repo.get_gym_class(id)
        self.query.record = data
        return self.query
